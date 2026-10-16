#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grover 振幅放大的经典数值模拟（档案 #37 Grover 精确下界）。

验证的已知结果：
  Grover 算法在 N 维状态空间上迭代算符 G = D·O（O 为 oracle 相位翻转，
  D 为 diffusion 算子）后，目标态的成功概率按 sin((2k+1)θ) 振荡，
  其中 sinθ = 1/√N。峰值出现在 k* = ⌊π√N/4⌋ 附近；迭代超过最优值后
  成功概率反而下降（"过旋转"）。

运行方式：
  python experiments/grover_amplitude_amplification.py          # 默认 N=8,16,32,64,128
  python experiments/grover_amplitude_amplification.py --help  # 查看参数

它不能说明什么（重要）：
  1. 这是对**已知上界**（Grover 算法行为）的数值复现，不是对
     Omega(√N) 查询下界的证明。下界是关于所有量子算法的数学命题，
     小规模数值模拟在原理上无法触及。
  2. 有限的 N 无法推出渐近结论；实测峰值位置与理论值的偏差
     在 N 增大时缩小，但这只是数值证据，不是证明。

只用 Python 标准库（复数运算用内置 complex）。
"""

import argparse
import cmath


def grover_simulation(n_qubits: int):
    """在 N=2^n 维状态向量上模拟 Grover 迭代，返回每轮成功概率列表。

    纯向量模拟：状态是长度 N 的复数列表，初始均匀叠加。
    Oracle O：目标位 |w> 振幅取负（相位翻转）。
    Diffusion D：D = 2|s><s| - I，作用在均匀叠加 |s> 上。
    """
    n = 1 << n_qubits
    target = n - 1  # 标记最后一个基态为目标
    # 初始均匀叠加态
    amp = 1.0 / cmath.sqrt(n)
    state = [amp] * n

    probs = [abs(state[target]) ** 2]
    max_iter = 2 * int((3.141592653589793 / 4) * (n ** 0.5)) + 4  # 覆盖过冲区间
    for _ in range(max_iter):
        # Oracle：目标振幅乘 -1
        state[target] = -state[target]
        # Diffusion：D = 2|s><s| - I，即 mean = 2*avg，然后 x -> mean - x
        total = sum(state)
        mean = 2.0 * total / n
        state = [mean - a for a in state]
        probs.append(abs(state[target]) ** 2)
    return probs


def main():
    parser = argparse.ArgumentParser(
        description="纯 Python 模拟 Grover 振幅放大，验证峰值位置与过旋转现象"
    )
    parser.add_argument(
        "--qubits", type=int, nargs="+", default=[3, 4, 5, 6, 7],
        help="比特数列表，N=2^n（默认 3 4 5 6 7，即 N=8..128）"
    )
    args = parser.parse_args()

    print(f"{'N':>5} {'理论最优k=round(pi*sqrt(N)/4)':>28} "
          f"{'实测峰值k':>10} {'峰值概率':>10} {'理论峰值sin^2((2k+1)theta)':>26} {'峰值后概率':>10}")
    for n_qubits in args.qubits:
        n = 1 << n_qubits
        theta = cmath.asin(1.0 / (n ** 0.5))
        k_theory = int((3.141592653589793 / 4) * (n ** 0.5))  # floor(pi*sqrt(N)/4)
        probs = grover_simulation(n_qubits)
        # "最优迭代数"取首个达到 (1 - 1/N) 成功概率的 k：连续迭代会周期性振荡，
        # 后续轮次可能偶然更高，但 Grover 的标准停止点就是第一个接近 1 的峰
        thresh = 1.0 - 1.0 / n
        k_best = next(k for k, p in enumerate(probs) if p >= thresh)
        p_peak = probs[k_best]
        p_theory = cmath.sin((2 * k_best + 1) * theta) ** 2
        # 过冲演示：峰值之后再迭代一次的概率
        k_over = min(k_best + 1, len(probs) - 1)
        p_over = probs[k_over]
        print(f"{n:>5} {k_theory:>28} {k_best:>10} {p_peak:>10.4f} "
              f"{p_theory.real:>26.4f} {p_over:>10.4f}")

    print()
    print("观察：")
    print("1. 首个接近 1 的峰值出现在 k* = floor(pi*sqrt(N)/4) 附近，峰值概率约 1 - 1/N。")
    print("2. 峰值后再迭代一次，成功概率明显下降 —— 过旋转（迭代越多不是越好；")
    print("   连续迭代会周期性振荡，后续偶有更高值，但标准停止点是第一个峰）。")
    print("3. 峰值迭代数随 sqrt(N) 增长 —— 平方加速的数值体现。")
    print("注意：这复现的是已知算法行为，不构成对 Omega(sqrt(N)) 下界的任何证明。")


if __name__ == "__main__":
    main()
