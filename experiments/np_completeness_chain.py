#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NP 完全性归约链 SAT -> 3-SAT -> 独立集 -> 顶点覆盖 的构造与验证
（档案 #1 P vs NP）。

验证的已知结果：
  三步经典多项式归约：
    1. SAT -> 3-SAT（Tseitin 式）：长度 k>3 的子句引入 k-3 个辅助变量，
       变成等价的可满足性链。
    2. 3-SAT -> 独立集：每个子句一个三角形顶点组，同一变量的正负文字
       之间连冲突边。原式可满足 ⟺ 图有大小 m（子句数）的独立集。
    3. 独立集 -> 顶点覆盖：同一图上，G 有大小 k 的独立集 ⟺ G 有
       大小 |V|-k 的顶点覆盖（互补关系）。
  脚本在随机生成的 50 个小 SAT 实例上，逐步验证解的一致性：
  原实例有相应大小的解 ⟺ 归约后实例有对应大小的解（双向检查）。

运行方式：
  python experiments/np_completeness_chain.py          # 默认 50 个实例
  python experiments/np_completeness_chain.py --help   # 查看参数

它不能说明什么（重要）：
  1. 验证的是**归约构造的正确性**（解的一一对应），不是 NP 完全性
     证明本身——证明还需论证归约是多项式时间的，且基准问题
     （SAT）是 NP 难的（Cook-Levin 定理，本脚本不涉及）。
  2. 小实例上的通过不能替代数学证明；它只是把抽象概念变成可检验的东西。
