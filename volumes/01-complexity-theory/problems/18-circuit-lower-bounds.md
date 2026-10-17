# #18 电路下界问题

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论（电路复杂性）
**首次提出**：研究可追溯到 Shannon 的计数论证（1949）；现代形式的电路下界问题在 1970 年代随复杂度类理论确立
**参与门槛**：需要新的数学工具

---

## 一句话概述

能否证明：**任何**多项式规模电路都算不出某个**可显式写出**的布尔函数（如判断图是否含三角形）？做不到，便无法排除 $\mathrm{P} = \mathrm{NP}$。

## 形式化陈述

**电路模型**：布尔电路是由与非门（或任意完备基）构成的有向无环图，$n$ 个输入位、一个输出位；"**规模**"指门数。

对函数 $s : \mathbb{N} \to \mathbb{N}$：

$$\mathrm{SIZE}(s(n)) = \{L : L \text{ 可由规模 } O(s(n)) \text{ 的电路族判定}\}, \qquad \mathrm{P}/\mathrm{poly} = \bigcup_{k \ge 1} \mathrm{SIZE}(n^k)$$

$\mathrm{P}/\mathrm{poly}$ 是**非一致**类：每个输入长度可用不同电路，无需统一生成算法，故 $\mathrm{P} \subseteq \mathrm{P}/\mathrm{poly}$。

**核心问题**：是否存在**显式** $f$，对**每个**常数 $k$ 都有 $f \notin \mathrm{SIZE}(n^k)$？最强目标是

$$\mathrm{NP} \nsubseteq \mathrm{P}/\mathrm{poly}$$

它**蕴含** $\mathrm{P} \neq \mathrm{NP}$（因 $\mathrm{P} \subseteq \mathrm{P}/\mathrm{poly}$），故更强更难；反向不成立——可有 $\mathrm{P} \neq \mathrm{NP}$ 而 $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly}$。

两条结构性结论：**Karp–Lipton（1982）**：$\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly}$ 蕴含多项式层级坍缩到 $\Sigma_2$；**Kannan（1982）**：对**每个固定的** $k$，$\Sigma_2^P \nsubseteq \mathrm{SIZE}(n^k)$（无条件，但仅对固定多项式规模）。二者合起来即技术边界：能证"对每个固定 $k$ 都有函数难"，不能证"存在对所有 $k$ 都难的函数"。

## 为什么困难

一句话：**主要敌人是自然化障碍，其张力是——证明电路下界的能力，与密码学能否存在，相互排斥。**

### 一、相对化障碍不适用于电路下界（必须澄清的区别）

**相对化障碍**（Baker–Gill–Solovay 1975）："对一切神谕成立"的技术无法证明 $\mathrm{P} \neq \mathrm{NP}$——存在 $A$ 使 $\mathrm{P}^A = \mathrm{NP}^A$，也存在 $B$ 使 $\mathrm{P}^B \neq \mathrm{NP}^B$。

电路下界**不在此列**：已知下界证明都是**非相对化**的——若给 $\mathrm{AC}^0$ 加上能算 PARITY 的神谕门，$\mathrm{PARITY} \notin \mathrm{AC}^0$ 立刻失效。真正相关的是**自然化障碍**（及更广的**代数化障碍**）。

### 二、自然化障碍的机制：构造性 + 广泛性 ⟹ 与伪随机性冲突

称性质 $\mathcal{P}$ **自然**，若：(1) **构造性**：给定真值表（$2^n$ 位）可在 $2^{O(n)}$ 时间判定 $f \in \mathcal{P}$；(2) **广泛性**：$\Pr_f[f \in \mathcal{P}] \ge 1/\mathrm{poly}(2^n)$。

再设 $\mathcal{P}$ **有用**：$f \in \mathcal{P}$ ⟹ $f$ 需超多项式规模电路，即想要的"难函数"判据。

