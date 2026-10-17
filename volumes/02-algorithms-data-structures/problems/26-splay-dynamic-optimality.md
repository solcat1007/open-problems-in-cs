# #26 Splay 树的动态最优性

**状态**：`OPEN`
**领域**：算法与数据结构
**首次提出**：Sleator 与 Tarjan，1985（*Self-Adjusting Binary Search Trees*, J. ACM）
**参与门槛**：需要新的数学工具

---

## 一句话概述

Splay 树每次访问后把被访问结点"伸展"到根，没有任何平衡规则。猜想说：**对任意访问序列，它的总代价都在最优二叉搜索树算法的常数倍之内**——这个猜想四十年未解，且连一个常数竞争比都还无人做到。

## 形式化陈述

先把**二叉搜索树（BST）模型**说清楚——猜想的精确含义完全取决于它。

- 树存放 $n$ 个有序键。
- **访问**键 $x$ 的代价是根到 $x$ 的路径长度加一，即 $d(x) + 1$。
- 两次访问之间，算法可以做**任意多次旋转**，每次旋转代价为 $1$。
- 对长度 $m$ 的访问序列 $X = \langle x_1, \dots, x_m \rangle$，记算法 $A$ 的总代价为 $A(X)$。
- 令
$$\mathrm{OPT}(X) \;=\; \min_{A} A(X),$$
其中 $A$ 遍历**所有** BST 算法，且允许它**离线**——即提前看到整个序列 $X$。

**动态最优性猜想（Sleator–Tarjan, 1985）**：

> 存在常数 $c$，使得对**所有** $n$ 与**所有**访问序列 $X$，
> $$\mathrm{cost}_{\text{splay}}(X) \;\le\; c \cdot \mathrm{OPT}(X) + O(n).$$

用竞争分析（competitive analysis）的语言：splay 树是 $O(1)$-**竞争的**（$O(1)$-competitive）。注意三点：量词是"对所有序列、对所有算法"；比较的对手是**允许旋转的最优树**，而不是静态树；加性项 $O(n)$ 用于抹平初始树的差异（把任意树旋转成另一棵树的代价是 $O(n)$）。

## 为什么困难

**第一，量词结构决定了它无法被"单点攻击"。** 猜想要求一个"对所有序列、对所有算法"成立的不等式；标准套路是找可计算下界 $\mathrm{LB}(X) \le \mathrm{OPT}(X)$ 再证算法代价 $\le c\cdot\mathrm{LB}(X)$，成败取决于下界能否抓住 $\mathrm{OPT}$。而这里的下界恰恰抓不住（见第三条）。

**第二，$\mathrm{OPT}$ 本身难以刻画。** 最优动态树策略依赖未来访问且允许任意旋转；计算 $\mathrm{OPT}(X)$ 本身就是课题，我们只有几个可计算下界函数，没有紧表达式。

**第三，最自然的工具（access lemma）在原理上不足以给出常数竞争比。** Access lemma 说的是：按权重 $w$ 定义秩 $r(x) = \log_2 (W / w(x))$（$W$ 为总权重），则

$$\text{splay}(x) \text{ 的摊销代价} \;\le\; 3\big(r(\text{root}) - r(x)\big) + 1 \;=\; O\!\left(\log \frac{W}{w(x)}\right).$$

这是一切"自适应界"的证明工具：选不同权重，它分别推出**静态最优性**、**工作集界**、**扫描定理**、**动态指纹界**（Cole 等，2000）、**key-independent optimality**（Iacono，2002）等。但 access lemma 的势函数只描述 splay 自身状态、不跟踪最优树在访问间的旋转，而 $\mathrm{OPT}$ 定义恰恰允许对手旋转。取等权权重时只给 $O(\log n)$ 量级、竞争比 $O(\log n)$，距常数甚远——它是证明部分结果的工具，不是通向猜想的道路。

**第四，最著名的下界（Wilber 界）与 $\mathrm{OPT}$ 之间存在真实缝隙。** Wilber（1989）给出 Wilber-1/Wilber-2，满足 $\mathrm{WB}(X) \le \mathrm{OPT}(X)$；最常用变体是 **interleave 界**（交换访问左/右子树的次数）。Tango 树贴着 interleave 界达到 $O(\log\log n)$ 竞争比，说明它只差 $O(\log\log n)$ 倍且不可能更紧。Lecomte 与 Weinstein（ESA 2020）进一步给出 $\Omega(\log\log n)$ 的分离结果 `[待核实]`：具体分离常数与表述。结论：任何只依赖 interleave 界的分析都不可能证明动态最优性，此路已堵死。

