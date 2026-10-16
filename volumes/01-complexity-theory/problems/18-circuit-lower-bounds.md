# #18 电路下界问题

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论（电路复杂性）
**首次提出**：研究可追溯到 Shannon 的计数论证（1949）；现代形式的电路下界问题在 1970 年代随复杂度类理论确立
**参与门槛**：需要新的数学工具

---

## 一句话概述

能否证明：**任何**多项式规模的电路都算不出某个**可显式写出**的布尔函数（例如判断一个图是否包含三角形）？做不到这一点，便无法排除 $\mathrm{P} = \mathrm{NP}$。

## 形式化陈述

**电路模型**：布尔电路是由与非门（或任意完备基）构成的有向无环图，$n$ 个输入位，一个输出位。"**规模**"指门的数量。

对函数 $s : \mathbb{N} \to \mathbb{N}$：

$$\mathrm{SIZE}(s(n)) = \{L : L \text{ 可由规模 } O(s(n)) \text{ 的电路族判定}\}, \qquad \mathrm{P}/\mathrm{poly} = \bigcup_{k \ge 1} \mathrm{SIZE}(n^k)$$

$\mathrm{P}/\mathrm{poly}$ 是**非一致**（non-uniform）类：每个输入长度允许使用不同的电路，不要求存在统一生成它们的算法。故 $\mathrm{P} \subseteq \mathrm{P}/\mathrm{poly}$。

**核心问题**：是否存在**显式**函数 $f$，使得对**每一个**常数 $k$ 都有 $f \notin \mathrm{SIZE}(n^k)$？最强目标是

$$\mathrm{NP} \nsubseteq \mathrm{P}/\mathrm{poly}$$

逻辑关系必须写明：$\mathrm{NP} \nsubseteq \mathrm{P}/\mathrm{poly}$ **蕴含** $\mathrm{P} \neq \mathrm{NP}$（因 $\mathrm{P} \subseteq \mathrm{P}/\mathrm{poly}$），故这是一个**更强**因而更难的陈述。反向不成立——完全可能有 $\mathrm{P} \neq \mathrm{NP}$ 而 $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly}$。

两条关键结构性结论：

- **Karp–Lipton（1982）**：$\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly}$ 蕴含多项式层级坍缩到 $\Sigma_2$。
- **Kannan（1982）**：对**每个固定的** $k$，$\Sigma_2^P \nsubseteq \mathrm{SIZE}(n^k)$。这是无条件下界，但只对固定多项式规模成立。

两者合起来刻画了当前的技术边界：能证明"对每个固定 $k$ 都有函数难"，却无法证明"存在一个函数对所有 $k$ 都难"。

## 为什么困难

本题是全套档案中"障碍"讲得最清楚的一题。一句话概括：**电路下界的主要敌人是自然化障碍，它揭示的深刻张力是——证明电路下界的能力，与密码学能否存在，相互排斥。**

### 一、相对化障碍不适用于电路下界（必须澄清的区别）

**相对化障碍**（Baker–Gill–Solovay 1975）：任何"对一切神谕都成立"的技术都无法证明 $\mathrm{P} \neq \mathrm{NP}$——存在神谕 $A$ 使 $\mathrm{P}^A = \mathrm{NP}^A$，也存在神谕 $B$ 使 $\mathrm{P}^B \neq \mathrm{NP}^B$。

电路下界**不在此列**：已知下界证明都是**非相对化**的——若给 $\mathrm{AC}^0$ 电路加上能算 PARITY 的神谕门，$\mathrm{PARITY} \notin \mathrm{AC}^0$ 立刻失效。因此本题真正相关的障碍是**自然化障碍**（及更广意义上的**代数化障碍**）。

### 二、自然化障碍的机制：构造性 + 广泛性 ⟹ 与伪随机性冲突

称一个函数集合 $\mathcal{P}$（即一个"性质"）是**自然的**（natural），若：

1. **构造性**（constructivity）：给定 $f$ 的真值表（$2^n$ 位），可在时间 $2^{O(n)}$ 内判定 $f \in \mathcal{P}$——"哪些函数具有该性质"是可有效计算的。
2. **广泛性**（largeness）：均匀随机函数以不可忽略的概率属于 $\mathcal{P}$，即 $\Pr_f[f \in \mathcal{P}] \ge 1/\mathrm{poly}(2^n)$。

再假设 $\mathcal{P}$ 是**有用的**（usefulness）：$f \in \mathcal{P}$ 意味着 $f$ 需要超多项式规模电路。这正是想证的结论——一个能识别"难函数"的判据。

