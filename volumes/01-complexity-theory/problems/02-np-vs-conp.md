# #2 NP vs Co-NP

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论
**首次提出**：1971 年前后，随 NP 类的定义出现（常归于 Stephen Cook 与 Richard Karp 的早期工作）
**参与门槛**：需要新的数学工具

---

## 一句话概述

如果每个"有解"的实例都能被快速**验证**，那么每个"无解"的事实是否也能被快速**验证**？

## 形式化陈述

设 $L \subseteq \Sigma^*$ 为一个判定问题，$\bar L = \Sigma^* \setminus L$ 为其补集。定义

$$\mathrm{co\text{-}NP} = \{\, L \subseteq \Sigma^* : \bar L \in \mathrm{NP} \,\}$$

展开这个定义：$L \in \mathrm{co\text{-}NP}$ 当且仅当存在多项式 $p$ 与多项式时间可计算的关系 $V$，使得

$$x \in L \iff \forall y,\ |y| \leq p(|x|),\ V(x,y)=1$$

也就是说，**"否"实例拥有多项式规模的证书**。这正是 co-NP 与 NP 的唯一区别：NP 要求"是"实例有简短证书，co-NP 要求"否"实例有简短证书。

**问题**：$\mathrm{NP} \overset{?}{=} \mathrm{co\text{-}NP}$

以下三个命题等价，可任取其一作为问题的形式化表述：

1. $\mathrm{NP} = \mathrm{co\text{-}NP}$；
2. NP 在补运算下封闭（对任意 $L \in \mathrm{NP}$ 都有 $\bar L \in \mathrm{NP}$）；
3. 存在一个 NP 完全问题属于 co-NP。

第 3 条在实践中最好用：**只要能为任何一个 NP 完全问题（如 SAT）的补集给出简短证书，就证明了两类相等**。

**与 P vs NP 的关系**：$\mathrm{P}$ 在补运算下封闭，因此

$$\mathrm{P} = \mathrm{NP} \implies \mathrm{NP} = \mathrm{co\text{-}NP}$$

取逆否命题得 $\mathrm{NP} \neq \mathrm{co\text{-}NP} \implies \mathrm{P} \neq \mathrm{NP}$。可见 NP vs co-NP 是一个比 P vs NP **更弱**的命题：证明前者会顺带解决后者，反之不然。这正是它值得单列、又不完全等同于母问题的原因。

## 为什么困难

### （一）相对化障碍

Baker、Gill 与 Solovay（1975）的构造不仅适用于 P vs NP，也适用于 NP vs co-NP：存在神谕 $A$ 使 $\mathrm{NP}^A = \mathrm{co\text{-}NP}^A$，同时存在神谕 $B$ 使 $\mathrm{NP}^B \neq \mathrm{co\text{-}NP}^B$。因此任何"对一切神谕都成立"的证明技术——包括 1970 年代的全部对角化与模拟方法——都无法解决本问题。

### （二）自然化与代数化障碍的连带作用

因为 $\mathrm{NP} \neq \mathrm{co\text{-}NP}$ 蕴含 $\mathrm{P} \neq \mathrm{NP}$，任何能分离这两类的论证必然也分离 P 与 NP。于是自然化障碍（Razborov–Rudich 1997）与代数化障碍（Aaronson–Wigderson 2009）所排除的技术，在这里同样无效。换言之，本问题继承母问题的全部障碍，只是结论更弱。

### （三）本问题特有的困难：非存在性证书

NP 的证书形如"存在一个解"——这种对象**可以被直接猜出、写出并检查**。co-NP 的证书形如"不存在解"，而要证明某类对象不存在，通常比指出一个对象存在困难得多。这不是技术细节，而是本问题在直觉上难以攻克的根源：我们缺少构造"否"实例简短证据的一般方法。

### （四）启发式

必须强调：**存在障碍不等于问题不可解**。障碍限制的是**证明技术**，不是答案。它的实用价值在于一条快速筛选规则——任何只用相对化、自然化或代数化技术的论证，必然有错。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（算法） | 每个 NP ∩ co-NP 问题都有指数时间确定性算法；无多项式时间算法已知 | 标准结论 |
| 下界 | **无任何无条件分离**；连 $\mathrm{NP} \neq \mathrm{co\text{-}NP}$ 都未证明 | — |
| 结构性 | $\mathrm{P} = \mathrm{NP} \Rightarrow \mathrm{NP} = \mathrm{co\text{-}NP}$ | 标准结论 |
| 结构性 | $\mathrm{NP} = \mathrm{co\text{-}NP}$ 当且仅当存在多项式有界的命题证明系统 | Cook & Reckhow, 1979 |
| 结构性 | $\mathrm{NP} = \mathrm{co\text{-}NP} \Rightarrow \mathrm{PH} = \mathrm{NP}$（多项式层级坍缩到第一层） | 标准结论 |
| 结构性 | 若存在稀疏的 NP 完全集，则 $\mathrm{P} = \mathrm{NP}$，从而两类相等 | Mahaney, 1982 |
| 候选中间类 | 素性在 NP ∩ co-NP 中（Pratt 证书）；其判定版本此后已知在 P 中。整数分解的判定版本也在 NP ∩ co-NP 中 | Pratt, 1975；Agrawal–Kayal–Saxena, 2004 |

