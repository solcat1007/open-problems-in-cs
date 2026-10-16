#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ECE（期望校准误差）与语义熵的构造性演示（档案 #45 LLM 幻觉）。

验证的已知结果：
  1. ECE 分箱计算：把模型置信度分成 15 个箱，每箱内 |平均置信度 -
     实际正确率| 加权求和。过自信模型（声称 0.95、实际 0.6）ECE 高，
     良好校准模型 ECE 低——尽管两者的"看起来对"的准确率可以完全相同。
  2. 语义熵 vs 字符串熵：当模型多次采样给出"措辞不同但语义相同"的
     答案时（"巴黎" / "法国首都" / "Paris"），原始字符串上的熵很高
     （看似不确定），而先做语义聚类再算的熵很低（实际很确定）。

运行方式：
  python experiments/hallucination_uncertainty.py          # 内置合成演示
  python experiments/hallucination_uncertainty.py --samples file.json
      # 读入真实模型输出，JSON 格式：
      # [
      #   {"question": "...",
      #    "samples": ["答案1", "答案2", ...],          # 同一问题的多次采样
      #    "confidence": 0.85}                          # 可选：模型自报置信度
      # ]
  python experiments/hallucination_uncertainty.py --help   # 查看参数

它不能说明什么（重要）：
  1. 所有数据是**合成的**，只展示度量的数学结构，不构成对任何真实
     LLM 校准/幻觉水平的测量。
  2. 语义聚类的"语义相同"判断用人工分组/字符串规则近似；真实语义熵
     （Kuhn et al. 2023）依赖 NLI 模型做蕴含判定，聚类的错误会直接
     影响熵值。
  3. ECE 对分箱数敏感；15 箱是惯例而非最优。