**定理（Razborov–Rudich 1997）**：若存在伪随机生成器（等价于单向函数，见 [#13](13-one-way-functions.md)），则**不存在**同时满足三性的 $\mathcal{P}$。

骨架：$D$ 读入 $2^n$ 位串 $w$（真值表），输出 $[w \in \mathcal{P}]$。$w$ 真随机时由**广泛性**以不可忽略概率输出 1；$w$ 伪随机时（短种子经小电路算出）作为函数"简单"，由**有用性**输出 0。故 $D$ 以不可忽略优势区分真/伪随机，矛盾。**它不断言下界不可证，而是说"用可有效检查的组合性质捕捉难函数"须以放弃伪随机性为代价**——伪随机性等价于单向函数，即现代密码学地基。

### 三、与密码学存在性的根本张力

> **要么接受密码学存在（放弃"自然的"技术，只能找"非自然"技术），要么放弃密码学（可尽情使用组合计数）。**

纯数学的技术问题与被广泛依赖的安全基础**互相排斥**。

方向须注意：该定理以"单向函数存在"为**前提**；前提成立则障碍生效，不成立（密码学全灭）则失效、组合计数重新可用。两者都**不能**推出"下界不可能被证明"——障碍限制**技术**，不是命题真假。

### 四、三个障碍的关系

| 障碍 | 出处 | 针对什么 | 对电路下界是否适用 |
|---|---|---|---|
| 相对化 | Baker–Gill–Solovay 1975 | 神谕无关的证明技术 | **不适用**：电路下界证明本身是非相对化的 |
| 自然化 | Razborov–Rudich 1997 | 构造性 + 广泛性的组合技术 | **直接适用**：本题最主要的障碍 |
| 代数化 | Aaronson–Wigderson 2009 | 允许低次多项式扩张的技术 | 限制 P vs NP 分离；对电路下界的约束取决于技术是否"代数化" [待核实：本档案未核对代数化框架对 Williams 型技术的判定] |

一句话：**相对化封锁了 1970 年代的对角化工具，自然化封锁了 1980–90 年代的组合计数工具，代数化封锁了"用交互式证明与代数方法绕过前两者"的希望。** 战场在第二层。

### 五、为什么至今没有可行的"非自然"路线

两条出路都受阻：

- **放弃构造性**：性质不可判定时，证明失去可验证的组合内容。Kannan（1982）的无条件下界正用（非构造的）对角化，故不与障碍冲突，但无法扩展至一般电路。
- **放弃广泛性**：只对特定函数成立的性质须能"瞄准"该函数，而随机函数（下界主要对象）不受约束；已知非自然下界仅覆盖极弱模型。

另注：$\mathrm{AC}^0$ 与单调电路下界（Håstad 1986；Razborov 1985；Alon–Boppana 1987）虽"自然"却不冲突——两模型算不了伪随机函数，前提不成立。

### 六、算法化下界

Williams（2011/2014）的**算法化下界**：先给某电路类中 SAT 的非平凡加速算法，再推出下界，证 $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$。它**不是**"定义性质并检查所有小电路函数"，故形式上不落入 Razborov–Rudich 框架；究竟规避构造性还是广泛性，文献表述有别 [待核实：两种框架下的具体归属]，本仓库 [#1](01-p-vs-np.md) 采"不满足广泛性"。**卡点在算法侧**：$\mathrm{TC}^0$、$\mathrm{NC}^1$ 或一般多项式规模电路所需的快 SAT 算法尚不存在。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（已知小电路） | PARITY 有 $O(n)$ 规模电路；加法、乘法有近线性规模电路 | 标准构造 |
| 下界（通用电路） | 存在显式函数需要 $\ge 3n - o(n)$ 规模电路（精确常数形式如 $(3+1/86)n - o(n)$） | Find–Golovnev–Hirsch–Kulikov 2016 |
| 下界（常数改进） | 后续工作可能改进了该常数 **[待核实：未核对最新常数与其出处]** | — |
| 下界（$\mathrm{AC}^0$） | $\mathrm{PARITY} \notin \mathrm{AC}^0$（任意常数深度） | Ajtai 1983；Furst–Saxe–Sipser 1984；Håstad 1986 |
| 下界（单调电路） | CLIQUE 需要指数级单调电路规模 | Razborov 1985；Alon–Boppana 1987 |
| 下界（$\mathrm{ACC}^0$） | $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$（非一致） | Williams 2011 / 2014 |
| 下界（固定多项式规模） | 对每个固定的 $k$，$\Sigma_2^P \nsubseteq \mathrm{SIZE}(n^k)$（无条件） | Kannan 1982 |
| 结构性 | $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly} \Rightarrow \mathrm{PH} = \Sigma_2$ | Karp–Lipton 1982 |
| 结构性 | 存在 $\mathrm{E}$ 中需 $2^{\Omega(n)}$ 规模电路的函数 ⟺ 某类伪随机生成器存在 | Nisan–Wigderson 1994；Impagliazzo–Wigderson 1997 |
| 条件性 | 若单向函数存在，则任何"自然的"组合技术都不能证明电路下界 | Razborov–Rudich 1997 |

区分：**上界**是"存在小电路"，**下界**是"任何电路都做不到"。通用下界最新记录为 **$3n - o(n)$，线性量级**，所需是**超多项式**——差距在**量级**非常数因子；说它"接近 $\mathrm{P} \neq \mathrm{NP}$"是严重误读。

## 解法现状与可行攻击路径

### 已解决的部分

- **AC⁰**：PARITY ∉ AC⁰（Ajtai 1983；Furst–Saxe–Sipser 1984；Håstad 1986 开关引理），任意常数深度成立。
- **单调电路**：CLIQUE 需指数级单调电路规模（Razborov 1985；Alon–Boppana 1987）。两者"自然"却不与障碍冲突，因模型算不了伪随机函数。
- **ACC⁰**：NEXP ⊄ ACC⁰（Williams 2011/2014，算法化下界）。
- **固定多项式规模**：对每个固定的 $k$，$\Sigma_2^P \nsubseteq \mathrm{SIZE}(n^k)$（Kannan 1982；非构造对角化，故不与自然化冲突）。
- **通用电路**：存在显式函数需 $\ge 3n - o(n)$ 规模（Find–Golovnev–Hirsch–Kulikov 2016）——但是**线性量级**，距超多项式是量级差距。
- **结构性刻画**：NP ⊆ P/poly ⟹ PH = Σ₂（Karp–Lipton 1982）；E 中需 $2^{\Omega(n)}$ 规模电路的函数 ⟺ 某类伪随机生成器存在（Nisan–Wigderson 1994；Impagliazzo–Wigderson 1997）。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 算法化下界（Williams 路线） | 先为电路类 $C$ 找快 SAT 算法，再推出 NEXP ⊄ C | 对 ACC⁰ 成功 | 对更强电路类，所需 SAT 算法等价于更强的下界，形成循环 |
| 非自然证明技术 | 有意放弃构造性或广泛性 | 只在极弱模型有效 | 前者失去组合内容，后者难以覆盖随机函数 |
| 几何复杂性理论（GCT） | Mulmuley–Sohoni 用代数几何与表示论分离代数复杂性类（VP vs VNP） | 纲领能预测自己会遇到的障碍 | 尚未产生任何无条件下界，障碍理论远未成熟 |
| 电路类分层推进 | AC⁰ → ACC⁰ → TC⁰ → NC¹ → P/poly 逐层攻克 | 前两层已解决，ACC⁰ 被 Williams 攻克 | TC⁰ 及以上是开放前沿，每层都要重写技术，没有统一迁移机制 |

### 已堵死的路径

- **自然化**（Razborov–Rudich 1997）：若单向函数存在，则不存在同时满足"构造性 + 广泛性 + 有用性"的性质——一切"自然的"组合计数技术被成体系排除，且与密码学存在性排斥。
- **两条理论出路各自受阻**：放弃构造性则失去可验证的组合内容（Kannan 型对角化无法扩展）；放弃广泛性则须"瞄准"特定函数，而随机函数不受约束。
- **相对化**：对电路下界**不适用**，真正战场在自然化一层；代数化的精确约束范围 [待核实：本档案未核对代数化框架对 Williams 型技术的判定]。

### 裁决

**`原理上受限`**

自然化障碍直接排除最主要的证明技术，并以"密码学是否存在"为代价形成根本张力；通用下界仍停留 $3n - o(n)$ 的线性量级，与超多项式所需相差量级而非因子。

## 研究路线图

**路线一：算法化下界。** 先为 $C$ 找快 SAT 算法，再推出 $\mathrm{NEXP} \nsubseteq C$。现状：$\mathrm{ACC}^0$ 成功；**卡点**：更强类所需的 SAT 算法等价于更强的下界，形成循环。

**路线二：非自然证明技术。** 放弃构造性或广泛性。现状：只在极弱模型有效；**卡点**：前者失去组合内容，后者难覆盖随机函数。

**路线三：几何复杂性理论（GCT）。** Mulmuley–Sohoni（2001 / 2007）以代数几何与表示论分离代数复杂性类（如 $\mathrm{VP}$ vs $\mathrm{VNP}$）。现状：能预测自身障碍，**尚无任何无条件下界**，障碍理论未成熟。

**路线四：分层推进。** $\mathrm{AC}^0 \to \mathrm{ACC}^0 \to \mathrm{TC}^0 \to \mathrm{NC}^1 \to \mathrm{P}/\mathrm{poly}$。现状：前两层与 $\mathrm{ACC}^0$（Williams）已攻克，$\mathrm{TC}^0$ 以上为开放前沿；**卡点**：每层都要重写技术。

**哪条路被堵死？** 满足"构造性 + 广泛性"的组合计数技术（Razborov–Rudich 1997）。

## 关键文献

1. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 自然化障碍。
2. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍出处。
3. **Aaronson, S., Wigderson, A.** *Algebrization: A New Barrier in Complexity Theory.* ACM Trans. Comput. Theory 1(1), 2009. — 代数化障碍。
4. **Håstad, J.** *Almost optimal lower bounds for small depth circuits.* STOC 1986. — $\mathrm{AC}^0$ 下界（开关引理）。
5. **Ajtai, M.** *$\Sigma^1_1$-formulae on finite structures.* Annals of Pure and Applied Logic, 1983. — $\mathrm{PARITY} \notin \mathrm{AC}^0$ 的早期证明之一。
6. **Furst, M., Saxe, J., Sipser, M.** *Parity, circuits, and the polynomial-time hierarchy.* Math. Systems Theory, 1984. — 独立给出 $\mathrm{PARITY} \notin \mathrm{AC}^0$。
7. **Razborov, A. A.** *Lower bounds on the monotone complexity of some Boolean functions.* Soviet Math. Doklady, 1985. — 单调电路下界开创工作。
8. **Alon, N., Boppana, R. B.** *The monotone circuit complexity of Boolean functions.* Combinatorica 7(1), 1987. — CLIQUE 的指数级单调下界。
9. **Kannan, R.** *Circuit-size lower bounds and non-reducibility to sparse sets.* Information and Control, 1982. — 固定多项式规模的无条件下界。
10. **Karp, R., Lipton, R.** *Some connections between nonuniform and uniform complexity classes.* STOC 1980. — $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly} \Rightarrow \mathrm{PH}$ 坍缩。
11. **Nisan, N., Wigderson, A.** *Hardness vs randomness.* J. Comput. Syst. Sci. 49(2), 1994. — 困难性 ⟺ 伪随机性。
12. **Impagliazzo, R., Wigderson, A.** *P = BPP if E requires exponential circuits.* STOC 1997. — 上述桥梁的最强形式。
13. **Williams, R.** *Nonuniform ACC circuit lower bounds.* JACM 61(1), 2014（CCC 2011）. — 算法化下界的实质突破。
14. **Find, M., Golovnev, A., Hirsch, E. A., Kulikov, A. S.** *A better-than-3n lower bound for the circuit complexity of an explicit function.* FOCS 2016. — 通用电路下界最新记录之一。
15. **Mulmuley, K., Sohoni, M.** *Geometric complexity theory I / II.* SIAM J. Comput., 2001 / 2008. — GCT 纲领。
16. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 教材，第 6、14、22–24 章。
17. **Goldreich, O.** *Computational Complexity: A Conceptual Perspective.* Cambridge University Press, 2008. — 教材。