**第五，竞争者稀少。** 除 splay 外，已知达 $O(\log\log n)$ 的结构（tango、multi-splay trees）都不满足 splay 满足的某些性质（如扫描定理），无法反过来支撑猜想。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（证明工具） | **Access lemma**：splay 的摊销代价 $\le 3(r(\text{root}) - r(x)) + 1$ | Sleator & Tarjan, 1985 |
| 上界（自适应界） | 静态最优性、工作集界、扫描定理（顺序访问总代价 $O(n)$）、动态指纹界、key-independent optimality | Sleator & Tarjan, 1985；Tarjan, 1985；Cole 等, 2000；Iacono, 2002 |
| 上界（竞争比，**非 splay**） | **tango**：$O(\log\log n)$ 竞争比，且该分析对 interleave 界是紧的 | Demaine 等, FOCS 2004（*Dynamic Optimality—Almost*） |
| 上界（竞争比，**非 splay**） | **multi-splay trees**：$O(\log\log n)$ 竞争比，且满足平衡定理与扫描定理 | Wang, Derryberry & Sleator, 2006 |
| 上界（竞争比，**splay 本身**，最新） | splay 树的**首个 $o(\log n)$ 竞争比**：$\tilde{O}(\log\log n)$；同时把 split 猜想证到 $\tilde{O}(\log\log n)$ 因子内 | 预印本 arXiv:2607.18498, 2026 `[待核实]`：作者与发表信息 |
| 下界（对 $\mathrm{OPT}$ 的界） | Wilber-1 / Wilber-2 界 $\le \mathrm{OPT}(X)$；interleave 界与 $\mathrm{OPT}$ 有 $\Omega(\log\log n)$ 分离 | Wilber, 1989；Lecomte & Weinstein, ESA 2020 `[待核实]` |
| 下界（对竞争比） | **无任何 BST 已知达到 $O(1)$ 竞争比**；十余年间最好为 $O(\log\log n)$ | Demaine 等, 2004 及其后续 |
| 未解推论 | Traversal 猜想、Deque 猜想（splay 已知在 $\alpha(n)$、$\alpha^*(n)$ 因子内）、Split 猜想 | Sleator & Tarjan, 1985；Sundar；Pettie, 2008 |

**读表要点**：第 1–5 行是**上界**，第 6–7 行是**下界**（对 $\mathrm{OPT}$ 的估计、"无人达常数竞争比"）。强调：表中无一行说猜想"已成立"或"已推翻"；竞争比从 $O(\log n)$（平凡）到 $O(\log\log n)$（已知最好）不等于 $O(1)$。2026 年结果把 splay 推进到 $\tilde{O}(\log\log n)$，仍非常数。

## 解法现状与可行攻击路径

### 已解决的部分

- **splay 的一族部分性质**：静态最优性、工作集界、扫描定理（顺序访问总代价 $O(n)$）、动态指纹界（Cole 等, 2000）、key-independent optimality（Iacono, 2002）均已被证明——它们是 access lemma 及其扩展的直接推论。
- **"逼近 OPT"的 BST 结构存在**：tango（$O(\log\log n)$ 竞争比，Demaine 等, FOCS 2004）与 multi-splay trees（$O(\log\log n)$，且满足平衡定理与扫描定理，Wang–Derryberry–Sleator, 2006）——"能否逼近最优"在非 splay 结构上答案为肯定（但仍非常数）。
- **推论性猜想的近似版本**：Deque 猜想对 splay 已知在 $\alpha^*(n)$ 因子内（Pettie, 2008）；Split 猜想被证到 $\tilde{O}(\log\log n)$ 因子内（2026 预印本 `[待核实]`）。
- **splay 本身的首个 $o(\log n)$ 竞争比**：$\tilde{O}(\log\log n)$（2026 预印本 `[待核实]`）——突破平凡 $O(\log n)$ 的第一步，但仍非常数。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 改进 Wilber 界 | 让下界更贴近 $\mathrm{OPT}$ | interleave 界是最常用变体 | 已被证明封顶（见"已堵死的路径"） |
| 绕开下界，直接对 $\mathrm{OPT}$ 记账 | 把势函数直接定义在最优树深度上，使算法与对手可比 | 2026 年工作走此路，得到 $\tilde{O}(\log\log n)$ 竞争比 | 分析异常繁重，因子尚未压到常数 |
| 先证明推论 | 逐条攻 Deque、Traversal、Split 等必要条件 | Split 到 $\tilde{O}(\log\log n)$；Deque 到 $\alpha^*(n)$ | 均未彻底解决，未收敛到常数因子 |
| 拓展模型 | 在更强/更弱对手下重述猜想 | 模型区分已被澄清 | 弱模型下成立不推出原猜想；强模型下若仍成立反而暗示猜想过强 |

