#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Splay 树 vs 静态最优 BST 的实测代价对比（档案 #26 Splay 树动态最优性）。

复现的已知行为（不是要证明什么）：
  Sleator & Tarjan (1985) 证明了 splay 的 **静态最优性（static optimality）**：
  对任意访问序列，splay 的总代价 ≤ O(静态最优 BST 的代价)。也就是说，
  静态最优代价是 splay 的一个**常数因子上界**——splay 不会被甩开，但也
  完全可能**低于**静态最优（自适应搬根利用了局部性，而静态树是固定不变
  的）。本脚本在四种访问序列上实测该比值：
    随机 (uniform) / 顺序 (1..n 扫描) / 循环 (步长互质的长周期) / Zipf 偏斜
  预期：局部性强（顺序/循环）时 splay 逼近甚至略低于静态最优；纯随机时比值
  略高于 1，但都被常数因子 bound，不会随 n 爆炸。

运行方式：
  python experiments/splay_tree.py          # 默认 n=64, 序列长 4000
  python experiments/splay_tree.py --help   # 查看参数

它不能说明什么（重要）：
  1. 本脚本**只复现了"静态最优性"这一已证下界对应的已知自适应行为**，
     并展示 splay 的代价比值有限。它**绝不**能验证"动态最优性猜想"——
     即 splay 的代价是否被某个常数因子 bound 在"离线最优动态 BST"之内。
     动态最优性至今是开放问题，需要理论证明，数值实验在原理上无法触及。
  2. 比值 >= 1 是由静态最优性定理保证的，不是本模拟的"发现"。
  3. 有限规模（n<=64）的实测不能推出渐近结论。