## 常见误区

- **误区：电路下界已被证明。** —— 最新通用下界仅 $3n - o(n)$ 的**线性**量级；超多项式下界一个都没有。
- **误区：$3n - o(n)$ 已很接近 $\mathrm{P} \neq \mathrm{NP}$。** —— 从线性到超多项式是**量级**差距，非常数因子。
- **误区：自然化障碍说明电路下界无法被证明。** —— **严重误读。** 它说的是：**若**单向函数存在，**则**某类技术失效；命题仍可真可假，去掉前提即成错误陈述。
- **误区：单调电路下界可推广到一般电路。** —— 不能。单调性已被用尽；一旦允许否定，伪随机性出现，"难函数"识别完全改变。
- **误区：Williams 的结果证明了 $\mathrm{P} \neq \mathrm{NP}$。** —— 它证的是 $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$，而 $\mathrm{ACC}^0$ 极弱，与 $\mathrm{P}/\mathrm{poly}$ 相去甚远。

## 可运行实验

**`experiments/circuit_min_size_small.py`** — 小规模精确电路规模与计数分布

对 $n=2,3,4$ 的**全部**布尔函数，穷举或 SAT/ILP 求精确最小电路规模并绘分布。

- **能说明**：Shannon 计数论证的直观版——"绝大多数函数都难"，即广泛性的经验来源。
- **不能说明**：$n\le4$ 渐近信息为零；**不能**由"随机函数都难"推出"显式函数也难"。

**`experiments/lower_bound_technique_toy.py`** — 观察统计判据为何在伪随机函数前失效

构造小型伪随机生成器，输出即真值表；对若干组合度量（自相关、Walsh 谱、子函数计数）与真随机函数比较。

- **能说明**：两者几乎无法区分——**只依赖统计特征的判据都会被欺骗**。
- **不能说明**：不能证明任何下界或障碍定理；把直觉当作证明是最常见的错误。

## 延伸阅读

- **入门**：Arora & Barak（文献 [16]）第 6 章与开放问题附录。
- **理解障碍**：Razborov & Rudich（文献 [1]）引言与定理陈述。
- **当代突破**：Williams（文献 [13]）"算法化下界"样板。
- **纲领视角**：Mulmuley & Sohoni（文献 [15]）引言。
- **交叉引用**：[#1 P vs NP](01-p-vs-np.md)（技术核心）；[#13 单向函数](13-one-way-functions.md)（自然化前提）；[#15 MCSP](15-mcsp.md)（"元问题"）；[#16 时间受限 Kolmogorov](16-time-bounded-kolmogorov.md)（另一族元复杂性）；[#3 P vs PSPACE](03-p-vs-pspace.md)（同受三重障碍限制）。
