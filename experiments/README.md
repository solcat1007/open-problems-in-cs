# 实验脚本（experiments/）

本目录下是一组**可运行（无外部依赖、仅 Python 标准库）**的实验脚本，用于
**复现与开放问题相关的已知结果 / 已知行为**。所有脚本默认无参数即可运行，
支持 `--help`，单脚本默认在 30 秒内跑完（Python 3.13，标准库；本机 `numpy`
不可用，故全部纯手写）。

---

## ⚠️ 总免责声明（务必先读）

> 这些脚本**全部只是对已知结果、已知行为的数值/构造性复现**，它们**不构成**
> 对任何开放问题的贡献、证明或反证：
>
> - 有限规模的实测数据在原理上无法推出渐近结论，更无法证明/否证 P vs NP、
>   动态最优性、量子纠错阈值、分布式复杂性下界等开放问题；
> - 每个脚本头部 docstring 都写明了**它复现的是什么**、以及**它不能说明什么**；
> - 实验数据是合成的或小规模随机生成的，数字本身没有经验/工程含义，仅供
>   "把抽象概念变成可检验的东西"。

请把它当作教学/直觉工具，而非研究结论。

---

## 脚本清单

| 脚本 | 对应档案（相对路径） | 复现的开放问题 | 运行命令 |
|------|----------------------|----------------|----------|
| `sat_scaling.py` | `../volumes/01-complexity-theory/problems/01-p-vs-np.md` | #1 P vs NP | `python experiments/sat_scaling.py` |
| `np_completeness_chain.py` | `../volumes/01-complexity-theory/problems/01-p-vs-np.md` | #1 P vs NP（归约链） | `python experiments/np_completeness_chain.py` |
| `grover_amplitude_amplification.py` | `../volumes/03-cryptography-security/problems/37-grover-exact-lower-bound.md` | #37 Grover 精确下界 | `python experiments/grover_amplitude_amplification.py` |
| `hallucination_uncertainty.py` | `../volumes/04-ai-machine-learning/problems/45-llm-hallucination.md` | #45 LLM 幻觉 | `python experiments/hallucination_uncertainty.py` |
| `effect_size_calculator.py` | `../volumes/09-software-engineering/problems/90-se-research-scale.md` | #90 软件工程实验方法学 | `python experiments/effect_size_calculator.py` |
| `splay_tree.py` | `../volumes/02-algorithms-data-structures/problems/26-splay-dynamic-optimality.md` | #26 Splay 树动态最优性 | `python experiments/splay_tree.py` |
| `surface_code_threshold.py` | `../volumes/05-quantum-computing/problems/59-quantum-error-correction.md` ，另见 `../volumes/05-quantum-computing/problems/61-qubit-error-rate.md` | #59/#61 量子纠错阈值 | `python experiments/surface_code_threshold.py` |
| `distributed_round_counter.py` | `../volumes/08-networks-distributed/problems/80-kt1-congest-mst.md` ，另见 `../volumes/08-networks-distributed/problems/82-leader-election-singular-optimality.md` | #80/#82 分布式算法 | `python experiments/distributed_round_counter.py` |

> 所有脚本均可用 `--help` 查看可选参数（如样本量、码距、节点数、随机种子等）。

---

## 各脚本要点与边界

- **`sat_scaling.py`**：手写 DPLL（单元传播 + 纯字面量消除）在随机 3-SAT 上
  的求解时间随变量数近似指数增长，且在相变点 α≈4.26 附近最难。只测单一算法、
  单一分布、有限规模——**不**能推出任何渐近结论。
- **`np_completeness_chain.py`**：逐步构造并验证 `SAT → 3-SAT → 独立集 →
  顶点覆盖` 的多项式归约链（解的一一对应）。验证的是**归约构造的正确性**，
  不替代 Cook–Levin 与 NP 完全性证明本身。
- **`grover_amplitude_amplification.py`**：纯向量模拟 Grover 迭代，复现成功概率
  按 `sin((2k+1)θ)` 振荡、峰值在 `k*≈⌊π√N/4⌋`、过旋转等现象。只复现已知上界
  行为，**不**证明 Ω(√N) 查询下界。
- **`hallucination_uncertainty.py`**：ECE 分箱 + 语义熵 vs 字符串熵的构造性演示。
  全部为**合成数据**，只展示度量数学结构，不测量任何真实 LLM。
- **`effect_size_calculator.py`**：Cohen's d / Hedges' g / Cliff's delta 与最小样本量。
  合成 A/B 数据，仅展示统计结构；样本量回答"需多少人才能检出某效应"，不回答
  "效应是否存在"。
- **`splay_tree.py`**：实现 Splay 树（zig / zig-zig / zig-zag 三种旋转），在随机 /
  顺序 / 循环 / Zipf 四种访问序列上对比 splay 总代价 vs 静态最优 BST（DP）代价
  及其比值。只复现**静态最优性**这一已知自适应行为；**不**能验证动态最优性猜想
  （splay 是否被常数因子 bound 在离线最优动态 BST 之内仍是开放问题）。
- **`surface_code_threshold.py`**：d=3 与 d=5 最小（环面）表面码的蒙特卡洛模拟，
  独立 Z 错误、完美测量，union-find（Kruskal 式最近邻配对）解码器，扫描
  p∈[0.01,0.15] 输出成功率曲线，让用户看到两码距曲线**交叉点**（阈值现象的直接
  证据）。但这是**简化模型**（独立错误、完美测量、仅 Z 错误），交叉点数值
  **不等于**真实物理阈值（真实表面码阈值 ≈ 1%）。
- **`distributed_round_counter.py`**：GHS 分布式 MST（简化版 = 分布式 Borůvka）与
  一个领导者选举算法，在随机无向图上统计通信**轮数**与**消息数**。脚本只实测一个
  具体（简化）实现的代价，这些值是**经验上界**；**无法验证任何下界**（如 CONGEST
  模型 Ω(√n)/Ω(D) 轮），下界需理论证明。

---

## 环境与运行

```bash
# 推荐：在项目根目录或 experiments/ 下运行
cd <repo>/open-problems-in-cs/experiments

python sat_scaling.py
python np_completeness_chain.py
python grover_amplitude_amplification.py
python hallucination_uncertainty.py
python effect_size_calculator.py
python splay_tree.py
python surface_code_threshold.py
python distributed_round_counter.py
# 每个都支持 --help
python splay_tree.py --help
```

- 依赖：仅 Python 3.13 标准库（`argparse`、`random`、`math`、`itertools`、
  `collections`、`heapq`、`sys`、`subprocess` 等）。本机无 `numpy`，已全程规避。
- 时长：每个脚本默认均以无参数运行、单脚本 ≤ 30 秒；`surface_code_threshold.py`
  默认每 (d,p) 点 2000 采样。
- 注意：`np_completeness_chain.py` 原默认规模（vars=6, clauses=8, 50 实例）会触发
  指数级暴力验证而超时，已将默认改为 `instances=30, vars=6, clauses=7`（仍全部通过
  归约链验证），并修复了最小顶点覆盖中的剪枝 bug（位掩码值误当计数比较）。