**严格区分上界与下界**：上界一栏说的是"存在算法"，下界一栏说的是"不存在算法"。本问题在下界方向**没有任何非平凡结果**——我们甚至无法排除 $\mathrm{NP} = \mathrm{co\text{-}NP}$。

## 解法现状与可行攻击路径

### 已解决的部分

- **NP ∩ co-NP 中的具体问题**：素性有简短证书（Pratt 1975），其判定版本此后已知在 P 中（Agrawal–Kayal–Saxena 2004）；整数分解的判定版本也在 NP ∩ co-NP 中。这些是"是/否证书对称"的真实子情形。
- **具体证明系统的下界**：对 Resolution、Frege 系统、Extended Frege 等**具体**命题证明系统已有超多项式下界——但"对所有系统"的排除尚无进展。
- **结构性刻画已确立**：NP = co-NP 当且仅当存在多项式有界的命题证明系统（Cook & Reckhow 1979）；NP = co-NP ⟹ PH = NP；P = NP ⟹ NP = co-NP；稀疏 NP 完全集不存在（Mahaney 1982）。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 证明复杂性（Cook–Reckhow 对偶） | 攻击目标转为"证明不存在多项式有界的命题证明系统" | 对具体系统（Resolution、Frege、Extended Frege）已有超多项式下界 | 对所有系统的排除无进展；证明复杂性的强下界又与电路下界纠缠，同样受自然化障碍限制 |
| NP ∩ co-NP 的结构研究 | 研究"若 NP = co-NP"的后果（层级坍缩、NP 完全集补集性质等） | 产出条件性结论 | 不直接推进无条件分离 |
| 算法化下界 | 仿 Williams（2011）思路：先为更强电路类给出非平凡 SAT 算法再导出下界 | 尚未触及能分离 NP 与 co-NP 的强度 | 所需算法强度远超当前水平 |

### 已堵死的路径

- **相对化**（Baker–Gill–Solovay 1975）：存在神谕使 $\mathrm{NP}^A = \mathrm{co\text{-}NP}^A$，也存在神谕使二者不等，故一切"对神谕成立"的技术（对角化、模拟）无效。
- **自然化与代数化的连带**：NP ≠ co-NP 蕴含 P ≠ NP，任何能分离这两类的论证必然也分离 P 与 NP，母问题的全部障碍在此同样无效。
- 研究路线图明确列为"已被排除"的：纯对角化、纯模拟，以及任何相对化或代数化的论证。
- "为某个 NP 完全问题（如 SAT）的补集给出简短证书"这一最直接路线至今无人做到，且该路线正受相对化障碍限制。

### 裁决

**`原理上受限`**

本问题继承母问题 P vs NP 的全部三重障碍，另有其特有困难：NP 的证书形如"存在一个解"可直接写出检查，co-NP 的证书形如"不存在解"，我们缺少构造"否"实例简短证据的一般方法。下界方向无任何无条件结果。

## 研究路线图

**路线一：证明复杂性（Cook–Reckhow 对偶）**

由等价命题，攻击目标转为"证明不存在多项式有界的命题证明系统"。对具体系统（Resolution、Frege 系统、Extended Frege 等）已有超多项式下界，但**对所有系统**的排除尚无进展。这条路线的卡点在于：证明复杂性自身的强下界又与电路下界纠缠在一起，因而同样受自然化障碍限制。

**路线二：NP ∩ co-NP 的结构研究**

研究"如果 $\mathrm{NP} = \mathrm{co\text{-}NP}$"会带来哪些后果（层级坍缩、NP 完全集补集的性质等）。此路线产出的是**条件性结论**，不直接推进无条件分离。

**路线三：算法化下界**

仿照 Williams（2011）以 SAT 加速算法分离 NEXP 与 ACC⁰ 的思路，先为更强的电路类给出非平凡 SAT 算法，再导出下界。目前尚未触及能分离 NP 与 co-NP 的强度。

**已被排除的路线**：纯对角化、纯模拟，以及任何相对化或代数化的论证。

## 关键文献

