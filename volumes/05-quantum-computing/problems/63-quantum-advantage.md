# #63 量子优势的实际应用

**状态**：`OPEN`
**领域**：量子计算
**首次提出**：问题动机源于 Feynman（1982，用量子系统模拟量子物理）；"量子优势"（quantum advantage / quantum supremacy）作为术语流行于 2010 年代，Preskill（2018）等人对其含义做过系统辨析
**参与门槛**：可以立刻上手做实验

---

## 一句话概述

目前所有"量子优势"演示都发生在**特定构造的问题**上、且可被经典方法在改进后处理或绕过——它们与"在实用问题上超过经典最佳方法"之间隔着一整条鸿沟，本题问的就是鸿沟对岸到底有没有可到达的立足点。

## 形式化陈述

本问题的理论部分有清楚的形式，开放部分是经验性的，需分别陈述。

**理论上已确立的（作为背景）**：

- 存在明确的算法加速：Shor 算法在多项式时间内分解整数与求离散对数（Shor, SIAM J. Comput. 1997，FOCS 1994）；Grover 搜索的 $\Theta(\sqrt N)$ 紧界（Grover 1996；Bennett-Bernstein-Brassard-Vazirani 1997，见 [#37](../03-cryptography-security/problems/37-grover-exact-lower-bound.md)）。
- 量子计算相对经典计算的能力边界（BQP 与经典类的关系）是独立的开放问题，见 [#7 BQP vs NP](../01-complexity-theory/problems/07-bqp-vs-np.md)。

**开放的经验命题**：

> 是否存在一个**实用**问题（有真实的科学或商业价值），使得某台量子设备在其**实际规模的实例**上，以可接受的成本与时间，超过**可获得的最佳经典方法**？

注意这个命题的三个限定词——"实用"（排除构造性问题）、"实际规模"（排除玩具实例）、"可获得的最佳"（排除稻草人式经典对比）。已有演示无一条同时满足三者。

## 为什么困难

1. **演示问题的构造性。** 已有的两类招牌演示——随机线路采样（Arute et al., Nature 2019）与高斯玻色采样（Zhong et al., Science 2020）——选择的问题本身就是为了让量子设备好做、让经典模拟难做。这与"实用问题恰好落在量子有优势的区域"是两回事。
2. **经典方法在追赶。** 量子演示公布后，经典模拟的代价估算随后被多项工作大幅压缩——Arute et al. 2019 声称的经典模拟耗时估计即被后续经典算法显著下调 `[待核实]`（具体数字）。每一次演示都演变成"演示—经典追赶"的循环。
3. **验证的困境。** 量子设备只有在**经典算得动**的问题上才容易被验证；而经典算得动的问题，量子优势又无从谈起。Aaronson（*Read the Fine Print*, Nature Physics 2015）对此有经典讨论。
4. **容错前提。** 实用规模的实例（如化学基态精确求解）需要的电路深度远超 NISQ 设备的可用范围——本题的答案被 [#60](60-nisq-to-ftqc.md) 的答案所钳制。
5. **NISQ 算法的可训练性与加速来源存疑。** 变分算法（VQE / QAOA）至今无证据表明能超过经典启发式（见 [#65](65-quantum-machine-learning.md) 与 McClean et al. 2018）。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 优势演示（采样类） | 超导处理器上随机线路采样的"优势"声明；经典代价随后被大幅下调 | Arute et al., Nature 574, 2019；经典追赶工作 `[待核实]` |
| 优势演示（光子类） | 光学平台上玻色采样的"优势"声明 | Zhong et al., Science 370, 2020 |
| 实用方向的小规模演示 | 超导比特上的 Hartree-Fock 计算（演示，非优势） | Arute et al., Science 369, 2020 |
| 原则性区分工具 | 对"优势"声明的审读框架 | Aaronson, *Read the Fine Print*, Nature Physics 11, 2015 |
| 浅电路的经典能力 | 浅深度量子电路可被经典多项式时间模拟——划出 NISQ 原则上难以产生优势的一片区域 | Bravyi & Gosset, Phys. Rev. Lett. 116, 2016 |
| 实用优势的达成 | **无已知结果**——没有任何量子设备在实用问题上超过经典最佳方法 | — |

## 解法现状与可行攻击路径

### 已解决的部分

- **算法层面的加速存在性**：Shor（指数加速，密码分析方向）与 Grover（平方根加速，紧界）是严格证明的。这些是"若容错机器可造，则加速必然兑现"的数学事实。
- **演示的方法论**：如何在采样问题上构造可核查的优势实验，已被 Arute 2019 与 Zhong 2020 两类方案建立（连同对其假设的批评体系，Aaronson 2015）。
- **部分排除区**：Bravyi-Gosset 2016 表明浅深度电路类经典可模拟，为"NISQ 能在哪里产生优势"划出了负面地图。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 量子化学模拟 | 模拟电子结构（Feynman 1982 的原初动机） | 小分子演示（Arute 2020 等），无优势 | 需要容错规模；经典方法（如各类数值方法）也在进步 |
| 密码分析 | Shor 算法分解整数 | 算法严格成立（Shor 1997） | 完全被 [#60](60-nisq-to-ftqc.md) 的硬件前提钳制；且价值在攻击侧 |
| 采样问题的中间应用 | 把采样优势嫁接到实用领域 | 无已知非平凡结果 | 演示问题的构造性与实用需求不匹配 |
| 优化与机器学习 | QAOA / 变分算法 | 无超过经典启发式的证据 | 可训练性与优势来源存疑（McClean 2018） |

### 已堵死的路径

暂无原理性排除结果（"量子在一切实用问题上无优势"这类命题本身无法被证明，也无证据）。但有几类**方法论上的死路**值得记录：以"经典方法算不动某个构造性采样问题"来宣称实用优势——已被"演示—经典追赶"循环与 Aaronson 2015 的审读框架反复证伪为不充分论证。

### 裁决

**`条件可解`**

加速的数学基础（Shor、Grover）是严格的，但它兑现为实用优势的前提——容错量子计算与合适问题实例——一个都还没满足。结论完全条件于 [#60](60-nisq-to-ftqc.md) 与 [#59](59-quantum-error-correction.md) 的工程进展；前提未证时，"实用优势存在"与"不存在"都无确定结论。

## 研究路线图

1. **化学模拟主线**：从演示走向基态求解的精度与规模竞争——短期受 NISQ 限制，长期受容错规模限制，两头都未通。
2. **采样优势的巩固**：让采样问题的经典难度**可证明**（而非估计性）——这是把演示升级为严格结论的方向，进展有限 `[待核实]`。
3. **混合工作流**：量子设备作为经典 HPC 流水线中的特殊协处理器——概念吸引人，尚无已验证的实用节点。
4. **反面工作**：系统性地改进经典方法——历史上每一次"优势声明"的缩水都来自这里；这条路的价值被长期低估。

## 关键文献

1. **Feynman, R.** *Simulating Physics with Computers.* Int. J. Theor. Phys. 21, 1982. — "用量子机器做量子模拟"的原初动机。
2. **Shor, P.** *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.* SIAM J. Comput. 26(5), 1997（FOCS 1994）. — 最强的已证算法加速。
3. **Grover, L.** *A Fast Quantum Mechanical Algorithm for Database Search.* STOC 1996. — 平方根加速及（配合下界）紧界。
4. **Arute, F. et al.** *Quantum Supremacy Using a Programmable Superconducting Processor.* Nature 574, 2019. — 采样类优势声明的代表。
5. **Zhong, H.-S. et al.** *Quantum Computational Advantage Using Photons.* Science 370, 2020. — 光子平台的优势声明代表。
6. **Aaronson, S.** *Read the Fine Print.* Nature Physics 11, 2015. — 如何审读优势声明的标准参考。
7. **Bravyi, S., Gosset, D.** *Improved Classical Simulation of Quantum Circuits Dominated by Clifford Gates.* Phys. Rev. Lett. 116, 2016. — 浅电路经典可模拟性，NISQ 优势的负面地图之一。
8. **Arute, F. et al.** *Hartree-Fock on a Superconducting Qubit Quantum Computer.* Science 369, 2020. — 实用方向的代表性**演示**（非优势）。
9. **Preskill, J.** *Quantum Computing in the NISQ Era and Beyond.* Quantum 2, 2018；*Quantum Computing 40 Years Later.* 2021. — 概念框架与现状评估。

## 常见误区

- **误区："量子优势已被演示"等于"量子计算机已有用"。** —— 已有演示全部是**特定构造问题**上的，且经典方法随后跟进；这与实用加速之间有本质距离。这是本题最需要传达的区分。
- **误区：经典方法"永远"追不上某个采样演示。** —— 历史证据相反：每次优势声明后经典代价估计都被显著下调 `[待核实]`。把"当前经典算不动"当成"原则上算不动"，混淆了经验观察与复杂性下界。
- **误区：Shor 算法证明了量子计算很快就有民用应用。** —— Shor 的加速兑现方向是**攻破**现有公钥密码（见 [#37](../03-cryptography-security/problems/37-grover-exact-lower-bound.md) 与 Vol.03），这需要容错机器（[#60](60-nisq-to-ftqc.md)）；它不是民用应用的证明。
- **误区：Grover 的平方根加速足以带来实用优势。** —— 平方根加速对常数因子与错误纠错开销极其敏感；在多数实际场景中不划算（见 [#37](../03-cryptography-security/problems/37-grover-exact-lower-bound.md)）。
- **误区：量子化学模拟"显然"会有优势。** —— 这是动机层面的信念，不是结论；经典计算化学方法同样在快速进步，竞争是动态的。
- **误区：优势命题可以像数学猜想一样被"证明"。** —— "存在实用优势"包含经验成分（问题实例、成本、经典方法的现状），无法写成纯数学命题；能严格化的只有算法复杂度本身。

## 可运行实验

**`experiments/qft_period_finding.py`** — 复现量子傅里叶变换作用于周期函数的峰值行为

用纯 numpy 构造周期函数的均匀叠加态，应用量子傅里叶变换（QFT），观察输出概率在周期倍数处的峰值集中；扫描比特数看峰值锐化。这是 Shor 算法核心子程序的最小可运行演示，也是"量子加速从结构中来"的体感。

**绝不能说明**：这个演示验证的是**已有算法**在一个可精确模拟的小系统上的行为，与"实用优势是否存在"无关；它也不能暗示 Shor 算法在真实设备上容易实现——真实噪声、纠错开销与数据加载问题都不在模拟中出现。真实量子设备行为无法在经典模拟中复现。

**`experiments/shallow_vs_brute.py`**（可选配套）— 对浅深度随机电路做直接经典模拟（Bravyi-Gosset 一类思路的最小版），体感"浅电路经典可模拟"的含义。

## 延伸阅读

- **入门**：Aaronson, *Read the Fine Print*（文献 [6]），短文，是审读一切优势声明的第一课。
- **历史脉络**：Preskill 2021（文献 [9]）。
- **相关档案**：[#60 NISQ 到容错量子计算的过渡](60-nisq-to-ftqc.md)（本题的硬件前提）、[#59 量子纠错](59-quantum-error-correction.md)、[#64 领域专用量子机器](64-domain-specific-quantum.md)（优势问题的另一形态）、[#65 量子机器学习](65-quantum-machine-learning.md)、[#7 BQP vs NP](../01-complexity-theory/problems/07-bqp-vs-np.md)（优势的复杂性理论背景）、[#37 Grover 下界](../03-cryptography-security/problems/37-grover-exact-lower-bound.md)、[#88 量子软件工程](../09-software-engineering/problems/88-quantum-software-engineering.md)。
