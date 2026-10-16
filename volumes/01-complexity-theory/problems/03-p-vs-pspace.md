# #3 P vs PSPACE

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论
**首次提出**：1970 年代，随空间复杂性与多项式层级的研究出现（Savitch 1970；Stockmeyer–Meyer 1973）
**参与门槛**：需要新的数学工具

---

## 一句话概述

一个用**多项式空间**就能判断的问题，是否也一定能在**多项式时间**内判断？

## 形式化陈述

设 $\Sigma$ 为有限字母表。

**多项式空间可判定类**：

$$\mathrm{PSPACE} = \bigcup_{c \geq 1} \mathrm{DSPACE}(n^c)$$

即存在一台确定性图灵机，对长度 $n$ 的输入至多使用 $O(n^c)$ 个存储单元、对运行时间不加限制地给出正确判定。

**多项式时间可判定类**：$\mathrm{P} = \bigcup_{k \geq 1} \mathrm{DTIME}(n^k)$。

**问题**：$\mathrm{P} \overset{?}{=} \mathrm{PSPACE}$

由于任何一个多项式空间机器最多运行 $2^{O(n^c)}$ 步（否则无限循环），有

$$\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PH} \subseteq \mathrm{PSPACE} \subseteq \mathrm{EXP}$$

这里 $\mathrm{PH}$ 是多项式层级，$\mathrm{EXP} = \bigcup_k \mathrm{DTIME}(2^{n^k})$。整条链中所有包含关系是否严格均未知，本问题关注其中最下游那一段的反向包含：$\mathrm{PSPACE} \subseteq \mathrm{P}$ 是否成立。**若 $\mathrm{P} = \mathrm{PSPACE}$，则由上式整条链全部塌缩为 P。**

**关键等价事实（Savitch 1970）**：$\mathrm{PSPACE} = \mathrm{NPSPACE}$，即空间类的非确定性不增强能力（非确定机器用 $s(n)$ 空间，确定机器用 $O(s(n)^2)$ 空间即可模拟）。因此本问题与 $\mathrm{P}$ vs $\mathrm{NPSPACE}$ 是同一个问题。

**完全问题**：量化的布尔公式问题 TQBF（True Quantified Boolean Formula）是 PSPACE 完全的（Stockmeyer–Meyer 1973）。

## 为什么困难

### （一）相对化障碍

取 $A$ 为一个 PSPACE 完全集（如 TQBF）。由于 $A \in \mathrm{PSPACE}$，且 PSPACE 在相对 $A$ 下不增大，可得 $\mathrm{P}^A = \mathrm{PSPACE}^A = \mathrm{PSPACE}$——存在**塌缩**的神谕。另一方面，存在使 $\mathrm{P}^A \neq \mathrm{PSPACE}^A$ 的神谕。两个方向的相对化世界都存在，故任何相对化技术都无法解决本问题。

### （二）继承 P vs NP 的三重障碍

$\mathrm{NP} \subseteq \mathrm{PSPACE}$，所以 $\mathrm{P} \neq \mathrm{PSPACE}$ 蕴含 $\mathrm{P} \neq \mathrm{NP}$。任何能证明 $\mathrm{P} \neq \mathrm{PSPACE}$ 的论证，稍加改造即可证明 $\mathrm{P} \neq \mathrm{NP}$。因此相对化、自然化（Razborov–Rudich 1997）、代数化（Aaronson–Wigderson 2009）三重障碍对本题**全部适用**。本问题在技术上比 P vs NP 更强，障碍也更重。

### （三）空间层级定理够不到 P

对角化在**空间**情形下确实能给出无条件分离：空间层级定理（Stearns–Hartmanis–Lewis 1965）证明 $\mathrm{DSPACE}(o(f)) \subsetneq \mathrm{DSPACE}(f)$，于是 $\mathrm{L} \subsetneq \mathrm{PSPACE}$ 是无条件结论。但该定理比较的是**同类资源**的两个不同量级，无法跨越"时间 vs 空间"这一资源边界，因此给不出 $\mathrm{P} \subsetneq \mathrm{PSPACE}$。

### （四）一个可用作"参照"的推论

