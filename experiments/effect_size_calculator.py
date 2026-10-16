#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""效应量与最小样本量计算器（档案 #90 软件工程中的实验方法学）。

验证的已知结果：
  软件工程对照实验中典型效应量很小（Cohen's d 约 0.2–0.5），而组内方差
  大（个体差异、任务复杂度波动），导致常规显著性水平下需要的样本量
  大得离谱——这是软件工程实证研究难以做大的统计学根源：
    n/组 ≈ 2(z_{1-a/2} + z_{1-b})^2 / d^2
  本脚本实现 Cohen's d、Hedges' g、Cliff's delta 三种效应量，并用
  合成的"小效应量、大方差"A/B 数据展示所需最小样本量。

运行方式：
  python experiments/effect_size_calculator.py          # 内置 3 组合成数据
  python experiments/effect_size_calculator.py --help   # 查看参数

它不能说明什么（重要）：
  1. 数据是**合成的**，不来自任何真实实验，数字本身没有经验含义。
  2. 效应量计算与样本量公式基于"正态近似 + 方差齐性"假设；真实
     软件工程数据常有重尾、配对结构，公式只作量级估计。
  3. 样本量计算回答"需要多少人才能检出某效应"，**不**回答"效应
     是否存在"；p 值也不衡量效应的实际重要性。
"""

import argparse
import math
import random


# ---------- 效应量 ----------

def cohens_d(a, b):
    """Cohen's d：(均值差)/合并标准差。"""
    n1, n2 = len(a), len(b)
    m1, m2 = sum(a) / n1, sum(b) / n2
    ss = sum((x - m1) ** 2 for x in a) + sum((x - m2) ** 2 for x in b)
    s_pooled = math.sqrt(ss / (n1 + n2 - 2))
    return (m1 - m2) / s_pooled


def hedges_g(a, b):
    """Hedges' g：Cohen's d 乘小样本校正因子 J。"""
    n1, n2 = len(a), len(b)
    df = n1 + n2 - 2
    d = cohens_d(a, b)
    j = 1.0 - 3.0 / (4.0 * df - 1.0)  # J 的标准近似
    return d * j


def cliffs_delta(a, b):
    """Cliff's delta：P(X>Y) - P(X<Y)，非参数效应量，范围 [-1,1]。"""
    gt = sum(1 for x in a for y in b if x > y)
    lt = sum(1 for x in a for y in b if x < y)
    return (gt - lt) / (len(a) * len(b))


# ---------- p 值（Welch t 检验，用正态近似）----------

def welch_t(a, b):
    """Welch t 统计量与自由度（Welch–Satterthwaite）。"""
    n1, n2 = len(a), len(b)
    m1, m2 = sum(a) / n1, sum(b) / n2
    v1 = sum((x - m1) ** 2 for x in a) / (n1 - 1)
    v2 = sum((x - m2) ** 2 for x in b) / (n2 - 1)
    se = math.sqrt(v1 / n1 + v2 / n2)
    t = (m1 - m2) / se
    df = (v1 / n1 + v2 / n2) ** 2 / ((v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1))
    return t, df


def normal_sf(x):
    """标准正态生存函数 1-Phi(x)（Abramowitz-Stegun 26.2.17 近似）。"""
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def t_p_value(t, df):
    """t 分布 p 值：用 Cornish-Fisher 近似把 t 折算成 z（df 不大时的粗近似）。"""
    # 用 z 近似加自由度修正（对 df>=10 误差可接受，本脚本只作演示）
    c1 = (t ** 3 + t) / (4.0 * df)
    c2 = (5.0 * t ** 5 + 16.0 * t ** 3 + 3.0 * t) / (96.0 * df ** 2)
    z = t + c1 + c2
    return 2.0 * normal_sf(abs(z))


# ---------- 最小样本量 ----------