### 已堵死的路径

- **只依赖 interleave（Wilber）界的分析**：tango 贴着 interleave 界达到 $O(\log\log n)$，而 Lecomte–Weinstein（ESA 2020 `[待核实]`）给出 interleave 界与 $\mathrm{OPT}$ 的 $\Omega(\log\log n)$ 分离——任何只靠这一界的分析都封顶在 $O(\log\log n)$ 竞争比，**不可能证明动态最优性**。
- **access lemma 作为通向常数竞争比的工具**：其势函数只描述 splay 自身状态、不跟踪最优树在访问之间的旋转，取等权权重时只给 $O(\log n)$ 量级——在原理上不足以给出常数竞争比；它是证明部分结果的工具，不是通向猜想的道路。

### 裁决

**路径已知，尚需突破**

主攻方向明确（直接对 $\mathrm{OPT}$ 记账，2026 年已把 splay 推进到 $\tilde{O}(\log\log n)$），且不可行的路线（Wilber 界路线、access lemma 路线）已被明确识别；硬卡点是把竞争比从 $\tilde{O}(\log\log n)$ 压到常数。

## 研究路线图

**路线一：改进 Wilber 界。** 让下界更贴近 $\mathrm{OPT}$。**已被证明不可行**：interleave 界与 $\mathrm{OPT}$ 的分离是 $\Omega(\log\log n)$，任何只靠这一界的分析都封顶在 $O(\log\log n)$ 竞争比。

**路线二：绕开下界，直接对 $\mathrm{OPT}$ 记账。** 把 splay 的势函数直接定义在**最优树的深度**上使二者可比。2026 年的工作正是走这条路（用最优树中的深度定义秩，在 splay 中定义朝向最优树根的重路径，复用 pairing heap 分析技术数 zig-zig 次数），是当前最有希望的方向，但分析异常繁重、因子未压到常数。

**路线三：先证明推论。** Deque、Traversal、Split 猜想都是动态最优性的必要条件。现状：Deque 对 splay 已知在 $\alpha^*(n)$ 因子内（Pettie, 2008），未彻底解决；Split 在 2026 年结果中被证到 $\tilde{O}(\log\log n)$ 因子内。

**路线四：拓展模型。** 在更强（允许对手也看到随机性）或更弱的对手下重述猜想。卡点：弱模型下成立不推出原猜想；强模型下若仍成立反而暗示猜想过强。

## 关键文献

1. **Sleator, D. D., Tarjan, R. E.** *Self-Adjusting Binary Search Trees.* J. ACM 32(3), 1985. — splay 树的原始论文，动态最优性猜想、access lemma、静态最优性与工作集界的出处。
2. **Sleator, D. D., Tarjan, R. E.** *Amortized Efficiency of List Update and Paging Rules.* Commun. ACM 28(2), 1985. — "移到前端"是 2-竞争的（猜想的动机类比）。
3. **Tarjan, R. E.** 顺序访问定理（扫描定理），1985. — 顺序访问 $n$ 个键总代价 $O(n)$。
4. **Cole, R. 等** 动态指纹定理，2000. — 访问相邻键摊销代价 $O(\log(d+1))$，access lemma 之外的新工具。
5. **Wilber, R.** *Lower Bounds for Accessing Binary Search Trees with Rotations.* SIAM J. Comput., 1989. — 两个经典下界，竞争比分析的基础。
6. **Demaine, E., Harmon, D., Iacono, J., Patrascu, M.** *Dynamic Optimality—Almost.* FOCS 2004. — tango 树，$O(\log\log n)$ 竞争比。
7. **Wang, C. C., Derryberry, J., Sleator, D. D.** *O(log log n)-Competitive Dynamic Binary Search Trees.* SODA 2006. — multi-splay trees。
8. **Lecomte, V., Weinstein, O.** 关于 interleave 界与 $\mathrm{OPT}$ 的 $\Omega(\log\log n)$ 分离，ESA 2020. — 说明只靠 interleave 界的路线已封顶。`[待核实]`：具体标题。
9. **Pettie, S.** 关于 splay 树 Deque 性质的改进界 $\alpha^*(n)$，2008. — `[待核实]`：具体出处。
10. **arXiv:2607.18498.** *Splay trees are almost dynamically optimal.* 2026. — 首个针对 splay 本身的 $o(\log n)$ 竞争比。`[待核实]`：作者与发表信息。

## 常见误区

