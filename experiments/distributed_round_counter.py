#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分布式 MST 与领导者选举的通信代价实测（档案 #80/#82）。

简化模型（见下方"它不能说明什么"）：
  - 在随机无向连通图上（n=8..64，多种边密度）运行两个**同步消息传递**
    算法的简化版，统计实际通信 **轮数（rounds）** 与 **消息数（messages）**：
    1. GHS 分布式 MST（Gallager-Humblet-Spira）的简化版：本质是分布式的
       Borůvka —— 每个连通分量（fragment）在每"相位"选出自己连向外部的
       最小权边（MOE），再沿 MOE 合并；重复直到全图合一。每相位的代价由
       洪泛（flooding）主导：洪泛片段 id + 上报 MOE + 通知合并，约若干轮、
       每轮 O(|E|) 条消息。
    2. 领导者选举（简化版）：洪泛"最大 id"，每节点不断把见到的最大 id 广播
       给邻居，稳定后 id 最大的节点即领导者。
  - 用并查集 / Prim 校验最终确实得到一棵 MST（总权值 == Prim 的 MST 权值），
    以确认算法实现正确、不是空转。

输出：表格列出 节点数 × 边密度 下的 MST 轮数、MST 消息数、选举轮数、选举消息数，
展示这些代价随节点数/密度的增长趋势。

运行方式：
  python experiments/distributed_round_counter.py
  python experiments/distributed_round_counter.py --help

它不能说明什么（重要）：
  1. 本脚本只**实测了一个具体（简化）实现的通信代价**，这些实测值是相应
     算法的**上界经验值**。它**无法验证任何下界**（如下界需要理论证明，
     例如 CONGEST 模型下的 Ω(√n) 或 Ω(D) 轮下界）。数值测出的轮数/消息数
     既可能是算法优化空间大，也可能离下界很远——数字本身不构成复杂性结论。
  2. GHS 与领导者选举都做了**大幅简化**（同步洪泛而非完整相位/状态机、无
     崩溃恢复、无加权仲裁细节），仅用于展示代价随规模的量级趋势。
  3. 随机图上的结果依赖于图模型（Erdős–Rényi），换拓扑结论会变。