由标准的填充（padding）论证可得：若 $\mathrm{P} = \mathrm{PSPACE}$，则 $\mathrm{EXP} = \mathrm{EXPSPACE}$（把指数空间类的实例按多项式放大成多项式空间实例，再回代）。因为学界普遍相信 $\mathrm{EXP} \neq \mathrm{EXPSPACE}$，这说明**证明 $\mathrm{P} \neq \mathrm{PSPACE}$ 至少与证明 $\mathrm{EXP} \neq \mathrm{EXPSPACE}$ 一样困难**。该推论属标准教材内容，具体表述请以 [Arora & Barak 2009] 为准。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界 | 每个 PSPACE 问题都可用指数时间确定性算法求解；$\mathrm{PSPACE} = \mathrm{NPSPACE}$ | Savitch, 1970 |
| 下界 | **无** $\mathrm{P} \subsetneq \mathrm{PSPACE}$ 的无条件证明；空间层级定理给出 $\mathrm{L} \subsetneq \mathrm{PSPACE}$ | Stearns–Hartmanis–Lewis, 1965 |
| 结构性 | $\mathrm{P} = \mathrm{PSPACE} \Rightarrow \mathrm{P} = \mathrm{NP} = \mathrm{PH} = \mathrm{PSPACE}$ | 标准结论 |
| 结构性 | $\mathrm{P} = \mathrm{PSPACE} \Rightarrow \mathrm{EXP} = \mathrm{EXPSPACE}$ | 标准填充论证 |
| 完全问题 | TQBF 是 PSPACE 完全的 | Stockmeyer & Meyer, 1973 |

**上界与下界的区分**：上界方向说的是"存在算法"，下界方向说的是"不存在算法"。在下界方向，除空间层级定理给出的 $\mathrm{L} \subsetneq \mathrm{PSPACE}$ 外，**没有任何针对 P 的非平凡结果**。

## 解法现状与可行攻击路径

### 已解决的部分

- **同类资源的空间分离**：空间层级定理（Stearns–Hartmanis–Lewis 1965）无条件证明 $\mathrm{L} \subsetneq \mathrm{PSPACE}$——同类资源、不同量级之间的分离已经解决；但该定理无法跨越"时间 vs 空间"的资源边界。
- **非确定性与确定性的等价**：Savitch（1970）证明 $\mathrm{PSPACE} = \mathrm{NPSPACE}$，本问题与非确定性版本是同一个问题——候选问题的形式已被缩减。
- **结构性刻画已确立**：TQBF 是 PSPACE 完全的（Stockmeyer & Meyer 1973）；P = PSPACE ⟹ 整条包含链塌缩为 P，且 P = PSPACE ⟹ EXP = EXPSPACE（标准填充论证）。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 算法化下界 | 与 P vs NP 相同：先为某电路类给出非平凡 SAT 算法，再导出下界 | 强度远不足以区分 P 与 PSPACE | 所需的算法与下界强度整体欠缺 |
| 空间-时间权衡 | 研究能在较小空间内解决通用问题的算法及其极限（DTISP 类结果） | SAT 不在 $\mathrm{DTISP}(n^{2\cos(\pi/7)-o(1)}, n^{o(1)})$ 中是当前少数可靠的通用下界 | 距分离 P 与 PSPACE 极远 |
| 完全问题的精细刻画 | 把 P = PSPACE 归约为 TQBF 等 PSPACE 完全问题能否被显著加速 | 产出条件性结论 | 不推进无条件分离 |

### 已堵死的路径

- **相对化**：存在塌缩的神谕（取 PSPACE 完全集 $A$，则 $\mathrm{P}^A = \mathrm{PSPACE}^A = \mathrm{PSPACE}$）与分离的神谕，两个方向的相对化世界都存在，故任何相对化技术无法解决本题。
- **三重障碍全部适用**：$\mathrm{P} \neq \mathrm{PSPACE}$ 蕴含 $\mathrm{P} \neq \mathrm{NP}$，任何证明前者的论证稍加改造即可证明后者，因此相对化、自然化、代数化对本题全部生效；本题比 P vs NP 更强，障碍也更重。
- **对角化的资源类型限制**：对角化在空间情形确能分离同类资源（层级定理），但被证明无法跨越时间与空间的边界——研究路线图明确列为已排除的：纯对角化、纯模拟，以及一切相对化或代数化论证。

### 裁决

**`原理上受限`**

本题严格强于 P vs NP，三重障碍全部适用；唯一无条件可用的对角化工具又被限制在同类资源之内，无法触及时间 vs 空间这一核心边界，下界方向没有任何针对 P 的非平凡结果。

## 研究路线图

**路线一：算法化下界**
与 P vs NP 相同：先为某电路类给出非平凡 SAT 算法，再导出下界。这条路线的强度目前远不足以区分 P 与 PSPACE。

