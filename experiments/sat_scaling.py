#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""随机 3-SAT 上 DPLL 求解器的指数增长实测（档案 #1 P vs NP）。

验证的已知结果：
  纯 Python DPLL（含单元传播、纯字面量消除）在随机 3-SAT 上，求解时间
  随变量数 n 大致呈指数增长，且在子句/变量比 alpha ≈ 4.26 的相变点附近
  最难（中位求解时间出现峰值）。

运行方式：
  python experiments/sat_scaling.py          # 默认 n=10..26 步长 4
  python experiments/sat_scaling.py --help   # 查看参数

它不能说明什么（重要）：
  1. 只测试了**一个算法**（本手写 DPLL）在**一种实例分布**（均匀随机
     3-SAT）上的表现。换算法（CDCL）、换分布，曲线完全不同。
  2. 它测的是有限规模（n<=26）。任何有限的实测数据在原理上都无法
     推出渐近结论，更不能证明或否证 P vs NP。
  3. 恰恰相反——有人正是用"我们的求解器在这些实例上很快"来论证
     SAT 不难，这是同一类错误的另一面。经验性能与复杂性下界是两回事。

实现说明：单实例超过 2 秒（可用 --timeout 调整）即放弃该实例，
保证脚本总能在 30 秒量级内跑完。
"""

import argparse
import random
import time


# ---------- DPLL 求解器 ----------

def dpll(clauses, deadline):
    """DPLL 求解。clauses: list[list[int]]（正负整数变量）。

    含单元传播与纯字面量消除。返回 (可满足?, 最大递归深度)。
    超过 deadline 则抛出 TimeoutError。
    """
    depth = [0]
    max_depth = [0]

    def solve(clauses, level):
        if time.monotonic() > deadline:
            raise TimeoutError
        max_depth[0] = max(max_depth[0], level)
        # 空子句集：全部满足；含空子句：冲突
        if not clauses:
            return True
        if any(len(c) == 0 for c in clauses):
            return False

        # 单元传播
        while True:
            unit = None
            for c in clauses:
                if len(c) == 1:
                    unit = c[0]
                    break
            if unit is None:
                break
            clauses = assign(clauses, unit)
            if any(len(c) == 0 for c in clauses):
                return False  # 传播中产生冲突
            if not clauses:
                return True

        # 纯字面量消除
        lits = set()
        for c in clauses:
            lits.update(c)
        pures = [l for l in lits if -l not in lits]
        if pures:
            for p in pures:
                clauses = assign(clauses, p)
            return solve(clauses, level + 1)

        # 分支：选出现次数最多的文字
        counts = {}
        for c in clauses:
            for l in c:
                counts[l] = counts.get(l, 0) + 1
        branch = max(counts, key=counts.get)
        return (solve(assign(clauses, branch), level + 1)
                or solve(assign(clauses, -branch), level + 1))

    return solve(clauses, 0), max_depth[0]


def assign(clauses, lit):
    """在子句集中令 lit 为真：删去含 lit 的子句，从其余子句中删去 -lit。"""
    out = []
    for c in clauses:
        if lit in c:
            continue
        if -lit in c:
            c = [l for l in c if l != -lit]
        out.append(c)
    return out


# ---------- 随机 3-SAT 生成 ----------

def random_3sat(n, alpha, rng):
    """生成 n 变量、m=alpha*n 条随机 3 子句（每子句 3 个互异变量）。"""
    m = int(round(alpha * n))
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(1, n + 1), 3)
        clauses.append([v if rng.random() < 0.5 else -v for v in vs])
    return clauses


def main():
    parser = argparse.ArgumentParser(
        description="随机 3-SAT 上 DPLL 的运行时间实测（相变点 alpha≈4.26 附近最难）"
    )
    parser.add_argument("--n-min", type=int, default=10)
    parser.add_argument("--n-max", type=int, default=26)
    parser.add_argument("--n-step", type=int, default=4)
    parser.add_argument("--alphas", type=float, nargs="+",
                        default=[3.0, 4.26, 5.0],
                        help="子句/变量比（默认含相变点 4.26）")
    parser.add_argument("--trials", type=int, default=8, help="每档实例数")
    parser.add_argument("--timeout", type=float, default=2.0,
                        help="单实例超时秒数（超时跳过）")
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()

    print(f"n    alpha   实例数  超时数  平均时间(ms)   平均递归深度")
    for n in range(args.n_min, args.n_max + 1, args.n_step):
        for alpha in args.alphas:
            rng = random.Random(args.seed * 1000 + n * 10 + int(alpha * 100))
            times, depths, n_timeout = [], [], 0
            for _ in range(args.trials):
                clauses = random_3sat(n, alpha, rng)
                deadline = time.monotonic() + args.timeout
                t0 = time.monotonic()
                try:
                    sat, depth = dpll([c[:] for c in clauses], deadline)
                except TimeoutError:
                    n_timeout += 1
                    continue
                times.append(time.monotonic() - t0)
                depths.append(depth)
            if times:
                avg_t = 1000.0 * sum(times) / len(times)
                avg_d = sum(depths) / len(depths)
                print(f"{n:<4} {alpha:<7.2f} {args.trials:<6} {n_timeout:<6} "
                      f"{avg_t:<12.2f} {avg_d:.1f}")
            else:
                print(f"{n:<4} {alpha:<7.2f} {args.trials:<6} {n_timeout:<6} "
                      f"{'全部超时':<12} -")

    print()
    print("观察：同一 alpha 下，平均时间随 n 近似指数增长；alpha=4.26（相变点）")
    print("附近的实例最难、递归深度最大。但这只是单一算法在单一分布上的有限")
    print("规模实测，不能推出任何渐近结论，更与 P vs NP 的证明无关。")


if __name__ == "__main__":
    main()