- **误区："splay 树已被证明是动态最优的。"** —— 没有。这是**猜想**，四十年未解。任何把它当定理引用的写法都是错的。

- **误区："access lemma 就是动态最优性的证明。"** —— 完全不是。Access lemma 只给摊销 $O(\log n)$ 上界并派生静态最优性、工作集界等；其势函数不刻画最优树旋转，原理上给不出常数竞争比。它是工具不是答案——本问题上最流行也最有害的误解。

- **误区："摊销 $O(\log n)$ 已经是理论上限。"** —— 对**静态**最优树是这样，对**动态**最优树不是。存在访问序列使 $\mathrm{OPT}(X) = O(m)$（例如顺序访问全部键），此时 $O(\log n)$ 摊销是次优的。

- **误区："静态最优性蕴含动态最优性。"** —— 静态最优性只与**不允许旋转**的最优树比较。动态最优性的对手可**任意旋转**，是更强的对手。

- **误区："tango 树证明了猜想。"** —— tango 达到 $O(\log\log n)$，是**非**常数；而且 tango 不满足 splay 满足的扫描定理，因此不能作为猜想的支撑。

- **误区："我在自己机器上跑，splay 比红黑树快，所以猜想成立。"** —— 实测性能受常数、内存与实现影响，与竞争比这一渐近命题无关；有限序列上较快**不构成**"对所有序列成立"的证据。

- **误区："找到一个 splay 表现很差的反例就推翻了猜想。"** —— 反例必须同时是 $\mathrm{OPT}$ 的**下界**（即任何 BST 算法在该序列上也不快），否则只说明 splay 在该序列上不如另一棵树，与猜想无关（参见 [#1 P vs NP](../../01-complexity-theory/problems/01-p-vs-np.md) 的"具体实例难 ≠ 问题本身难"）。

## 可运行实验

**`experiments/splay_vs_bst.py`** — 在一组结构化访问序列上对比多种 BST

脚本实现四种树，全部记录**同一口径**的代价（访问路径长度 + 旋转次数）：

1. **splay 树**（自底向上，zig / zig-zig / zig-zag）；
2. **平衡树**（AVL 或红黑树）作为"总是 $O(\log n)$"的对照；
3. **静态最优 BST**（用 Knuth 的 DP 按已知访问频率构造），作为**静态**最优的基准；
4. 可选：**tango 风格**的简化结构，用于观察 $O(\log\log n)$ 竞争比的存在性（实现完整 tango 较复杂，可只做骨架）。

访问序列生成器覆盖：顺序（$1,2,\dots,n$）、逆序、随机、**工作集**（在一小撮键内反复访问）、**滑动窗口/动态指纹**、**两端交替**（deque 式）。

你会观察到：顺序序列上 splay 总代价接近线性（扫描定理的实测影子）；工作集序列上显著优于平衡树；两端交替序列上它与平衡树的差距比静态最优基准大得多。这些差异**正是**猜想所预言的行为。

**这个实验不能说明什么**（重要）：它**不能**验证竞争比（需与最优离线算法 $\mathrm{OPT}$ 比较，而 $\mathrm{OPT}$ 无法在实验中求出，静态最优树只是下界候选）；**不能**用"某序列上 splay 更好/更差"来支持或否定猜想——那需要关于**所有**序列与**所有**算法的论证；有限长度序列无法暴露渐近竞争比。

**`experiments/wilber_interleave_bound.py`** — 计算 interleave 下界并测量缝隙

实现 Wilber 的 interleave 界：固定一棵完美 BST $P$，统计序列在左右子树间切换次数，与 splay 实际代价并列画出随 $m$ 的曲线，观察二者比例随 $m$ 缓慢增长（$\log\log n$ 量级的影子），从而理解"贴着 interleave 界"为何无法通向常数竞争比。

## 延伸阅读

- **原始论文**：Sleator & Tarjan (1985)，先读 access lemma 与静态最优性两节，再读猜想陈述；其链表更新与分页规则（"移到前端"是 2-竞争的）是猜想的动机类比。
- **综述**：Iacono 关于动态最优性猜想的综述（*In Pursuit of the Dynamic Optimality Conjecture*）`[待核实]`：具体出处与年份。
- **相关档案**：[#1 P vs NP](../../01-complexity-theory/problems/01-p-vs-np.md)（"具体实例 vs 问题本身"方法论母题）、[#30 精确算法的指数时间下界](30-exponential-time-lower-bounds.md)（"全称量词下的最优性"如何成为证明难点）、[#21 TSP 的细粒度下界](21-tsp-fine-grained.md)（"某经典算法是否已最优"问题家族）。