1. **Cook, S.** *The complexity of theorem-proving procedures.* STOC 1971. — 定义 NP 与 NP 完全性。
2. **Karp, R.** *Reducibility among combinatorial problems.* 收录于 *Complexity of Computer Computations*, 1972. — 确立 NP 完全问题的普遍性。
3. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍。
4. **Cook, S., Reckhow, R.** *The relative efficiency of propositional proof systems.* J. Symbolic Logic 44(1), 1979. — 把 NP vs co-NP 改写为命题证明系统问题。
5. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 自然化障碍。
6. **Aaronson, S., Wigderson, A.** *Algebrization: A New Barrier in Complexity Theory.* ACM Trans. Comput. Theory 1(1), 2009. — 代数化障碍。
7. **Pratt, V.** *Every prime has a succinct certificate.* SIAM J. Comput. 4(3), 1975. — 素性的简短证书，NP ∩ co-NP 的经典例子。
8. **Mahaney, S.** *Sparse complete sets for NP: Solution of a conjecture of Berman and Hartmanis.* J. Comput. Syst. Sci. 25(2), 1982. — 稀疏完全集蕴含坍缩。
9. **Agrawal, M., Kayal, N., Saxena, N.** *PRIMES is in P.* Annals of Mathematics 160(2), 2004. — 素性判定落入 P。
10. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 2–3 章。
11. **Papadimitriou, C.** *Computational Complexity.* Addison-Wesley, 1994. — 经典教材，对 NP ∩ co-NP 与层级结构有清晰讨论。

## 常见误区

- **误区：NP 与 co-NP 是互斥的两类。** —— 恰恰相反，$\mathrm{P} \subseteq \mathrm{NP} \cap \mathrm{co\text{-}NP}$，交集**非空**（P 中每个问题都在两者中，因为 P 对补封闭）。焦点是它们是否**恰好相等**。
- **误区：SAT 的补集看起来很难，所以 $\mathrm{NP} \neq \mathrm{co\text{-}NP}$ 已被证明。** —— "看起来难"不是证明。本问题在下界方向无任何无条件结果。
- **误区：$\mathrm{NP} \neq \mathrm{co\text{-}NP}$ 与 $\mathrm{P} \neq \mathrm{NP}$ 是同一个命题。** —— 不是。$\mathrm{P} = \mathrm{NP}$ 蕴含 $\mathrm{NP} = \mathrm{co\text{-}NP}$，但在已知范围内反之不成立；前者更弱。
- **误区：证明了某个 NP 完全问题不在 co-NP 中，就等于分离了两类。** —— 这**确实**能分离两类（若某 NP 完全问题不属于 co-NP，则 $\mathrm{NP} \neq \mathrm{co\text{-}NP}$），但至今无人做到，且这条路线正受相对化障碍限制。
- **误区：把"co-NP 完全"理解为"比 NP 完全更难"。** —— co-NP 完全问题（如 UNSAT、重言式判定）与 NP 完全问题在复杂度上是对称的。$\mathrm{NP} \neq \mathrm{co\text{-}NP}$ 若成立，只说明两类不交于各自的完全问题，并不比较二者的"难度高低"。
- **误区：Cook–Reckhow 定理"解决了"本问题。** —— 它给出的是**等价重述**（$\mathrm{NP} = \mathrm{co\text{-}NP}$ 等价于存在多项式有界的证明系统），把问题换了个形式，并未解决它。

## 可运行实验

**`experiments/np_conp_certificate.py`** — 对比"是"证书与"否"证书的长度增长

脚本对若干小规模实例同时构造并测量两类证书：(a) 一个可满足 3-SAT 实例的满足赋值（"是"证书）；(b) 一个不可满足实例在 **Resolution（分辨率）** 系统下的反驳（"否"证书）。随后比较两者规模随实例变量数的增长。

**它能验证的已知部分结果**：对随机 3-SAT，在相变点（子句/变量比约 4.26）附近，"是"实例通常有一个易于检查的解，而"否"实例在 Resolution 下的最短反驳规模增长很快。这直观展示了"否"证书为何难以构造。

**这个实验不能说明什么**：

- 它只考察了**一种**证明系统（Resolution）。Cook–Reckhow 定理要求的是**存在某个**多项式有界系统，故 Resolution 上的（指数）下界**不蕴含** $\mathrm{NP} \neq \mathrm{co\text{-}NP}$。
- 它测的是**有限规模**与**特定实例分布**，任何有限实测都无法推出渐近结论。
- 它完全无法触及"究竟是否存在多项式有界证明系统"这一核心问题。

## 延伸阅读

- **教材**：Arora & Barak（文献 [10]）第 2 章；Papadimitriou（文献 [11]）中关于补类与多项式层级的讨论。
- **证明复杂性入门**：关于 Resolution 与 Frege 系统下界的综述，可作为 Cook–Reckhow 路线的延伸。
- **相关档案**：[#1 P vs NP](01-p-vs-np.md) 是本问题的母问题；[#9 PH vs PSPACE](09-ph-vs-pspace.md) 讨论补运算封闭性对层级的影响；[#18 电路下界](18-circuit-lower-bounds.md) 与证明复杂性存在技术联系。