**定理（Razborov–Rudich 1997）**：若存在伪随机生成器（等价地，若存在单向函数，见 [#13](13-one-way-functions.md)），则**不存在**同时满足构造性、广泛性与有用性的 $\mathcal{P}$。

证明骨架：假设这样的 $\mathcal{P}$ 存在，构造算法 $D$ 区分真随机与伪随机。输入长度 $2^n$ 的串 $w$（解释为一个函数的真值表），输出 $[w \in \mathcal{P}]$。

- $w$ 真随机时：由**广泛性**，$w \in \mathcal{P}$ 的概率不可忽略，$D$ 大概输出 1。
- $w$ 伪随机时（由短种子经小电路算出）：$w$ 作为函数"简单"、可用小电路计算，由**有用性**，$w \notin \mathcal{P}$，$D$ 输出 0。

于是 $D$ 以不可忽略的优势区分了真随机与伪随机——与伪随机生成器的定义矛盾。**它不是说下界证明不可能，而是说"任何试图用可有效检查的组合性质去捕捉难函数的路线"，都必须以放弃伪随机性为代价**——而伪随机性等价于单向函数，也就等价于现代密码学的地基。

### 三、与密码学存在性的根本张力

> **你要么接受密码学存在（那就必须放弃"自然的"证明技术，只能找"非自然"的技术），要么放弃密码学（那就可以尽情使用组合计数）。**

一个纯数学的证明技术问题，与一个被广泛依赖的安全基础，被证明**互相排斥**。

注意张力的**方向**：Razborov–Rudich 以"单向函数存在"为**前提**的条件性结论。前提成立则障碍生效、必须找非自然技术；若不成立（现代密码学全灭），障碍失效、组合计数重新可用。无论哪种情况，**都不能**说"因此电路下界不可能被证明"——障碍限制的是**技术**，不是**命题的真假**。

### 四、三个障碍的关系

| 障碍 | 出处 | 针对什么 | 对电路下界是否适用 |
|---|---|---|---|
| 相对化 | Baker–Gill–Solovay 1975 | 神谕无关的证明技术 | **不适用**：电路下界证明本身是非相对化的 |
| 自然化 | Razborov–Rudich 1997 | 构造性 + 广泛性的组合技术 | **直接适用**：本题最主要的障碍 |
| 代数化 | Aaronson–Wigderson 2009 | 允许低次多项式扩张的技术 | 对 P vs NP 一类分离构成限制；对电路下界的精确约束范围取决于技术是否"代数化" [待核实：本档案未核对代数化框架对 Williams 型技术的判定] |

一句话总结：**相对化封锁了 1970 年代的对角化工具，自然化封锁了 1980–90 年代的组合计数工具，代数化则封锁了"用交互式证明与代数方法绕过前两者"的希望。** 电路下界的战场在第二层。

### 五、为什么至今没有可行的"非自然"路线

绕过自然化障碍只有两条理论出路，两条都受阻：

- **放弃构造性。** 性质无法有效判定时，证明就失去可验证的组合内容。Kannan（1982）的无条件下界正是用（非构造的）对角化得到的——它不与自然化障碍冲突，正因为其性质不满足构造性条件。但这类技术无法扩展到一般电路。
- **放弃广泛性。** 若性质只对特定函数成立，就必须能"瞄准"那个函数；而随机函数（下界最主要的对象）不受约束。已知的非自然下界只能覆盖极弱模型。

一条重要观察：$\mathrm{AC}^0$ 与单调电路的下界（Håstad 1986；Razborov 1985；Alon–Boppana 1987）确实"自然"却不与障碍冲突——这两个模型无法计算伪随机函数（单调电路没有否定、$\mathrm{AC}^0$ 太弱），障碍的前提不成立。

### 六、算法化下界

Williams（2011 / 2014）提出**算法化下界**：先给出某电路类中 SAT 的非平凡加速算法，再由该算法推出下界，由此证明 $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$。它**不是**"定义性质并检查所有小电路函数都不满足"的论证，故形式上不落在 Razborov–Rudich 框架内；它究竟规避了构造性还是广泛性，文献表述略有差异 [待核实：两种框架下的具体归属]，本仓库 [#1](01-p-vs-np.md) 采用"不满足广泛性"的表述。**卡点在算法一侧**：对 $\mathrm{TC}^0$、$\mathrm{NC}^1$ 或一般多项式规模电路，所需的快 SAT 算法尚不存在。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（已知小电路） | PARITY 有规模 $O(n)$ 的电路；加法、乘法有近线性规模电路 | 标准构造 |
| 下界（通用电路） | 存在显式函数需要 $\ge 3n - o(n)$ 规模的电路（更精确的常数形式如 $(3+1/86)n - o(n)$） | Find–Golovnev–Hirsch–Kulikov 2016 |
| 下界（常数改进） | 后续工作可能改进了该常数 **[待核实：未核对最新常数与其出处]** | — |
| 下界（$\mathrm{AC}^0$） | $\mathrm{PARITY} \notin \mathrm{AC}^0$（任意常数深度） | Ajtai 1983；Furst–Saxe–Sipser 1984；Håstad 1986 |
| 下界（单调电路） | CLIQUE 需要指数级单调电路规模 | Razborov 1985；Alon–Boppana 1987 |
| 下界（$\mathrm{ACC}^0$） | $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$（非一致） | Williams 2011 / 2014 |
| 下界（固定多项式规模） | 对每个固定的 $k$，$\Sigma_2^P \nsubseteq \mathrm{SIZE}(n^k)$（无条件） | Kannan 1982 |
| 结构性 | $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly} \Rightarrow \mathrm{PH} = \Sigma_2$ | Karp–Lipton 1982 |
| 结构性 | 存在 $\mathrm{E}$ 中需 $2^{\Omega(n)}$ 规模电路的函数 ⟺ 某类伪随机生成器存在 | Nisan–Wigderson 1994；Impagliazzo–Wigderson 1997 |
| 条件性 | 若单向函数存在，则任何"自然的"组合技术都不能证明电路下界 | Razborov–Rudich 1997 |

严格区分：**上界**栏是"存在小电路"（正向构造），**下界**栏是"证明了任何电路都做不到"。最关键的一条对照：通用电路下界的最新记录是 **$3n - o(n)$，一个线性量级**，而需要的是**超多项式**下界——差距是**量级**而非常数因子；把 $3n - o(n)$ 说成"接近 $\mathrm{P} \neq \mathrm{NP}$"是严重误读。

## 解法现状与可行攻击路径

### 已解决的部分

电路下界的分层战场中，较弱层次已被攻克：

- **AC⁰**：PARITY ∉ AC⁰（Ajtai 1983；Furst–Saxe–Sipser 1984；Håstad 1986 的开关引理），对任意常数深度成立。
- **单调电路**：CLIQUE 需要指数级单调电路规模（Razborov 1985；Alon–Boppana 1987）。这两个模型的下界"自然"却不与障碍冲突——它们无法计算伪随机函数（单调电路没有否定、AC⁰ 太弱），障碍的前提不成立。
- **ACC⁰**：NEXP ⊄ ACC⁰（Williams 2011/2014，算法化下界）。
- **固定多项式规模**：对每个固定的 $k$，$\Sigma_2^P \nsubseteq \mathrm{SIZE}(n^k)$（Kannan 1982，无条件下界，用非构造的对角化得到，故不与自然化障碍冲突）。
- **通用电路**：存在显式函数需 $\ge 3n - o(n)$ 规模（Find–Golovnev–Hirsch–Kulikov 2016）——但是**线性量级**，距超多项式下界是量级差距。
- **结构性刻画**：NP ⊆ P/poly ⟹ PH = Σ₂（Karp–Lipton 1982）；E 中需 $2^{\Omega(n)}$ 规模电路的函数 ⟺ 某类伪随机生成器存在（Nisan–Wigderson 1994；Impagliazzo–Wigderson 1997）。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 算法化下界（Williams 路线） | 先为电路类 $C$ 找快 SAT 算法，再推出 NEXP ⊄ C | 对 ACC⁰ 成功 | 对更强电路类，所需 SAT 算法等价于更强的下界，形成循环 |
| 非自然证明技术 | 有意放弃构造性或广泛性 | 只在极弱模型有效 | 前者失去组合内容，后者难以覆盖随机函数 |
| 几何复杂性理论（GCT） | Mulmuley–Sohoni 用代数几何与表示论分离代数复杂性类（VP vs VNP） | 纲领能预测自己会遇到的障碍 | 尚未产生任何无条件下界，障碍理论远未成熟 |
| 电路类分层推进 | AC⁰ → ACC⁰ → TC⁰ → NC¹ → P/poly 逐层攻克 | 前两层已解决，ACC⁰ 被 Williams 攻克 | TC⁰ 及以上是开放前沿，每层都要重写技术，没有统一迁移机制 |

### 已堵死的路径

- **自然化**（Razborov–Rudich 1997）：若单向函数存在（即密码学地基成立），则不存在同时满足"构造性 + 广泛性 + 有用性"的性质——一切"自然的"组合计数技术被成体系排除。这是本题最主要的障碍，且揭示证明电路下界的能力与密码学存在性互相排斥。
- **两条理论出路各自受阻**：放弃构造性则证明失去可验证的组合内容（Kannan 型对角化因此无法扩展到一般电路）；放弃广泛性则必须"瞄准"特定函数，而随机函数（下界最主要的对象）不受约束——已知的非自然下界只能覆盖极弱模型。
- **相对化**：相对化障碍对电路下界**不适用**（下界证明本身是非相对化的），本题真正的战场在自然化一层；代数化对下界技术的精确约束范围 [待核实：本档案未核对代数化框架对 Williams 型技术的判定]。

### 裁决

**`原理上受限`**

自然化障碍直接排除了本题最主要的证明技术，并以"密码学是否存在"为代价形成根本张力；当前通用下界停留在 $3n - o(n)$ 的线性量级，与所需的超多项式下界相差的是量级而非常数因子。

## 研究路线图

**路线一：算法化下界（Williams 路线）。** 先为电路类 $C$ 找快 SAT 算法，再推出 $\mathrm{NEXP} \nsubseteq C$。现状：对 $\mathrm{ACC}^0$ 成功。**卡点**：对更强电路类，所需 SAT 算法等价于更强的下界，形成循环。

**路线二：非自然证明技术。** 有意放弃构造性或广泛性。现状：只在极弱模型有效。**卡点**：前者失去组合内容，后者难以覆盖随机函数。

**路线三：几何复杂性理论（GCT）。** Mulmuley 与 Sohoni（2001 / 2007）用代数几何与表示论分离代数复杂性类（如 $\mathrm{VP}$ vs $\mathrm{VNP}$）。现状：纲领能预测自己会遇到哪些障碍，但**尚未产生任何无条件下界**；所需障碍理论远未成熟。

**路线四：电路类分层推进。** $\mathrm{AC}^0 \to \mathrm{ACC}^0 \to \mathrm{TC}^0 \to \mathrm{NC}^1 \to \mathrm{P}/\mathrm{poly}$。现状：前两层已解决，$\mathrm{ACC}^0$ 由 Williams 攻克，$\mathrm{TC}^0$ 及以上是开放前沿。**卡点**：每层都要重写技术，没有统一迁移机制。

**哪条路被堵死？** 一切满足"构造性 + 广泛性"的组合计数技术（Razborov–Rudich 1997）。

## 关键文献

1. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 自然化障碍，本问题最核心的文献。
2. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍的原始出处。
3. **Aaronson, S., Wigderson, A.** *Algebrization: A New Barrier in Complexity Theory.* ACM Trans. Comput. Theory 1(1), 2009. — 代数化障碍。
4. **Håstad, J.** *Almost optimal lower bounds for small depth circuits.* STOC 1986. — $\mathrm{AC}^0$ 下界的经典证明（开关引理）。
5. **Ajtai, M.** *$\Sigma^1_1$-formulae on finite structures.* Annals of Pure and Applied Logic, 1983. — $\mathrm{PARITY} \notin \mathrm{AC}^0$ 的早期证明之一。
6. **Furst, M., Saxe, J., Sipser, M.** *Parity, circuits, and the polynomial-time hierarchy.* Math. Systems Theory, 1984. — 独立给出 $\mathrm{PARITY} \notin \mathrm{AC}^0$。
7. **Razborov, A. A.** *Lower bounds on the monotone complexity of some Boolean functions.* Soviet Math. Doklady, 1985. — 单调电路下界的开创工作。
8. **Alon, N., Boppana, R. B.** *The monotone circuit complexity of Boolean functions.* Combinatorica 7(1), 1987. — CLIQUE 的指数级单调电路下界。
9. **Kannan, R.** *Circuit-size lower bounds and non-reducibility to sparse sets.* Information and Control, 1982. — 固定多项式规模的无条件下界。
10. **Karp, R., Lipton, R.** *Some connections between nonuniform and uniform complexity classes.* STOC 1980. — $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly} \Rightarrow \mathrm{PH}$ 坍缩。
11. **Nisan, N., Wigderson, A.** *Hardness vs randomness.* J. Comput. Syst. Sci. 49(2), 1994. — 困难性 ⟺ 伪随机性。
12. **Impagliazzo, R., Wigderson, A.** *P = BPP if E requires exponential circuits.* STOC 1997. — 上述桥梁的最强形式。
13. **Williams, R.** *Nonuniform ACC circuit lower bounds.* JACM 61(1), 2014（CCC 2011）. — 算法化下界，三十年来的实质突破。
14. **Find, M., Golovnev, A., Hirsch, E. A., Kulikov, A. S.** *A better-than-3n lower bound for the circuit complexity of an explicit function.* FOCS 2016. — 通用电路下界的最新记录之一。
15. **Mulmuley, K., Sohoni, M.** *Geometric complexity theory I / II.* SIAM J. Comput., 2001 / 2008. — GCT 纲领。
16. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 教材，第 6、14、22–24 章。
17. **Goldreich, O.** *Computational Complexity: A Conceptual Perspective.* Cambridge University Press, 2008. — 教材，对障碍的讨论清楚。