只用 Python 标准库。
"""

import argparse
import random


# ---------- Splay 树（带父指针，支持 zig / zig-zig / zig-zag） ----------

class _Node:
    __slots__ = ("key", "left", "right", "parent")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self):
        self.root = None

    def _rotate(self, x):
        """单旋：把 x 提升为父节点 p 的父。用于 zig（p 为根）或
        zig-zig / zig-zag 的每一步。"""
        p = x.parent
        g = p.parent
        if p.left is x:
            p.left = x.right
            if x.right is not None:
                x.right.parent = p
            x.right = p
        else:
            p.right = x.left
            if x.left is not None:
                x.left.parent = p
            x.left = p
        p.parent = x
        x.parent = g
        if g is None:
            self.root = x
        elif g.left is p:
            g.left = x
        else:
            g.right = x

    def _splay(self, x):
        """将节点 x 旋转到根：三种情形。"""
        while x.parent is not None:
            p = x.parent
            g = p.parent
            if g is None:
                # zig（单旋）：x 的父就是根
                self._rotate(x)
            elif (p.left is x) == (g.left is p):
                # zig-zig：x 与父同侧，先旋父再旋 x
                self._rotate(p)
                self._rotate(x)
            else:
                # zig-zag：x 与父异侧，连旋两次 x
                self._rotate(x)
                self._rotate(x)

    def _find_depth(self, key):
        """返回 (节点, 访问前的深度+1)。访问代价即路径上的节点数。"""
        x = self.root
        depth = 0
        while x is not None:
            depth += 1
            if key == x.key:
                return x, depth
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None, depth

    def access(self, key):
        """访问 key：返回访问前路径节点数（代价），并把该节点 splay 到根。"""
        node, cost = self._find_depth(key)
        if node is not None:
            self._splay(node)
        return cost

    def insert(self, key):
        if self.root is None:
            self.root = _Node(key)
            return
        x = self.root
        while True:
            if key < x.key:
                if x.left is None:
                    x.left = _Node(key)
                    x.left.parent = x
                    self._splay(x.left)
                    return
                x = x.left
            else:
                if x.right is None:
                    x.right = _Node(key)
                    x.right.parent = x
                    self._splay(x.right)
                    return
                x = x.right


# ---------- 静态最优 BST（DP，Knuth/标准 OPT） ----------

def static_optimal_cost(freqs):
    """给定有序键的频率 freqs[0..n-1]，返回静态最优 BST 的加权路径长度
    = sum_i freqs[i] * (depth_i + 1)。O(n^3)（n 很小，足够）。"""
    n = len(freqs)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + freqs[i]
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = pref[j + 1] - pref[i]
            if i == j:
                dp[i][j] = total
                continue
            best = None
            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                cand = left + right
                if best is None or cand < best:
                    best = cand
            dp[i][j] = best + total
    return dp[0][n - 1]


# ---------- 访问序列生成 ----------

def make_sequence(kind, n, length, rng):
    if kind == "random":
        return [rng.randrange(1, n + 1) for _ in range(length)]
    if kind == "sequential":
        return [(i % n) + 1 for i in range(length)]
    if kind == "cyclic":
        # 步长 k 与 n 互质 -> 单条长周期，整体仍均匀但带强局部性
        k = 5
        while __import__("math").gcd(k, n) != 1:
            k += 2
        seq = []
        pos = 0
        for _ in range(length):
            pos = (pos + k) % n
            seq.append(pos + 1)
        return seq
    if kind == "zipf":
        # Zipf: P(key i) ∝ 1/(i+1)^alpha，偏斜分布
        alpha = 1.0
        weights = [(1.0 / (i + 1) ** alpha) for i in range(n)]
        total = sum(weights)
        cum = []
        acc = 0.0
        for w in weights:
            acc += w / total
            cum.append(acc)
        seq = []
        for _ in range(length):
            r = rng.random()
            # 二分查找
            lo, hi = 0, n - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if cum[mid] < r:
                    lo = mid + 1
                else:
                    hi = mid
            seq.append(lo + 1)
        return seq
    raise ValueError(kind)


def main():
    parser = argparse.ArgumentParser(
        description="Splay 树 vs 静态最优 BST：多种访问序列下的代价比值"
    )
    parser.add_argument("--n", type=int, default=64, help="键空间大小 1..n")
    parser.add_argument("--length", type=int, default=4000, help="访问序列长度")
    parser.add_argument("--seed", type=int, default=12345)
    parser.add_argument(
        "--kinds", nargs="+",
        default=["random", "sequential", "cyclic", "zipf"],
        help="访问序列类型",
    )
    args = parser.parse_args()

    rng = random.Random(args.seed)
    print(f"键空间 n={args.n}，序列长度 L={args.length}")
    print(f"{'序列类型':<12}{'splay总代价':>14}{'静态最优代价':>14}{'比值':>10}")
    print("-" * 50)

    for kind in args.kinds:
        seq = make_sequence(kind, args.n, args.length, rng)
        tree = SplayTree()
        for k in range(1, args.n + 1):
            tree.insert(k)
        splay_cost = sum(tree.access(k) for k in seq)

        freqs = [0] * args.n
        for k in seq:
            freqs[k - 1] += 1
        static_cost = static_optimal_cost(freqs)

        ratio = splay_cost / static_cost if static_cost else float("inf")
        print(f"{kind:<12}{splay_cost:>14}{static_cost:>14}{ratio:>10.2f}")

    print()
    print("观察：")
    print("  1. 静态最优性定理给出的是上界：splay 代价 ≤ O(静态最优代价)，因此比值")
    print("     被常数因子 bound（不会随 n 发散）；splay 作为自适应结构，代价也可")
    print("     能低于静态最优（比值 < 1，如顺序访问时 splay 把刚访问节点搬根）。")
    print("  2. 局部性强的序列（sequential / cyclic）比值接近或低于 1；纯随机/Zipf 略高，")
    print("     但都保持有限——这是 splay 利用局部性的已知自适应行为。")
    print("  3. 本脚本只复现了已知行为；真正的开放问题是**动态最优性猜想**：splay 是否")
    print("     被某个常数因子 bound 在'离线最优动态 BST'之内。数值实验无法证明它。")


if __name__ == "__main__":
    main()
