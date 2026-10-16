# Vol.04 AI 与机器学习

**本册收录 100 题清单中的第 39–58 题，共 20 篇档案。** 状态分级定义见 [METHODOLOGY.md](../../METHODOLOGY.md)，档案格式见 [TEMPLATE.md](../../TEMPLATE.md)。

本册是全清单中**最容易上手**的一册：20 题中有 11 题的门槛标为"可以立刻上手做实验"。这也是**最容易写坏**的一册——因为这个领域的信息噪音最大，大多数问题没有终局答案。以下先说清楚本册与其他分册根本不同的地方。

---

## 一、本册的结构性特征：工程推进远快于理论理解

第一卷（计算复杂性理论）的困难是**单一来源**的：问题难，是因为缺少工具，且已有原理性障碍说明哪些工具不行。本册的困难是**多种来源**的，其中最根本的一条是：

> **在这门学科里，能造出来的东西，远远领先于能解释的东西。**

这一条有三个具体表现。

**表现一：结果是经验性的，且外推无保证。** 标度律（Kaplan et al. 2020；Hoffmann et al. 2022）是拟合，不是定律。任何"更大就更好"的陈述在观测范围之外都只是外推。因此本册大量"当前最好结果"必须是**定性**的——引用规范明确禁止用单一 benchmark 分数代表问题状态（见 [METHODOLOGY.md](../../METHODOLOGY.md) 第六节）。