## 常见误区

- **误区：电路下界已被证明。** —— **错**。最新通用电路下界是 $3n - o(n)$ 的**线性**量级；真正需要的超多项式下界一个都没有。
- **误区：$3n - o(n)$ 已经很接近 $\mathrm{P} \neq \mathrm{NP}$ 了。** —— 从线性到超多项式是**量级**的差距，不是常数因子的差距。
- **误区：自然化障碍说明电路下界无法被证明。** —— **严重误读。** 它说明的是：**若**单向函数存在，**则**某一类特定技术失效。命题本身仍可真可假；且该定理本身以"单向函数存在"为**前提**，去掉前提即为错误陈述。
- **误区：单调电路下界可以推广到一般电路。** —— 不能。单调性是被用尽的资源；一旦允许否定，伪随机性出现，"难函数"的识别难度完全改变。
- **误区：Williams 的结果证明了 $\mathrm{P} \neq \mathrm{NP}$。** —— 它证明的是 $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$，而 $\mathrm{ACC}^0$ 是极弱的电路类，与 $\mathrm{P}/\mathrm{poly}$ 相去甚远。

## 可运行实验

**`experiments/circuit_min_size_small.py`** — 小规模精确电路规模与计数分布

对 $n = 2, 3, 4$ 的**全部**布尔函数，用穷举或 SAT/ILP 求出精确最小电路规模，绘制分布直方图。