**路线二：空间-时间权衡（space-time tradeoff）**
研究能在较小空间内解决通用问题的算法，并寻找其极限（如 [#1 P vs NP](01-p-vs-np.md) 中提到的 $\mathrm{DTISP}$ 类结果）。此类下界（如 SAT 不在 $\mathrm{DTISP}(n^{2\cos(\pi/7)-o(1)}, n^{o(1)})$ 中）是当前少数可靠的通用下界，但距分离 P 与 PSPACE 极远。

**路线三：完全问题的精细刻画**
把 $\mathrm{P} = \mathrm{PSPACE}$ 归约为某个 PSPACE 完全问题（如 TQBF）是否可被显著加速。此类研究给出条件性结论，不推进无条件分离。

**已被排除的路线**：纯对角化（受资源类型限制）、纯模拟，以及一切相对化或代数化论证。

## 关键文献

1. **Savitch, W.** *Relationships between nondeterministic and deterministic tape complexities.* J. Comput. Syst. Sci. 4(2), 1970. — $\mathrm{PSPACE} = \mathrm{NPSPACE}$。
2. **Stearns, R., Hartmanis, J., Lewis, P.** *Hierarchies of memory limited computations.* FOCS 1965. — 空间层级定理。
3. **Stockmeyer, L., Meyer, A.** *Word problems requiring exponential time.* STOC 1973. — 引入多项式层级，并证明 TQBF 是 PSPACE 完全的。
4. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍。
5. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 自然化障碍。
6. **Aaronson, S., Wigderson, A.** *Algebrization: A New Barrier in Complexity Theory.* ACM Trans. Comput. Theory 1(1), 2009. — 代数化障碍。
7. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 4 章讲空间复杂性，第 3 章讲层级。
8. **Papadimitriou, C.** *Computational Complexity.* Addison-Wesley, 1994. — 经典教材，对 PSPACE 完全性有系统整理。

## 常见误区

- **误区：PSPACE 是"指数空间"。** —— 不是。PSPACE 是**多项式**空间；指数空间记为 EXPSPACE。混淆二者会把包含链写错。
- **误区：因为 PSPACE 完全问题（如 TQBF、博弈类问题）很难，所以 $\mathrm{P} \neq \mathrm{PSPACE}$ 已被证明。** —— "问题难"是直觉，不是证明。本问题在方向 $\mathrm{P} \neq \mathrm{PSPACE}$ 上无任何无条件结果。
- **误区：空间层级定理已经证明了 $\mathrm{P} \neq \mathrm{PSPACE}$。** —— 它证明的是 $\mathrm{L} \subsetneq \mathrm{PSPACE}$（同类资源、不同量级）。它**不能**跨资源类型比较时间与空间，给不出 $\mathrm{P} \subsetneq \mathrm{PSPACE}$。
- **误区：非确定性对空间有帮助。** —— Savitch 定理指出 $\mathrm{PSPACE} = \mathrm{NPSPACE}$：在多项式空间这个量级上，非确定性**不增加**能力。这与时间情形（相信 $\mathrm{P} \neq \mathrm{NP}$）形成鲜明对比。
- **误区：把 $\mathrm{PSPACE} \subseteq \mathrm{EXP}$ 当作"PSPACE 就是 EXP"。** —— 二者是否相等（即 $\mathrm{PSPACE} \subsetneq \mathrm{EXP}$ 是否严格）同样是未知的；不要把包含关系读成相等。
- **误区：既然 $\mathrm{P} = \mathrm{PSPACE}$ 蕴含 $\mathrm{P} = \mathrm{NP}$，那么"先解决 P vs NP 就能顺带解决本题"。** —— 顺序反了：$\mathrm{P} \neq \mathrm{NP}$ 只说 $\mathrm{P} \neq \mathrm{PSPACE}$ 的必要条件，并不蕴含它。本题严格更强。

## 可运行实验

**`experiments/tqbf_game_solver.py`** — 用博弈树理解 PSPACE 完全性

脚本把一个小规模 TQBF 实例编码成一场**双人对弈**（存在量词对应"我"的走法，全称量词对应"对手"的走法），用带记忆化的搜索或简单的交替量化枚举求解，并测量所需的空间与时间随公式规模的增长。

**它能验证的已知部分结果**：TQBF 的博弈语义（$\exists$ / $\forall$ 交替即"我走 / 对手走"），以及用 $O(n)$ 递归深度（对应多项式空间）即可判定的现象。这有助于建立对"PSPACE 完全"这一概念的具体体感。

**这个实验不能说明什么**：

- 它只是在一个**玩具规模**上复现了 TQBF 的判定过程，**不能**推出"TQBF 需要指数时间"或任何渐近下界。
- 它测的是**实现**在有限实例上的性能，与 $\mathrm{P} \neq \mathrm{PSPACE}$ 这一数学命题无关。
- 它无法触及由相对化/自然化/代数化障碍限制的任何证明路线。

## 延伸阅读

- **教材**：Arora & Barak（文献 [7]）第 4 章；Papadimitriou（文献 [8]）第 8、19 章，对 PSPACE 完全性与博弈有生动讲解。
- **科普**：Fortnow, *The Golden Ticket*（Princeton University Press, 2013）中对包含链的通俗介绍。
- **相关档案**：[#1 P vs NP](01-p-vs-np.md) 是本题的必要条件；[#2 NP vs Co-NP](02-np-vs-conp.md) 讨论补类封闭性；[#9 PH vs PSPACE](09-ph-vs-pspace.md) 关注层级与 PSPACE 之间的那一段；[#4 NC vs P](04-nc-vs-p.md) 从并行视角切入 P 的边界。