**表现二：失败模式缺少统一理论。** 深度网络能完美记住随机标签却仍泛化良好（[#54 泛化保证](problems/54-generalization-guarantees.md)），这本身就说明我们的理论工具箱与工程现实脱节。本册大量问题（推理、常识、终身学习）的困难，最终都绕回同一个空洞：**没有一个能解释"模型到底学到了什么"的框架**。

**表现三：很多"解"其实是工程手段，而非原理。** 检索增强、思维链、回放缓冲、量化、水印——都是真实有效的手段，但它们**不回答"为什么有效、能走多远"**。本册的"解法现状与可行攻击路径"一节因此比第一卷写得"实"：具体手段很多，但每一手段的适用边界必须诚实标注。

**为什么这一册仍值得读。** 正因为工程推进快、理论滞后，这里**最容易看到"知识"与"宣称"的差距**。学会分辨二者，比记住任何具体结论都有用。

---

## 二、三类问题：工程瓶颈、理论空白、价值对齐

本册的 20 题不是同一种东西。混淆这三类，会严重误判研究难度与"进展"的含义。

### 第一类：工程瓶颈（Engineering bottleneck）

**特征**：目标清楚，验证清楚，缺的是成本、规模或工艺。

- [#40 数据墙](problems/40-data-wall.md) —— 高质量人类语料有限，解法受成本与合规约束。
- [#47 AI 的能耗问题](problems/47-energy.md) —— 单位能耗下降是已验证的工程事实；难在总需求是否发散。
- [#48 深度伪造检测](problems/48-deepfake-detection.md) —— 封闭集检测可靠；难在开放集下的攻防不对称。
- [#49 训练数据的动态组合](problems/49-data-mixture.md) —— 目标函数不可观测，只能靠代理信号。
- [#55 可复现性保证](problems/55-reproducibility.md) —— 度量口径与报告规范问题。
- [#57 多模态细粒度检索](problems/57-multimodal-retrieval.md) —— 检索质量与细粒度对齐。

**这类问题的"进展"可以测量**：单位成本下降、覆盖扩大、误差降低。但也最容易出现"进步很快"的错觉——测的常常是工程曲线，而非问题本身是否被理解。

### 第二类：理论空白（Theoretical gap）

**特征**：问题可以清楚陈述，但我们没有能给出正确解释或保证的框架。

- [#39 推理差距](problems/39-reasoning-gap.md) —— 分布内拟合与分布外组合的落差，缺少理论刻画。
- [#42 当前架构能否实现通用智能](problems/42-architecture-limits.md) —— 目标概念未定义，缺上下界工具。
- [#43 常识推理](problems/43-common-sense.md) —— "默认不说"的知识难以通过统计覆盖。
- [#44 终身学习](problems/44-lifelong-learning.md) —— 稳定性与可塑性的结构性冲突。
- [#46 AI 的可解释性](problems/46-interpretability.md) —— "解释"的定义本身存在争议。

此外还有 [#50](problems/50-epistemic-uncertainty-rl.md)、[#52](problems/52-compositional-sparsity.md)、[#53](problems/53-adversarial-robustness.md)、[#54](problems/54-generalization-guarantees.md)、[#56](problems/56-unidentifiability.md)、[#58](problems/58-vqa-language-bias.md)（见下表总览）。

**这一类是本册的主体。** 注意其中 [#54](problems/54-generalization-guarantees.md) 是唯一的 `OPEN-BARRIER`：均匀收敛这条最自然的证明路线，已被证明在重要情形下必然失败（Nagarajan & Kolter 2019）。**这是本册唯一一处有可能与第一卷"障碍"传统对话的地方**——它限制的是证明技术，不是问题答案。

### 第三类：价值对齐问题（Value alignment）

**特征**：**连"解决"的定义都难以说清。** 困难不在技术实现，而在目标侧——"对齐到什么""由谁定义""如何验证"本身是被争论的对象。

- [#41 对齐瓶颈](problems/41-alignment.md) —— 目标不可完备写出、验证不可独立完成，因此"是否已对齐"无法判定。
- [#45 大语言模型的幻觉问题](problems/45-llm-hallucination.md) —— "幻觉"没有公认定义；"与事实矛盾"需要一个可能出错的事实真源；且评测本身受污染。
- [#51 奖励黑客问题](problems/51-reward-hacking.md) —— 判别"是否在刷代理"需要一个"真实目标"，而该目标正是问题本身。

**这一类是与前两类最不同的。** 对工程瓶颈，可以问"成本降了多少"；对理论空白，可以问"有没有定理"；但对价值对齐问题，**连"进步"都难以定义**——因为所优化的是代理目标，而代理与真实目标的差距恰恰是问题的定义。本册因此在裁决中从不对这类问题给出"可解"方向的暗示。

**三类的重叠是常态**：数据墙（第一类）里的合成数据会引入模型坍缩，那部分属于第二类；奖励黑客（第三类）的可形式化子问题在玩具环境里又属于第二类。**把每题只看成单一类型，是最常见的误判来源。**

---

## 三、本册二十题总览

| # | 问题 | 状态 | 门槛 | 核心卡点（一句话） |
|---|---|---|---|---|
| 39 | [推理差距](problems/39-reasoning-gap.md) | `OPEN` | 可以立刻上手做实验 | 缺少验证器时，无法区分真推理与"看起来对的匹配" |
| 40 | [数据墙](problems/40-data-wall.md) | `OPEN` | 主要缺的是方法论 | 合成数据在无验证器域会放大自身偏置 |
| 41 | [对齐瓶颈](problems/41-alignment.md) | `OPEN` | 需要长期工程积累 | 目标不可完备写出，验证不可独立完成 |
| 42 | [当前架构能否实现通用智能](problems/42-architecture-limits.md) | `OPEN` | 需要新的数学工具 | 目标概念未定义，缺可判定的度量 |
| 43 | [常识推理](problems/43-common-sense.md) | `OPEN` | 可以立刻上手做实验 | 常识的很大一部分是"默认不说"的，语料信号极弱 |
| 44 | [终身学习](problems/44-lifelong-learning.md) | `OPEN` | 可以立刻上手做实验 | 稳定性与可塑性在共享参数上直接冲突 |
| 45 | [大语言模型的幻觉问题](problems/45-llm-hallucination.md) | `OPEN` | 可以立刻上手做实验 | "幻觉"无公认定义，事实真源本身可能出错 |
| 46 | [AI 的可解释性](problems/46-interpretability.md) | `OPEN` | 需要新的数学工具 | 忠实性与可理解性存在内在张力，机制分析有规模壁垒 |
| 47 | [AI 的能耗问题](problems/47-energy.md) | `OPEN` | 需要长期工程积累 | 效率提升能否跑赢需求增长，两侧都不可外推 |
| 48 | [深度伪造检测](problems/48-deepfake-detection.md) | `OPEN` | 可以立刻上手做实验 | 开放集攻防不对称：生成方掌握过程信息 |
| 49 | [训练数据的动态组合](problems/49-data-mixture.md) | `OPEN` | 可以立刻上手做实验 | 目标函数不可微、不可观测，只能用代理信号 |
| 50 | [RL 中的认知不确定性解耦](problems/50-epistemic-uncertainty-rl.md) | `OPEN` | 可以立刻上手做实验 | 认知与偶然不确定性难以在同一框架下分离 |
| 51 | [奖励黑客问题](problems/51-reward-hacking.md) | `OPEN` | 可以立刻上手做实验 | 判别"刷分"需要一个"真实目标"，而它正是问题本身 |
| 52 | [深度学习的组合稀疏性理论](problems/52-compositional-sparsity.md) | `OPEN` | 需要新的数学工具 | 缺少刻画"组合结构如何被学习"的理论 |
| 53 | [对抗鲁棒性](problems/53-adversarial-robustness.md) | `OPEN` | 可以立刻上手做实验 | 鲁棒性与准确性、容量之间存在张力 |
| 54 | [泛化保证](problems/54-generalization-guarantees.md) | `OPEN-BARRIER` | 需要新的数学工具 | 均匀收敛界被证在重要情形下必然空泛 |
| 55 | [可复现性保证](problems/55-reproducibility.md) | `OPEN` | 主要缺的是方法论 | 度量口径与报告规范不统一 |
| 56 | [极端不可识别性下的学习](problems/56-unidentifiability.md) | `OPEN` | 需要新的数学工具 | 观测不足时目标不可识别 |
| 57 | [多模态细粒度检索](problems/57-multimodal-retrieval.md) | `OPEN` | 可以立刻上手做实验 | 细粒度对齐缺少可靠评测与保证 |
| 58 | [视觉问答中的语言偏差](problems/58-vqa-language-bias.md) | `PARTIAL` | 可以立刻上手做实验 | 偏差机制部分被诊断，但消除无通用解 |

---

## 四、阅读地图

**若你只有半小时**：读 [#54 泛化保证](problems/54-generalization-guarantees.md) 的"为什么困难"一节与 [#45 幻觉](problems/45-llm-hallucination.md) 的"形式化陈述"一节。前者告诉你本册唯一的原理性障碍长什么样，后者告诉你为什么本册一半问题的"形式化陈述"只能是"为什么无法形式化"。

**若你想先建立"三类问题"的直觉**：在"二"中按 [工程瓶颈 → 理论空白 → 价值对齐] 各挑一题对读——[#47 能耗](problems/47-energy.md)、[#44 终身学习](problems/44-lifelong-learning.md)、[#41 对齐](problems/41-alignment.md)。

**若你对"能力宣称"保持警惕**：读 [#39 推理差距](problems/39-reasoning-gap.md) → [#43 常识推理](problems/43-common-sense.md) → [#42 架构极限](problems/42-architecture-limits.md)。这条线从"单点任务上的失败机制"走到"通用能力的度量设计"。

**若你关心安全问题**：[#41 对齐](problems/41-alignment.md) → [#51 奖励黑客](problems/51-reward-hacking.md) → [#46 可解释性](problems/46-interpretability.md) → [#53 对抗鲁棒性](problems/53-adversarial-robustness.md)。共同母题是**在缺少可靠验证时如何保证行为**。

**交叉依赖**（值得并读）：

- [#54 泛化保证](problems/54-generalization-guarantees.md) ↔ [#53 对抗鲁棒性](problems/53-adversarial-robustness.md) ↔ [#41 对齐](problems/41-alignment.md)：泛化与鲁棒性保证的缺失，是"对齐"难以形式化的直接原因——**你无法对行为边界不可预测的系统做形式化保证**。
- [#40 数据墙](problems/40-data-wall.md) ↔ [#49 数据组合](problems/49-data-mixture.md) ↔ [#44 终身学习](problems/44-lifelong-learning.md)：数据、混合、持续更新构成一条"数据生命周期"链。
- [#45 幻觉](problems/45-llm-hallucination.md) ↔ [#39 推理差距](problems/39-reasoning-gap.md) ↔ [#43 常识推理](problems/43-common-sense.md)：三者共享同一个验证困难。
- [#47 能耗](problems/47-energy.md) ↔ [#42 架构极限](problems/42-architecture-limits.md)：算力能否持续，直接影响"继续扩大规模"是否可行。

---

## 五、哪些问题最适合动手实验

本册 11 题标为"可以立刻上手做实验"，且**全部不需要 GPU**。按可做性排序：

**无需任何外部依赖（纯标准库 / numpy 即可）**：

- **#39 推理差距** —— 构造捷径特征，观察分布外崩溃（`experiments/reasoning_shortcut.py`）。
- **#44 终身学习** —— 复现灾难性遗忘的准确率矩阵（`experiments/catastrophic_forgetting.py`）。
- **#54 泛化保证** —— 随机标签记忆 + 双下降 + 空泛界的数值演示（`experiments/generalization_gap.py`）。
- **#45 幻觉** —— 期望校准误差 ECE 与语义熵的构造逻辑（`experiments/hallucination_uncertainty.py`）。
- **#46 可解释性** —— 不同归因方法给出不一致排序（`experiments/interpretability_probe.py`）。
- **#43 常识推理** —— 非单调默认推理与例外撤销（`experiments/commonsense_default.py`）。

**需要一点图像/信号处理库**：

- **#48 深度伪造检测** —— 频域谱对比 + 后处理脆弱性（`experiments/deepfake_artifact_probe.py`）。
- **#47 能耗问题** —— 训练代价随规模的曲线与口径敏感性（`experiments/energy_scaling.py`）。

**其余可做性较高的**：[#40 数据墙](problems/40-data-wall.md)、[#49 数据组合](problems/49-data-mixture.md)、[#50](problems/50-epistemic-uncertainty-rl.md)、[#51](problems/51-reward-hacking.md)、[#53](problems/53-adversarial-robustness.md)、[#57](problems/57-multimodal-retrieval.md)、[#58](problems/58-vqa-language-bias.md)。

**统一警告**：每份档案的"可运行实验"一节都写明了**该实验不能说明什么**——**先读这一条，再动手**。本册所有实验的共同结论是同一条：**小规模上观察到的现象不能外推到前沿规模**。实验的价值在于让你亲手看清某个失败机制或度量口径，而不是产出能力评估。

---

## 关联阅读

- **本册内部**：见"四、阅读地图"中的四条主路径与四条交叉依赖链。
- **跨册引用**：
  - [#1 P vs NP](../01-complexity-theory/problems/01-p-vs-np.md) —— 相对化 / 自然化 / 代数化三重障碍，是全仓库的方法论地基；本册多处"验证与生成不对称"的类比都以它为参照（但请注意那只**是类比**，无归约关系）。
  - [#18 电路下界](../01-complexity-theory/problems/18-circuit-lower-bounds.md) —— 本册认为"当前架构有计算上界"的讨论需对照此题的边界。
  - [#31 从任意单向函数构造密钥交换](../03-cryptography-security/problems/31-key-exchange-from-owf.md) —— 对抗性设定下"检测方信息劣势"与密码学中的信息结构有形式上的相似。
- **方法论**：[METHODOLOGY.md](../../METHODOLOGY.md) 第一节（状态分级）与第六节（引用规范）。**请先读这两节，再读任何一份档案的"当前最好结果"表。**