- **能说明什么**：Shannon 计数论证的直观版本——"绝大多数函数都难"，这正是"广泛性"的经验来源。
- **不能说明什么**：$n \le 4$ 渐近信息量为零，不能给出任何下界；尤其**不能**用"随机函数都难"论证"显式函数也难"。

**`experiments/lower_bound_technique_toy.py`** — 观察统计判据为何在伪随机函数前失效

构造一个小型伪随机生成器，把输出解释为函数真值表；对若干看似合理的组合度量（真值表自相关、Walsh 谱、子函数计数）计算取值，与真随机函数比较。

- **能说明什么**：两者的这些统计度量几乎无法区分——**任何只依赖统计特征的判据都会被欺骗**，这是自然化障碍机制最直观的体感。
- **不能说明什么**：它不能证明任何下界或自然化障碍定理；把这种直觉当作证明是最常见的错误之一。

## 延伸阅读

- **入门**：Arora & Barak（文献 [16]）第 6 章（电路复杂性）与开放问题附录。
- **理解障碍**：Razborov & Rudich（文献 [1]）的引言与定理陈述——其引言本身就值得反复读。
- **当代突破**：Williams（文献 [13]）作为"算法化下界"的样板；对照 [#1 P vs NP](01-p-vs-np.md) 中对这一路线的讨论。
- **纲领性视角**：Mulmuley & Sohoni（文献 [15]）的引言，理解"为什么需要全新的数学工具"。
- **交叉引用**：[#1 P vs NP](01-p-vs-np.md)（电路下界是它的技术核心）；[#13 单向函数是否存在](13-one-way-functions.md)（自然化障碍的前提，与本题构成根本张力）；[#15 最小电路规模问题（MCSP）](15-mcsp.md)（本题的"元问题"）；[#16 时间受限 Kolmogorov 复杂性](16-time-bounded-kolmogorov.md)（另一族元复杂性问题）；[#3 P vs PSPACE](03-p-vs-pspace.md)（同受三重障碍限制的分离问题）。
