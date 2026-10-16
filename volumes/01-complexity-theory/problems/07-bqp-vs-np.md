# #7 BQP vs NP

**状态**：`OPEN`
**领域**：计算复杂性理论（量子计算）
**首次提出**：1990 年代中期，随量子复杂性类 BQP 的定义出现（Bernstein–Vazirani 1993；Bennett–Bernstein–Brassard–Vazirani 1997）
**参与门槛**：需要新的数学工具

---

## 一句话概述

**量子计算机**能否高效求解 NP 完全问题？反过来，量子计算机能高效解决的问题，是否都在 NP 之内？

## 形式化陈述

**BQP（Bounded-error Quantum Polynomial time）**：由**一致**的量子电路族 $\{Q_n\}$ 定义，每个 $Q_n$ 有 $\mathrm{poly}(n)$ 个量子门，作用于 $n$ 个量子比特（外加辅助比特），使得

$$x \in L \implies \Pr[Q(x)=1] \geq 2/3, \qquad x \notin L \implies \Pr[Q(x)=1] \leq 1/3$$

误差界可由重复运行压到任意小。BQP 对应"量子计算机能高效解决的问题"。

**问题**：$\mathrm{BQP}$ 与 $\mathrm{NP}$ 的相互包含关系

$$\mathrm{NP} \overset{?}{\subseteq} \mathrm{BQP}, \qquad \mathrm{BQP} \overset{?}{\subseteq} \mathrm{NP}$$

两者均为开放问题。已知的包含关系是

$$\mathrm{P} \subseteq \mathrm{BPP} \subseteq \mathrm{BQP} \subseteq \mathrm{AWPP} \subseteq \mathrm{PP} \subseteq \mathrm{PSPACE}$$

其中 $\mathrm{BQP} \subseteq \mathrm{PP}$ 是关键上界。**主流猜想是 $\mathrm{NP} \nsubseteq \mathrm{BQP}$**：量子计算机不能高效求解 NP 完全问题。

**为何这不是显然的**：量子算法在某些**结构化**问题上给出指数加速（见下），因此"量子到底能走多远"起初并不清楚。BQP 是否触及 NP，需要真正的下界论证。

## 为什么困难

### （一）相对化障碍

BQP vs NP 的**两个方向都相对化地分离**：

- 存在神谕 $A$ 使 $\mathrm{NP}^A \nsubseteq \mathrm{BQP}^A$（Bennett–Bernstein–Brassard–Vazirani 1997）——这排除了"用量子算法高效求解所有 NP 问题"的相对化论证；
- 存在神谕 $B$ 使 $\mathrm{BQP}^B \nsubseteq \mathrm{PH}^B$，从而 $\mathrm{BQP}^B \nsubseteq \mathrm{NP}^B$（Aaronson 2010）——这排除了"证明 BQP ⊆ NP"的相对化论证。

因为两个相反方向都存在神谕世界，任何相对化技术都无法确定 BQP 与 NP 的关系。

### （二）Shor 算法非相对化

Shor（1997）证明整数分解与离散对数在 BQP 中，用的是**数论结构**（周期查找、量子傅里叶变换），而非黑箱。这类算法的威力来自问题的**代数结构**，无法推广到一般的 NP 完全问题。这提示：**量子加速是"结构化问题的红利"，而非通用求解器**。

### （三）黑箱下界：Grover 给出的硬限制

对**无序搜索**（黑箱版本），Grover 算法需要 $\Theta(\sqrt{N})$ 次查询，而 Bennett–Bernstein–Brassard–Vazirani（1997）证明这个 $\Omega(\sqrt{N})$ 下界是**最优的**。因此即便对 NP 完全问题，量子黑箱算法最多只能得到**二次**加速，而非指数加速。这一结果被广泛视为"量子计算机不会让 NP 完全问题变简单"的最强证据之一。

### （四）证明 $\mathrm{NP} \nsubseteq \mathrm{BQP}$ 需要量子电路下界

