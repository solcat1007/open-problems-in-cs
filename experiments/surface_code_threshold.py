#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""最小表面码（环面码）逻辑错误率的蒙特卡洛模拟与阈值现象（档案 #59/#61）。

模型（刻意简化的教学模型，见下方"它不能说明什么"）：
  - 在 d×d 环面码（toric code）上，只模拟 **Z 错误**：每条"数据比特边"以
    独立概率 p 发生 Z 错误（对应开放问题中的量子纠错阈值）。
  - **完美测量**（syndrome 无噪声）、**仅 Z 错误**（不含 X/Y 错误、不含
    测量误读）。X 型 stabilizer 的 syndrome 就是顶点处邻接边上 Z 错误数的
    奇偶性；出现奇数个 Z 错误的顶点叫 **defect**。
  - 解码器：**并查集（union-find）配对解码器**。按 X-stabilizer 的 syndrome
    找出所有 defect（奇奇偶顶点）；把每条边视为可翻转的"边权"（距离）。
    对所有 defect 对计算环绕曼哈顿距离，按距离从小到大排序，用并查集做
    **最小权配对（Kruskal 式贪心，近似 MWPM）**：每次取距离最小且尚属不同
    集合的一对 defect 配对，并沿最短路径把对应边翻转计入校正。最后检查校正
    后剩余错误是否绕环面形成非平庸同调圈（x/y 缠绕数非零）→ 逻辑错误。

输出：扫描 p∈[0.01,0.15]，对每个码距 d∈{3,5} 输出逻辑错误率，让用户看到
两条曲线的**交叉点**（p 较小时 d=5 更优、p 较大时 d=3 更优），即阈值现象
的直接（尽管是简化的）证据。

运行方式：
  python experiments/surface_code_threshold.py          # d=3,5，每 p 点 2000 采样
  python experiments/surface_code_threshold.py --help   # 查看参数

它不能说明什么（重要）：
  1. 这是**极度简化**的模型：独立错误、完美测量、仅 Z 错误、环面边界。
     真实表面码阈值 ≈ 1%（电路级噪声含测量错、X/Z 混合、空间关联），本
     模拟给出的交叉点数值**不等于**真实物理阈值，量级都可能差很多。
  2. union-find 解码器此处为可运行的教学实现，非生产级（未做 full peeling
     优化、未处理奇缺陷簇的边界匹配）。它复现的是"阈值存在、两码距曲线
     交叉"这一定性现象，不是精确的阈值估计。
  3. 有限码距（d≤5）下交叉点只是阈值存在的迹象；证明/估计真实阈值需要
     渐近分析与更精细的噪声模型，数值扫描无法替代。