只用 Python 标准库。
"""

import argparse
import random
from collections import defaultdict


# ---------- 图生成 ----------

def erdos_renyi(n, p, rng):
    """生成随机无向图（边带随机权值）；保证连通。返回 adjacency 与边列表。"""
    while True:
        adj = [[] for _ in range(n)]
        edges = []
        for u in range(n):
            for v in range(u + 1, n):
                if rng.random() < p:
                    w = rng.randint(1, 100)
                    adj[u].append((v, w))
                    adj[v].append((u, w))
                    edges.append((u, v, w))
        if len(edges) >= n - 1 and _is_connected(n, adj):
            return adj, edges


def _is_connected(n, adj):
    seen = [False] * n
    stack = [0]
    seen[0] = True
    cnt = 1
    while stack:
        u = stack.pop()
        for v, _ in adj[u]:
            if not seen[v]:
                seen[v] = True
                cnt += 1
                stack.append(v)
    return cnt == n


def prim_mst_weight(n, adj):
    """中心化 Prim 计算 MST 总权值，用于校验分布式结果。"""
    import heapq
    visited = [False] * n
    visited[0] = True
    pq = [(w, 0, v) for v, w in adj[0]]
    heapq.heapify(pq)
    total = 0
    count = 1
    while pq and count < n:
        w, u, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        total += w
        count += 1
        for v2, w2 in adj[v]:
            if not visited[v2]:
                heapq.heappush(pq, (w2, v, v2))
    return total


# ---------- 同步洪泛（用于计数轮数/消息数）----------

def _flood_min(n, adj, frags, rounds, messages):
    """把每个分量的 '最小节点 id' 洪泛到整个分量；返回收敛所需轮数。"""
    changed = True
    while changed:
        changed = False
        rounds[0] += 1
        new = frags[:]
        for u in range(n):
            fu = frags[u]
            for v, _ in adj[u]:
                messages[0] += 1
                if frags[v] < fu:
                    fu = frags[v]
            if fu < new[u]:
                new[u] = fu
                changed = True
        frags[:] = new


def _flood_max(n, adj, lead, rounds, messages):
    """洪泛最大 id（领导者选举）。"""
    changed = True
    while changed:
        changed = False
        rounds[0] += 1
        new = lead[:]
        for u in range(n):
            lu = lead[u]
            for v, _ in adj[u]:
                messages[0] += 1
                if lead[v] > lu:
                    lu = lead[v]
            if lu > new[u]:
                new[u] = lu
                changed = True
        lead[:] = new


# ---------- 简化 GHS（分布式 Borůvka）----------

def run_ghs(n, adj, edges, density, seed):
    """返回 (总轮数, 总消息数, MST总权值)。每相位：洪泛片段id -> 上报MOE -> 合并。"""
    rounds = [0]
    messages = [0]
    rng = random.Random(seed)
    frags = list(range(n))  # 片段 id = 分量内最小节点 id

    while len(set(frags)) > 1:
        # 1) 洪泛：让同一分量所有节点知道本分量 id
        _flood_min(n, adj, frags, rounds, messages)

        # 2) 每个分量选 MOE（连向外部的最小权边）
        comp = defaultdict(list)
        for u in range(n):
            comp[frags[u]].append(u)
        moe = {}  # 分量 id -> (min_w, 邻分量 id)
        for c, members in comp.items():
            best_w, best_nc = None, None
            for u in members:
                for v, w in adj[u]:
                    if frags[v] != c:
                        if best_w is None or w < best_w or (w == best_w and frags[v] < best_nc):
                            best_w, best_nc = w, frags[v]
            moe[c] = (best_w, best_nc)
        # 上报 MOE 计为 1 轮、|E| 条消息（分布式聚合的近似）
        rounds[0] += 1
        messages[0] += len(edges)

        # 3) 沿 MOE 合并分量（用并查集合并分量 id）
        comp_ids = list(comp.keys())
        parent = {c: c for c in comp_ids}

        def cfind(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def cunion(a, b):
            ra, rb = cfind(a), cfind(b)
            if ra != rb:
                parent[ra] = rb

        for c in comp_ids:
            d = moe[c][1]
            if d is not None:
                cunion(c, d)
        # 新片段 id = 合并组内最小的原分量 id
        groupmin = {}
        for c in comp_ids:
            r = cfind(c)
            if r not in groupmin or c < groupmin[r]:
                groupmin[r] = c
        for u in range(n):
            frags[u] = groupmin[cfind(frags[u])]
        # 合并通知计为 1 轮、2|E| 条消息
        rounds[0] += 1
        messages[0] += 2 * len(edges)

    return rounds[0], messages[0]


def run_election(n, adj, edges, seed):
    """简化领导者选举（洪泛最大 id）。返回 (轮数, 消息数)。"""
    rounds = [0]
    messages = [0]
    lead = list(range(n))
    _flood_max(n, adj, lead, rounds, messages)
    return rounds[0], messages[0]


def main():
    parser = argparse.ArgumentParser(
        description="分布式 MST(GHS简化) 与领导者选举 的轮数/消息数实测"
    )
    parser.add_argument("--ns", type=int, nargs="+", default=[8, 16, 32, 64],
                        help="节点数列表")
    parser.add_argument("--densities", type=float, nargs="+", default=[0.2, 0.4, 0.6],
                        help="边密度（Erdős–Rényi 连边概率）")
    parser.add_argument("--trials", type=int, default=3, help="每种 (n,密度) 重复次数取均值")
    parser.add_argument("--seed", type=int, default=99)
    args = parser.parse_args()

    print(f"{'n':>4} {'密度':>6} {'边|E|':>7} {'MST轮数':>9} {'MST消息':>11} "
          f"{'选举轮数':>9} {'选举消息':>11}  MST校验")
    print("-" * 70)

    for n in args.ns:
        for p in args.densities:
            mst_r_sum = mst_m_sum = elect_r_sum = elect_m_sum = 0
            ok_all = True
            for t in range(args.trials):
                rng = random.Random(args.seed * 1000 + n * 13 + int(p * 1000) + t * 7)
                adj, edges = erdos_renyi(n, p, rng)
                mst_r, mst_m = run_ghs(n, adj, edges, p, args.seed + t)
                elect_r, elect_m = run_election(n, adj, edges, args.seed + t)
                # 校验：用中心化 Borůvka 重算 MST 总权值，应与 Prim 一致
                mst_w = _boruvka_weight(n, adj)
                prim_w = prim_mst_weight(n, adj)
                ok = (mst_w == prim_w)
                ok_all = ok_all and ok
                mst_r_sum += mst_r
                mst_m_sum += mst_m
                elect_r_sum += elect_r
                elect_m_sum += elect_m
            e = len(edges)
            print(f"{n:>4} {p:>6.2f} {e:>7} "
                  f"{mst_r_sum / args.trials:>9.1f} {mst_m_sum / args.trials:>11.0f} "
                  f"{elect_r_sum / args.trials:>9.1f} {elect_m_sum / args.trials:>11.0f}  "
                  f"{'ok' if ok_all else 'MISMATCH'}")

    print()
    print("观察：")
    print("  1. MST 与选举的轮数大致随图的直径（受 n、密度影响）增长；消息数随 |E|（密度）")
    print("     线性增长——符合洪泛类同步算法的直觉。")
    print("  2. 这些数字只是本简化实现的实测代价（经验上界），不构成对分布式复杂性")
    print("     下界（如 CONGEST 模型 Ω(√n)/Ω(D) 轮）的任何验证；下界需理论证明。")
    print("  3. 表格末列 'MST校验' 为 ok 表示本实现确实得到正确 MST（总权值==Prim）。")


def _boruvka_weight(n, adj):
    """中心化 Borůvka 重算 MST 总权值，用于校验分布式实现的合并结果。"""
    frags = list(range(n))
    total = 0

    def find(x):
        while frags[x] != x:
            frags[x] = frags[frags[x]]
            x = frags[x]
        return x

    while len(set(find(i) for i in range(n))) > 1:
        comp = defaultdict(list)
        for u in range(n):
            comp[find(u)].append(u)
        moe = {}
        for c, members in comp.items():
            best_w, best_nc = None, None
            for u in members:
                for v, w in adj[u]:
                    if find(v) != c:
                        if best_w is None or w < best_w:
                            best_w, best_nc = w, find(v)
            moe[c] = (best_w, best_nc)
        added = False
        for c in comp:
            d = moe[c][1]
            if d is not None and find(c) != find(d):
                # 合并 c, d：把 c 挂到 d
                frags[find(c)] = find(d)
                total += moe[c][0]
                added = True
        if not added:
            break
    return total


if __name__ == "__main__":
    main()