"""

import argparse
import json
import math
import random


# ---------- 第一部分：ECE 分箱计算 ----------

def compute_ece(confidences, correctness, n_bins=15):
    """标准 ECE：把 [0,1] 置信度等宽分箱，返回 (ECE, 各箱统计)。

    ECE = sum_b (|B_b|/N) * |acc(B_b) - conf(B_b)|
    """
    bins = [[] for _ in range(n_bins)]
    for c, ok in zip(confidences, correctness):
        b = min(int(c * n_bins), n_bins - 1)
        bins[b].append((c, ok))
    ece = 0.0
    table = []
    for b, items in enumerate(bins):
        if not items:
            table.append((b, 0, 0.0, 0.0, 0.0))
            continue
        conf = sum(c for c, _ in items) / len(items)
        acc = sum(ok for _, ok in items) / len(items)
        ece += len(items) / len(confidences) * abs(acc - conf)
        table.append((b, len(items), conf, acc, acc - conf))
    return ece, table


def print_reliability_table(name, table):
    print(f"  {name} reliability 表（15 箱，只列非空箱）：")
    print(f"    {'箱':>4} {'样本':>6} {'平均置信度':>10} {'实际正确率':>10} {'差':>8}")
    for b, cnt, conf, acc, gap in table:
        if cnt:
            print(f"    {b:>4} {cnt:>6} {conf:>10.3f} {acc:>10.3f} {gap:>+8.3f}")


def ece_demo(rng):
    """三组合成数据：完美校准 / 过自信 / 欠自信。"""
    n = 3000
    scenarios = []

    # 完美校准：置信度 c 的样本以概率 c 回答正确
    confs = [rng.random() for _ in range(n)]
    ok = [rng.random() < c for c in confs]
    scenarios.append(("完美校准", confs, ok))

    # 过自信：声称 0.95 的把握实际只有约 0.6（把置信度向 1 挤压）
    confs = [0.6 + 0.4 * rng.random() for _ in range(n)]   # 全都"很自信"
    ok = [rng.random() < 0.6 for _ in range(n)]            # 实际正确率恒为 0.6
    scenarios.append(("过自信", confs, ok))

    # 欠自信：声称 0.4 实际 0.8
    confs = [0.2 + 0.3 * rng.random() for _ in range(n)]
    ok = [rng.random() < 0.8 for _ in range(n)]
    scenarios.append(("欠自信", confs, ok))

    print("== 第一部分：ECE（15 箱）==")
    for name, confs, ok in scenarios:
        ece, table = compute_ece(confs, ok)
        avg_conf = sum(confs) / n
        avg_acc = sum(ok) / n
        print(f"  {name}：平均置信度={avg_conf:.3f}  实际准确率={avg_acc:.3f}  ECE={ece:.3f}")
        print_reliability_table(name, table)
        print()


# ---------- 第二部分：语义熵 vs 字符串熵 ----------

# 语义等价组：归一化函数把同义表达映射到同一语义类别
SEMANTIC_EQUIV = {
    "巴黎": "paris",
    "法国首都": "paris",
    "paris": "paris",
    "the capital of france is paris": "paris",
    "巴黎市": "paris",
    "伦敦": "london",
    "伦敦市": "london",
    "马德里": "madrid",
    "不知道": "unknown",
    "无法回答": "unknown",
}


def normalize(ans):
    """语义归一化：查同义词表，未收录的做小写/去标点/去虚词的粗归一化。"""
    a = ans.strip().lower().rstrip("。.！!?？")
    if a in SEMANTIC_EQUIV:
        return SEMANTIC_EQUIV[a]
    return a


def shannon_entropy(groups_counts):
    """给定计数 dict 计算香农熵（以 nats 计，用 ln）。"""
    total = sum(groups_counts.values())
    if total == 0:
        return 0.0
    h = 0.0
    for c in groups_counts.values():
        p = c / total
        h -= p * math.log(p)
    return h


def semantic_entropy_demo():
    """关键场景：10 次采样中 6 次语义相同但措辞各异 + 语义不同的答案。"""
    samples = [
        "巴黎",
        "法国首都",
        "Paris",
        "巴黎市",
        "The capital of France is Paris",
        "巴黎",
        "伦敦",
        "不知道",
        "伦敦",
        "马德里",
    ]
    str_counts = {}
    sem_counts = {}
    for s in samples:
        str_counts[s] = str_counts.get(s, 0) + 1
        sem_counts[normalize(s)] = sem_counts.get(normalize(s), 0) + 1

    h_str = shannon_entropy(str_counts)
    h_sem = shannon_entropy(sem_counts)

    print("== 第二部分：语义熵 vs 字符串熵 ==")
    print(f"  10 次采样：6 次语义上都是'巴黎'（5 种不同措辞），另有 3 种不同语义答案")
    print(f"  原始字符串分布：{len(str_counts)} 个不同字符串")
    print(f"  语义聚类后分布：{len(sem_counts)} 个语义类别")
    print(f"  字符串熵 = {h_str:.3f} nats（看起来模型很不确定）")
    print(f"  语义熵   = {h_sem:.3f} nats（实际上模型相当确定）")
    print(f"  语义熵比字符串熵低 {h_str - h_sem:.3f} nats ——")
    print("  即：单看字符串多样性会高估模型的不确定性（以及幻觉风险）。")
    print()


def entropy_on_file(samples):
    """对 JSON 输入的每个问题计算两种熵。"""
    print("== 外部采样文件：字符串熵 vs 语义熵 ==")
    print("  （语义归一化用内置同义词表 + 粗字符串规则；真实使用请接入 NLI 聚类）")
    for item in samples:
        q = item.get("question", "?")
        samps = item.get("samples", [])
        str_counts, sem_counts = {}, {}
        for s in samps:
            str_counts[s] = str_counts.get(s, 0) + 1
            sem_counts[normalize(s)] = sem_counts.get(normalize(s), 0) + 1
        print(f"  问题：{q[:40]}{'...' if len(q) > 40 else ''}")
        print(f"    字符串熵 = {shannon_entropy(str_counts):.3f} nats, "
              f"语义熵 = {shannon_entropy(sem_counts):.3f} nats "
              f"({len(samps)} 次采样)")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="ECE 分箱计算 + 语义熵 vs 字符串熵 的构造性演示（合成数据）"
    )
    parser.add_argument(
        "--samples", type=str, default=None,
        help="JSON 文件路径，格式见文件头 docstring；不指定则跑内置合成演示"
    )
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()

    if args.samples:
        with open(args.samples, "r", encoding="utf-8") as f:
            data = json.load(f)
        entropy_on_file(data)
    else:
        rng = random.Random(args.seed)
        ece_demo(rng)
        semantic_entropy_demo()
        print("注意：以上均为合成数据，只演示度量的数学结构；")
        print("不构成对任何真实 LLM 的校准或幻觉水平的测量。")


if __name__ == "__main__":
    main()