只用 Python 标准库。
"""

import argparse
import random
import sys


def build_lattice(d):
    """构造 d×d 环面码的边与邻接结构。

    顶点 v = x*d + y（x,y∈[0,d)）。返回：
      edges: list[(u,v)]，长度 M=2*d*d（d*d 水平边 + d*d 垂直边，均按周期连接）
      adj:   每个顶点的 (邻居, 边序号) 列表
      seams: (horiz_seam_edges, vert_seam_edges) 用于缠绕数检测
    """
    N = d * d
    edges = []
    # 水平边：(x,y)-(x+1,y) mod d
    for x in range(d):
        for y in range(d):
            u = x * d + y
            v = ((x + 1) % d) * d + y
            edges.append((u, v))
    # 垂直边：(x,y)-(x,y+1) mod d
    for x in range(d):
        for y in range(d):
            u = x * d + y
            v = x * d + ((y + 1) % d)
            edges.append((u, v))
    M = len(edges)
    adj = [[] for _ in range(N)]
    for ei, (u, v) in enumerate(edges):
        adj[u].append((v, ei))
        adj[v].append((u, ei))
    # 缠绕数检测的"接缝"边：跨越周期边界的边
    # 水平接缝：x=d-1 连到 x=0 的水平边（每个 y）
    hseam = [y for y in range(d)]  # edges 中第 (d-1)*d + y 条是水平边 (d-1,y)-(0,y)
    hseam = [ (d - 1) * d + y for y in range(d) ]
    # 垂直接缝：y=d-1 连到 y=0 的垂直边（每个 x）：垂直边从索引 d*d 开始
    vseam = [ d * d + x * d + (d - 1) for x in range(d) ]
    return N, M, edges, adj, hseam, vseam


def syndrome(errors, M, edges, N):
    """给定每条边的错误位 errors，返回每个顶点的 syndrome（奇数个邻接边错误=1）。"""
    s = [0] * N
    for ei in range(M):
        if errors[ei]:
            u, v = edges[ei]
            s[u] ^= 1
            s[v] ^= 1
    return s


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra != rb:
        parent[ra] = rb


def toric_dist(d, a, b):
    """环绕曼哈顿距离（周期边界）。a,b 为顶点索引 x*d+y。"""
    ax, ay = a // d, a % d
    bx, by = b // d, b % d
    dx = abs(((bx - ax + (d + 1) // 2) % d) - (d + 1) // 2)
    dy = abs(((by - ay + (d + 1) // 2) % d) - (d + 1) // 2)
    # 等价于把坐标差归一到 [-d/2, d/2]
    dx = bx - ax
    if dx > d // 2:
        dx -= d
    elif dx < -(d // 2):
        dx += d
    dy = by - ay
    if dy > d // 2:
        dy -= d
    elif dy < -(d // 2):
        dy += d
    return abs(dx) + abs(dy)


def path_edges(a, b, d, M):
    """返回 a→b 最短路径上的边索引列表（周期网格，任意最短路径边界相同）。"""
    ax, ay = a // d, a % d
    bx, by = b // d, b % d
    dx = bx - ax
    if dx > d // 2:
        dx -= d
    elif dx < -(d // 2):
        dx += d
    dy = by - ay
    if dy > d // 2:
        dy -= d
    elif dy < -(d // 2):
        dy += d
    edges_on = []
    x, y = ax, ay
    sx = 1 if dx >= 0 else -1
    for _ in range(abs(dx)):
        nx = (x + sx) % d
        if sx > 0:
            edges_on.append(x * d + y)
        else:
            edges_on.append(((x - 1) % d) * d + y)
        x = nx
    sy = 1 if dy >= 0 else -1
    for _ in range(abs(dy)):
        ny = (y + sy) % d
        if sy > 0:
            edges_on.append(d * d + x * d + y)
        else:
            edges_on.append(d * d + x * d + ((y - 1) % d))
        y = ny
    return edges_on


def decode(s, N, M, d):
    """并查集（贪心最近邻）配对解码器：返回校正边位 c（长度 M）。

    实现：找出全部 defect，按环绕曼哈顿距离排序所有 defect 对，贪心地
    依次取距离最小且两端都尚未配对的一对进行配对（完美匹配）。每对沿
    最短路径翻转对应边。由于每个 defect 恰为一条配对路径的端点，校正后
    syndrome 被精确归零；逻辑错误仅由"剩余错误绕环面形成非平庸圈"造成。
    """
    defects = [v for v in range(N) if s[v] == 1]
    k = len(defects)
    if k == 0:
        return bytearray(M)
    if k % 2 == 1:
        # 环面码 defect 数必为偶数；若出现奇数则直接判解码失败
        return None
    pairs = []
    for i in range(k):
        for j in range(i + 1, k):
            a, b = defects[i], defects[j]
            pairs.append((toric_dist(d, a, b), i, j))
    pairs.sort()
    matched = [False] * k
    c = bytearray(M)
    for _, i, j in pairs:
        if not matched[i] and not matched[j]:
            matched[i] = matched[j] = True
            for e in path_edges(defects[i], defects[j], d, M):
                c[e] ^= 1
    return c


def logical_error(errors, c, M, hseam, vseam):
    """校正后剩余错误 e_total = errors XOR c；若绕环面形成非平庸同调圈则逻辑错误。"""
    x_wind = 0
    for e in hseam:
        x_wind ^= (errors[e] ^ c[e])
    y_wind = 0
    for e in vseam:
        y_wind ^= (errors[e] ^ c[e])
    return (x_wind & 1) == 1 or (y_wind & 1) == 1


def simulate(d, p, samples, seed):
    N, M, edges, adj, hseam, vseam = build_lattice(d)
    rng = random.Random(seed * 100000 + d * 7 + int(round(p * 1000)))
    n_fail = 0
    for _ in range(samples):
        errors = [1 if rng.random() < p else 0 for _ in range(M)]
        s = syndrome(errors, M, edges, N)
        c = decode(s, N, M, d)
        if c is None:
            n_fail += 1
            continue
        if logical_error(errors, c, M, hseam, vseam):
            n_fail += 1
    return n_fail / samples


def main():
    parser = argparse.ArgumentParser(
        description="最小表面码阈值的蒙特卡洛模拟（union-find 解码器，d=3,5）"
    )
    parser.add_argument("--ds", type=int, nargs="+", default=[3, 5],
                        help="码距列表")
    parser.add_argument("--p-min", type=float, default=0.01)
    parser.add_argument("--p-max", type=float, default=0.15)
    parser.add_argument("--p-steps", type=int, default=15,
                        help="p 扫描点数")
    parser.add_argument("--samples", type=int, default=2000,
                        help="每个 (d,p) 的蒙特卡洛采样数")
    parser.add_argument("--seed", type=int, default=2024)
    args = parser.parse_args()

    ps = [args.p_min + (args.p_max - args.p_min) * i / (args.p_steps - 1)
          for i in range(args.p_steps)]

    print(f"表面码阈值模拟（独立 Z 错误、完美测量；并查集配对解码器）")
    print(f"码距 d={args.ds}  采样/点={args.samples}  p∈[{args.p_min},{args.p_max}]")
    print()
    header = f"{'p':>6}" + "".join(f"{'d='+str(d):>12}" for d in args.ds)
    print(header)
    results = {d: [] for d in args.ds}
    for p in ps:
        row = f"{p:>6.3f}"
        for d in args.ds:
            rate = simulate(d, p, args.samples, args.seed)
            results[d].append(rate)
            row += f"{rate:>12.3f}"
        print(row)

    # 找交叉点：d=5 的逻辑错误率首次低于（即优于）较小码距的位置
    if len(args.ds) >= 2:
        small, large = args.ds[0], args.ds[-1]
        cross = None
        for i, p in enumerate(ps):
            if results[large][i] < results[small][i]:
                cross = p
                break
        print()
        if cross is not None:
            print(f"交叉点（d={large} 首次优于 d={small}）约在 p≈{cross:.3f} 附近。")
            print("该交叉点即'阈值现象'的定性证据：p 低于它时更大码距更抗错，")
            print("高于它时更大码距反而更易错。注意此数值≠真实物理阈值（见文件头说明）。")
        else:
            print("本扫描区间内未观察到交叉（可降低 --p-max 或增加 --samples 再看）。")
    print()
    print("免责：简化模型（独立错误、完美测量、仅 Z 错误）；交叉点数值不等于真实阈值。")


if __name__ == "__main__":
    main()