def min_sample_size(d, alpha=0.05, power=0.8):
    """两独立样本 t 检验每组最小样本量（正态近似）。

    n/组 ≈ 2 (z_{1-a/2} + z_{1-b})^2 / d^2
    """
    z_a = 1.959963984540054  # alpha=0.05 双侧
    # z_{1-b}：power=0.8 -> 0.8416；power=0.9 -> 1.2816
    z_b = {0.8: 0.8416212335729143, 0.9: 1.2815515655446004}.get(
        round(power, 2),
        0.8416212335729143,
    )
    return math.ceil(2.0 * (z_a + z_b) ** 2 / (d * d))


# ---------- 合成数据 ----------

def make_scenarios(seed=42):
    """三组合成 A/B 数据：小效应量、大方差——软件工程实验的典型困境。

    场景 1：静态分析工具 -- 缺陷密度。真实效应往往 d≈0.2。
    场景 2：新编译器优化 -- 运行时间（毫秒）。d≈0.3 但个体方差巨大。
    场景 3：结对编程 -- 任务完成时间。d≈0.5 已属"文献中较大"的效应。
    """
    rng = random.Random(seed)

    def sample(mean, sd, n):
        return [rng.gauss(mean, sd) for _ in range(n)]

    scenarios = [
        {
            "name": "静态分析工具 vs 缺陷密度(kloc)",
            "control": sample(2.30, 0.85, 30),
            "treat": sample(2.13, 0.85, 30),
            "unit": "defects/kLOC",
        },
        {
            "name": "新优化开关 vs 构建耗时(ms)",
            "control": sample(8400, 1500, 30),
            "treat": sample(7950, 1500, 30),
            "unit": "ms",
        },
        {
            "name": "结对编程 vs 任务完成时间(人时)",
            "control": sample(46.0, 9.0, 30),
            "treat": sample(41.5, 9.0, 30),
            "unit": "person-hours",
        },
    ]
    return scenarios


def main():
    parser = argparse.ArgumentParser(
        description="计算 Cohen's d / Hedges' g / Cliff's delta 与最小样本量（合成 A/B 数据）"
    )
    parser.add_argument("--alpha", type=float, default=0.05, help="显著性水平（默认 0.05）")
    parser.add_argument("--power", type=float, default=0.8, help="统计功效（默认 0.8）")
    parser.add_argument("--seed", type=int, default=42, help="随机种子")
    args = parser.parse_args()

    print(f"显著性水平 alpha={args.alpha}，功效 power={args.power}")
    print("=" * 88)
    for sc in make_scenarios(args.seed):
        a, b = sc["control"], sc["treat"]
        d = cohens_d(a, b)
        g = hedges_g(a, b)
        delta = cliffs_delta(a, b)
        t, df = welch_t(a, b)
        p = t_p_value(t, df)
        n_need = min_sample_size(abs(d), args.alpha, args.power)
        print(f"场景：{sc['name']}（单位：{sc['unit']}）")
        print(f"  当前每组 n=30：均值 {sum(a)/len(a):.2f} vs {sum(b)/len(b):.2f}")
        print(f"  Cohen's d = {d:+.3f}   Hedges' g = {g:+.3f}   Cliff's delta = {delta:+.3f}")
        print(f"  Welch t = {t:+.3f} (df≈{df:.0f})，p = {p:.4f}  "
              f"({'显著' if p < args.alpha else '不显著'}，alpha={args.alpha})")
        print(f"  要以 {int(args.power*100)}% 功效检出 |d|={abs(d):.3f} 的效应，"
              f"每组需 n >= {n_need} 人")
        print("-" * 88)

    print("观察：d=0.2（软件工程常见的小效应）需要每组约 394 人；")
    print("而 n=30 的典型实验室研究在 p<0.05 处大多检不出、或只能靠运气检出。")
    print("注意：以上全部基于合成数据，仅展示统计结构，不代表任何真实工具/实践的效应。")


if __name__ == "__main__":
    main()