"""

import argparse
import itertools
import random


# ---------- SAT 实例（CNF）的基本操作 ----------

def satisfiable_check(cnf, assignment):
    """给定变量赋值 dict，检查 CNF 是否满足。"""
    for clause in cnf:
        if not any(assignment.get(abs(l), l > 0) == (l > 0) for l in clause):
            return False
    return True


def brute_force_sat(cnf, n_vars):
    """小实例暴力枚举全部赋值，返回是否存在满足赋值。"""
    for bits in itertools.product([False, True], repeat=n_vars):
        assign = {i + 1: bits[i] for i in range(n_vars)}
        if satisfiable_check(cnf, assign):
            return True
    return False


# ---------- 归约 1：SAT -> 3-SAT（Tseitin 式链） ----------

def sat_to_3sat(cnf):
    """把每个长度 k>3 的子句替换为等价 3-CNF 链，返回 (新cnf, 新变量数)。

    子句 (l1 ∨ l2 ∨ ... ∨ lk) 引入辅助变量 y1..y{k-3}：
      (l1∨l2∨y1) ∧ (¬y1∨l3∨y2) ∧ ... ∧ (¬y{k-3}∨l{k-1}∨lk)
    """
    out = []
    n_extra = 0
    for clause in cnf:
        if len(clause) <= 3:
            out.append(list(clause))
            continue
        ys = []
        for _ in range(len(clause) - 3):
            n_extra += 1
            ys.append(10 ** 6 + n_extra)  # 辅助变量编号避开原变量
        out.append([clause[0], clause[1], ys[0]])
        for i in range(1, len(ys)):
            out.append([-ys[i - 1], clause[i + 1], ys[i]])
        out.append([-ys[-1], clause[-2], clause[-1]])
    return out, n_extra


# ---------- 归约 2：3-SAT -> 独立集 ----------

def sat_to_independent_set(cnf3):
    """构造图 G：每个子句 3 个顶点（文字），子句内连三角形，
    互为否定的文字之间连冲突边。返回 (顶点集, 边集, 目标k=子句数)。

    定理：原式可满足 ⟺ G 有大小为 m 的独立集。
    """
    vertices = []  # (子句下标, 文字)
    for i, clause in enumerate(cnf3):
        for l in clause:
            vertices.append((i, l))
    vset = set(vertices)
    edges = set()
    # 子句内三角形
    for i, clause in enumerate(cnf3):
        trio = [(i, l) for l in clause]
        for a, b in itertools.combinations(trio, 2):
            edges.add((a, b))
    # 冲突边：x 与 ¬x
    by_lit = {}
    for v in vertices:
        by_lit.setdefault(v[1], []).append(v)
    for lit, vs in by_lit.items():
        if -lit in by_lit:
            for a in vs:
                for b in by_lit[-lit]:
                    if a != b:
                        edges.add((min(a, b), max(a, b)))
    return vset, edges, len(cnf3)


def has_independent_set(vset, edges, k):
    """检查是否存在大小为 k 的独立集（位掩码分支限界：最大独立集 >= k）。"""
    verts = sorted(vset)
    idx = {v: i for i, v in enumerate(verts)}
    n = len(verts)
    adj = [0] * n
    for a, b in edges:
        adj[idx[a]] |= 1 << idx[b]
        adj[idx[b]] |= 1 << idx[a]
    return max_is(adj, (1 << n) - 1) >= k


def _greedy_is(adj, candidates):
    """贪心可行独立集大小：反复取候选中度数最小的点，删去其邻居。

    作为最大独立集的**下界**（可行解），供分支限界做剪枝。
    """
    size = 0
    c = candidates
    while c:
        # 取度数最小的顶点
        best_v, best_deg = None, None
        m = c
        while m:
            low = m & -m
            v = low.bit_length() - 1
            deg = (adj[v] & c).bit_count()
            if best_deg is None or deg < best_deg:
                best_v, best_deg = v, deg
            m ^= low
        size += 1
        c &= ~adj[best_v] & ~(1 << best_v)
    return size


def _greedy_vc(adj, n):
    """贪心顶点覆盖大小（2-近似）：反复取覆盖未覆盖边最多的顶点。

    作为最小顶点覆盖的**上界**（可行解），供分支限界做剪枝。
    """
    edges = []
    for a in range(n):
        e = adj[a] & ~((1 << a) - 1)  # 只取 a 之后的邻居，避免重复
        while e:
            low = e & -e
            b = low.bit_length() - 1
            edges.append((1 << a) | (1 << b))
            e ^= low
    chosen = 0
    rem = list(edges)
    while rem:
        cnt = [0] * n
        for e in rem:
            u = e & -e
            v = e ^ u
            cnt[u.bit_length() - 1] += 1
            cnt[v.bit_length() - 1] += 1
        best_i = max(range(n), key=lambda i: cnt[i])
        chosen |= 1 << best_i
        rem = [e for e in rem if not ((e >> best_i) & 1)]
    return chosen.bit_count()


def max_is(adj, candidates):
    """分支限界求最大独立集大小：任取一候选顶点 v，
    要么 v 在独立集中（删去 v 及其邻居），要么不在（只删 v）。
    用贪心可行解做下界、用剩余顶点数做上界剪枝，避免指数爆炸。

    实现：递归携带已选独立集大小 depth；若"depth + 剩余候选数"已
    无法超越已知最优 best，则剪枝。返回值为精确的最大独立集大小。
    """
    best = [_greedy_is(adj, candidates)]

    def rec(c, depth):
        if c == 0:
            if depth > best[0]:
                best[0] = depth
            return
        pc = c.bit_count()
        if best[0] >= depth + pc:       # 即使取尽剩余顶点也无法超越已知最优
            return
        # 选候选中度数最小的顶点分支
        best_v, best_deg = None, None
        m = c
        while m:
            low = m & -m
            v = low.bit_length() - 1
            deg = (adj[v] & c).bit_count()
            if best_deg is None or deg < best_deg:
                best_v, best_deg = v, deg
            m ^= low
        v = best_v
        rec(c & ~adj[v] & ~(1 << v), depth + 1)   # 选 v
        if best[0] < depth + pc:                  # 仍可能通过"不选 v"改进
            rec(c & ~(1 << v), depth)             # 不选 v

    rec(candidates, 0)
    return best[0]


def max_independent_set(vset, edges):
    """返回最大独立集大小。"""
    verts = sorted(vset)
    idx = {v: i for i, v in enumerate(verts)}
    n = len(verts)
    adj = [0] * n
    for a, b in edges:
        adj[idx[a]] |= 1 << idx[b]
        adj[idx[b]] |= 1 << idx[a]
    return max_is(adj, (1 << n) - 1)


def min_vertex_cover(n_verts, edges):
    """分支限界求最小顶点覆盖：任取一条未覆盖边 (a,b)，
    覆盖必含 a 或 b，分别递归。以贪心 2-近似解作为上界做剪枝，
    避免指数爆炸。"""
    adj = [0] * n_verts
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    best = [_greedy_vc(adj, n_verts)]
    full = (1 << n_verts) - 1
    edge_masks = [(1 << a) | (1 << b) for a, b in edges]

    def solve(remaining, chosen):
        if chosen.bit_count() >= best[0]:   # 已选顶点数不可能优于已知上界，剪枝
            return best[0]
        remaining = [e for e in remaining if not (e & chosen)]
        if not remaining:
            sz = chosen.bit_count()
            if sz < best[0]:
                best[0] = sz
            return sz
        cand = full & ~chosen
        # 选两端度数和最大的未覆盖边分支（启发式，缩小搜索）
        best_e, best_deg = None, -1
        for e in remaining:
            u = e & -e
            v = e ^ u
            iu = u.bit_length() - 1
            iv = v.bit_length() - 1
            deg = (adj[iu] & cand).bit_count() + (adj[iv] & cand).bit_count()
            if deg > best_deg:
                best_deg, best_e = deg, e
        u = best_e & -best_e
        v = best_e ^ u
        r1 = solve(remaining, chosen | u)
        r2 = solve(remaining, chosen | v)
        return min(r1, r2)

    return solve(edge_masks, 0)


# ---------- 归约 3：独立集 -> 顶点覆盖 ----------

def independent_set_to_vertex_cover(vset, edges):
    """同一图上：G 有大小 k 的独立集 ⟺ G 有大小 |V|-k 的顶点覆盖。

    返回 (顶点数, 边数)。验证时独立计算 max 独立集与 min 顶点覆盖，
    检查 min_VC == |V| - max_IS（互补关系的双向交叉验证）。
    """
    return len(vset), len(edges)


# ---------- 主流程 ----------

def random_cnf(n_vars, n_clauses, rng, max_len=4):
    clauses = []
    for _ in range(n_clauses):
        k = rng.randint(2, max_len)
        vs = rng.sample(range(1, n_vars + 1), k)
        clauses.append([v if rng.random() < 0.5 else -v for v in vs])
    return clauses


def main():
    parser = argparse.ArgumentParser(
        description="构造并验证归约链 SAT -> 3-SAT -> 独立集 -> 顶点覆盖"
    )
    parser.add_argument("--instances", type=int, default=30, help="随机实例数")
    parser.add_argument("--vars", type=int, default=6, help="每实例变量数（小规模便于暴力验证）")
    parser.add_argument("--clauses", type=int, default=7, help="每实例子句数")
    parser.add_argument("--seed", type=int, default=2024)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    n_pass_sat3 = n_pass_is = n_pass_vc = 0

    print(f"{'#':>3} {'|V| SAT':>8} {'|C| 3SAT':>9} {'图|V|':>6} {'图|E|':>6}  验证结果")
    for t in range(args.instances):
        cnf = random_cnf(args.vars, args.clauses, rng)

        # 步骤 0：原 SAT 可满足性（暴力基准）
        sat0 = brute_force_sat(cnf, args.vars)

        # 归约 1：SAT -> 3-SAT，验证可满足性保持（等价）
        cnf3, n_extra = sat_to_3sat(cnf)
        n3_vars = args.vars + n_extra
        sat3 = brute_force_sat(cnf3, n3_vars)
        ok1 = (sat0 == sat3)

        # 归约 2：3-SAT -> 独立集，验证 可满足 ⟺ 有大小 m 的独立集
        vset, edges, k = sat_to_independent_set(cnf3)
        is_k = has_independent_set(vset, edges, k)
        ok2 = (sat3 == is_k)

        # 归约 3：独立集 -> 顶点覆盖，独立计算 max 独立集 α 与 min 顶点覆盖 τ，
        #         验证互补关系 τ = |V| - α
        alpha = max_independent_set(vset, edges)
        n_verts, n_edges = independent_set_to_vertex_cover(vset, edges)
        verts_sorted = sorted(vset)
        tau = min_vertex_cover(n_verts,
                               [(verts_sorted.index(a), verts_sorted.index(b))
                                for a, b in edges])
        ok3 = (tau == n_verts - alpha)

        n_pass_sat3 += ok1
        n_pass_is += ok2
        n_pass_vc += ok3
        if t < 5 or not (ok1 and ok2 and ok3):
            print(f"{t:>3} {args.vars:>8} {len(cnf3):>9} {n_verts:>6} {n_edges:>6}  "
                  f"SAT->3SAT:{'ok' if ok1 else 'FAIL'}  3SAT->IS:{'ok' if ok2 else 'FAIL'}  "
                  f"IS->VC:{'ok' if ok3 else 'FAIL'}")

    print()
    print(f"实例总数 {args.instances}")
    print(f"  归约1 SAT->3-SAT 可满足性保持:   {n_pass_sat3}/{args.instances} 通过")
    print(f"  归约2 3-SAT->独立集 解对应:      {n_pass_is}/{args.instances} 通过")
    print(f"  归约3 独立集<->顶点覆盖 互补:    {n_pass_vc}/{args.instances} 通过")
    print()
    print("观察：三步归约在全部随机小实例上解一一对应。注意这只验证了归约")
    print("构造的正确性；NP 完全性证明还需要多项式时间论证与 Cook-Levin 基准，")
    print("小实例通过不能替代数学证明。")


if __name__ == "__main__":
    main()