要严格证明 $\mathrm{NP} \nsubseteq \mathrm{BQP}$，需要证明某个 NP 问题**不存在**多项式规模量子电路——这是**量子电路下界**，与经典电路下界（见 [#18 电路下界](18-circuit-lower-bounds.md)）同属一个困难家族。经典情形已被自然化障碍（Razborov–Rudich 1997）严重限制；量子情形的相应障碍理论尚不成熟 [待核实]。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（BQP 的上界） | $\mathrm{BQP} \subseteq \mathrm{PP}$ | Adleman, DeMarrais, Huang, 1997 |
| 上界（更精细） | $\mathrm{BQP} \subseteq \mathrm{AWPP} \subseteq \mathrm{PP}$；$\mathrm{BQP} \subseteq \mathrm{PSPACE}$ | Fortnow & Rogers, 1999 |
| 量子算法（上界） | 整数分解、离散对数 $\in \mathrm{BQP}$（多项式时间量子算法） | Shor, 1997 |
| 黑箱下界 | 无序搜索需 $\Omega(\sqrt{N})$ 次查询，Grover 算法最优 | Bennett–Bernstein–Brassard–Vazirani, 1997 |
| 相对化分离 | 存在神谕 $A$ 使 $\mathrm{NP}^A \nsubseteq \mathrm{BQP}^A$ | Bennett–Bernstein–Brassard–Vazirani, 1997 |
| 相对化分离 | 存在神谕 $B$ 使 $\mathrm{BQP}^B \nsubseteq \mathrm{PH}^B$（故 $\nsubseteq \mathrm{NP}^B$） | Aaronson, 2010 |
| 无条件分离 | **无**：$\mathrm{NP} \subseteq \mathrm{BQP}$ 与 $\mathrm{BQP} \subseteq \mathrm{NP}$ 均未解决 | — |

**上界与下界的区分**：上界方向（BQP 包含什么、被什么包含）成果明确；下界方向只有**相对化 / 黑箱**结论，**没有无条件结果**。断言"量子计算机不可能解决 NP 完全问题"目前仍是猜想，不是定理。

## 解法现状与可行攻击路径

### 已解决的部分

- **结构化子情形的量子多项式算法**：整数分解与离散对数 ∈ BQP（Shor 1997）——量子加速在具有代数结构的问题上已被确定实现。
- **黑箱特例已被完全解决**：无序搜索（黑箱版本）需 $\Theta(\sqrt{N})$ 次查询——Grover 算法达到上界，Bennett–Bernstein–Brassard–Vazirani（1997）证明 $\Omega(\sqrt{N})$ 下界最优。
- **BQP 的上界定位**：$\mathrm{BQP} \subseteq \mathrm{AWPP} \subseteq \mathrm{PP}$（Adleman–DeMarrais–Huang 1997；Fortnow & Rogers 1999），且 $\mathrm{BQP} \subseteq \mathrm{PSPACE}$。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 寻找新的量子算法 | 在代数、几何、图论的特定结构化问题上寻找指数加速 | 只扩大 BQP 的内容 | 不推进 BQP 与 NP 的关系本身 |
| 相对化与黑箱下界 | 在神谕/黑箱模型下建立更细的分离 | 已有 $\mathrm{NP}^A \nsubseteq \mathrm{BQP}^A$ 与 $\mathrm{BQP}^B \nsubseteq \mathrm{PH}^B$ | 产出是相对化结论，受相对化障碍限制，不能翻译为无条件结果 |
| 量子电路下界 | 证明某显式问题不存在多项式规模量子电路，以分离 NP 与 BQP | 这是分离两个方向的"正道"，方向明确 | 经典下界技术本已受自然化障碍限制，量子情形更困难，相应的障碍理论尚不成熟 [待核实] |
| 结构化线索 | 利用 $\mathrm{BQP} \subseteq \mathrm{PP}$ 等上界推理 | 若 $\mathrm{NP} \subseteq \mathrm{BQP}$ 则 $\mathrm{NP} \subseteq \mathrm{PP}$（后者本已成立，无排斥力） | 上界无法区分两种可能 |

### 已堵死的路径

- **相对化**：两个方向都相对化地分离——存在神谕 $A$ 使 $\mathrm{NP}^A \nsubseteq \mathrm{BQP}^A$（Bennett–Bernstein–Brassard–Vazirani 1997），也存在神谕 $B$ 使 $\mathrm{BQP}^B \nsubseteq \mathrm{PH}^B$ 从而 $\nsubseteq \mathrm{NP}^B$（Aaronson 2010）；任何相对化技术都无法确定 BQP 与 NP 的关系。
- **黑箱搜索路线**：$\Omega(\sqrt{N})$ 下界证明即便对 NP 完全问题，量子黑箱算法最多二次加速而非指数加速——"用量子黑箱搜索攻克 NP 完全问题"已被证明不可行。
- **把 Shor 型加速推广到一般 NP 完全问题**：Shor 算法的威力来自数论结构（周期查找、量子傅里叶变换）而非黑箱，无法推广；分解问题本身也不已知是 NP 完全的。

### 裁决

**`路径已知，尚需突破`**

量子算法的能力边界已有明确证据（Grover 最优、Shor 的结构性、$\mathrm{BQP} \subseteq \mathrm{PP}$），分离两个方向的唯一正道是量子电路下界；但该方向被经典电路下界的同类困难（自然化障碍家族）拖住，至今无任何无条件结果——两个方向的包含关系都悬而未决。

## 研究路线图

**路线一：寻找新的量子算法**

研究还有哪些结构化问题能获得量子加速（如代数、几何、图论中的特定问题）。此路线只扩大 BQP 的内容，不推进 BQP 与 NP 的关系。

**路线二：相对化与黑箱下界**

在神谕 / 黑箱模型下建立更细的分离，作为"量子不可能求解 NP"的证据。此路线的产出是**相对化结论**，受相对化障碍限制，不能直接翻译为无条件结果。

**路线三：量子电路下界**

尝试证明某个显式问题不存在小量子电路，以分离 NP 与 BQP。卡点在于：经典下界技术本已受自然化障碍限制，量子情形更为困难。

**路线四：结构化线索**

利用 $\mathrm{BQP} \subseteq \mathrm{PP}$ 等上界。若 $\mathrm{NP} \subseteq \mathrm{BQP}$，则 $\mathrm{NP} \subseteq \mathrm{PP}$；虽然 $\mathrm{NP} \subseteq \mathrm{PP}$ 本身成立（PP 能计数），但把 NP 完全问题全部纳入可高效量子求解的范畴，被普遍认为极不可能。

## 关键文献

1. **Bernstein, E., Vazirani, U.** *Quantum complexity theory.* SIAM J. Comput. 26(5), 1997（STOC 1993）. — 定义 BQP，并给出相对化分离 $\mathrm{BQP}^A \nsubseteq \mathrm{BPP}^A$。
2. **Shor, P.** *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer.* SIAM J. Comput. 26(5), 1997（FOCS 1994）. — 整数分解与离散对数的量子多项式算法。
3. **Adleman, L., DeMarrais, J., Huang, M.-D.** *Quantum computability.* SIAM J. Comput. 26(5), 1997. — 证明 $\mathrm{BQP} \subseteq \mathrm{PP}$。
4. **Bennett, C., Bernstein, E., Brassard, G., Vazirani, U.** *Strengths and weaknesses of quantum computing.* SIAM J. Comput. 26(5), 1997. — 无序搜索的 $\Omega(\sqrt{N})$ 下界，及 $\mathrm{NP}^A \nsubseteq \mathrm{BQP}^A$。
5. **Grover, L.** *A fast quantum mechanical algorithm for database search.* STOC 1996. — 无序搜索的量子二次加速。
6. **Fortnow, L., Rogers, J.** *Complexity limitations on quantum computation.* J. Comput. Syst. Sci. 59(2), 1999. — $\mathrm{BQP} \subseteq \mathrm{AWPP}$ 等上界。
7. **Aaronson, S.** *BQP and the polynomial hierarchy.* STOC 2010. — 给出 $\mathrm{BQP}^A \nsubseteq \mathrm{PH}^A$ 的相对化分离。
8. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 经典电路下界的自然化障碍。
9. **Nielsen, M., Chuang, I.** *Quantum Computation and Quantum Information.* Cambridge University Press, 2000. — 量子计算标准教材。
10. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 10 章讲量子计算与 BQP。

## 常见误区

- **误区：量子计算机能并行尝试所有解，因此能高效求解 NP 完全问题。** —— 这是**最普遍的误解**。量子并行性不等于并行搜索：测量会坍缩，Grover 对无序搜索只能给出 $\sqrt{N}$ 加速，且已被证明是最优的（BBBV 1997）。对指数大的解空间，二次加速远远不够。
- **误区：Shor 算法说明量子计算机能解决 NP 完全问题。** —— 分解问题**不**已知是 NP 完全的，且 Shor 算法依赖分解问题的特殊数论结构，无法推广到一般 NP 完全问题。
- **误区：因为有神谕使 $\mathrm{NP}^A \nsubseteq \mathrm{BQP}^A$，所以 $\mathrm{NP} \nsubseteq \mathrm{BQP}$ 已被证明。** —— 相对化分离**不是**无条件分离。存在这样的神谕只说明"相对化技术无法证明反面"，不等于结论本身成立。
- **误区：$\mathrm{BQP} \subseteq \mathrm{PP}$ 说明 BQP 很弱。** —— PP 是**极强**的类（含 NP，且 PP 包含 BQP）。这条包含关系主要用来定位 BQP 的**上界**，而非说明它弱。真正弱的是 P ⊆ BQP 那一侧。
- **误区：BQP 与 NP 一个是"量子版"、一个是"经典版"，直接比较无意义。** —— 二者是同一计算任务下的不同类，比较它们（谁包含谁）是标准的、有意义的问题；只是答案未知。
- **误区：把"量子优势"（quantum advantage）的实验演示等同于 BQP 与 BPP 的分离。** —— 实验演示的是特定任务上量子机器快于**当前**经典机器，这与**渐近**的类分离（$\mathrm{BQP} \neq \mathrm{BPP}$）是两回事。

## 可运行实验

**`experiments/grover_scaling.py`** — Grover 与经典搜索的查询次数对比

脚本用经典模拟（状态向量）实现 Grover 迭代，对小规模 $N = 2^n$（$n$ 取到能在经典机上模拟的范围，如 $n \leq 20$）测量找到目标所需的**迭代次数**，并与经典线性搜索的期望次数对比，观察 $\Theta(\sqrt{N})$ 与 $\Theta(N)$ 的差异。

**它能验证的已知部分结果**：Grover 算法用约 $\frac{\pi}{4}\sqrt{N}$ 次迭代达到高成功概率，与经典 $N/2$ 次形成对比——这是 BQP 相对 BPP 加速的一个具体实例（虽然 N 太小无法体现渐近分离）。

**这个实验不能说明什么**：

- 只有**二次**加速的行为可见；它**不能**说明量子计算机对 NP 完全问题有指数优势（恰恰相反，BBB V 定理说明做不到）。
- 它测的是**黑箱搜索**这一特定任务，与 $\mathrm{NP} \subseteq \mathrm{BQP}$ 这一一般命题无关。
- 经典模拟量子态本身需要指数资源，能跑到的 $n$ 极小，**不能**推出任何渐近或实际机器性能的结论。

## 延伸阅读

- **教材**：Nielsen & Chuang（文献 [9]）是量子计算标准教材；Arora & Barak（文献 [10]）第 10 章从复杂性角度讲 BQP。
- **综述**：Aaronson 关于量子计算复杂性的综述文章（如 *Quantum Computing since Democritus*，Cambridge University Press, 2013）。
- **相关档案**：[#1 P vs NP](01-p-vs-np.md) 与本题的核心问题直接相连；[#3 P vs PSPACE](03-p-vs-pspace.md) 提供 BQP 的经典上界背景（$\mathrm{BQP} \subseteq \mathrm{PSPACE}$）；[#8 P vs BPP](08-p-vs-bpp.md) 讨论经典随机化的去随机化；[#18 电路下界](18-circuit-lower-bounds.md) 是量子电路下界的经典参照。
