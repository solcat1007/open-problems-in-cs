# #4 NC vs P

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论
**首次提出**：1970 年代末至 1980 年代初，随并行计算模型与 P 完全性理论出现（Pippenger 1979；Ladner 1975）
**参与门槛**：需要新的数学工具

---

## 一句话概述

一个能在**多项式时间**内串行解决的问题，是否一定能在**极短时间**内用大量并行处理器解决？

## 形式化陈述

**并行类 NC**：$\mathrm{NC} = \bigcup_{k \geq 1} \mathrm{NC}^k$，其中 $\mathrm{NC}^k$ 由一族布尔电路 $\{C_n\}$ 定义，满足

- **多项式规模**：$|C_n| \leq \mathrm{poly}(n)$；
- **多对数深度**：$\mathrm{depth}(C_n) = O(\log^k n)$；
- 扇入为 2，且电路族是**一致的**（uniform，通常取对数空间一致），即电路本身可由对数空间机器生成。

深度对应**并行时间**，规模对应**总工作量**。因此 NC 直觉上正是"可被高效并行化"的问题类。

**问题**：$\mathrm{NC} \overset{?}{=} \mathrm{P}$

有包含链

$$\mathrm{AC}^0 \subsetneq \mathrm{ACC}^0 \subseteq \mathrm{TC}^0 \subseteq \mathrm{NC}^1 \subseteq \mathrm{L} \subseteq \mathrm{NL} \subseteq \mathrm{NC}^2 \subseteq \cdots \subseteq \mathrm{NC} \subseteq \mathrm{P}$$

其中 L、NL 是对数空间类，$\subseteq \mathrm{P}$ 是已知的（每个多项式规模的多对数深度电路都能被多项式时间机器逐层求值）。

**完全问题的等价刻画**：若某个 **P 完全**问题（在**对数空间归约**下）属于 NC，则 $\mathrm{NC} = \mathrm{P}$。最经典的 P 完全问题是**电路值问题 CVP（Circuit Value Problem）**：给定一个布尔电路与输入，求输出。因此

> $\mathrm{NC} = \mathrm{P}$ 当且仅当 $\mathrm{CVP} \in \mathrm{NC}$。

这给出一个具体的、看起来"天生串行"的候选问题族。

## 为什么困难

### （一）相对化障碍

取 $A$ 为一个 P 完全集。可以构造使 $\mathrm{NC}^A = \mathrm{P}^A$ 的神谕，也可以构造使二者分离的神谕。因此任何"对一切神谕都成立"的技术——对角化、模拟——都无法解决本题。

### （二）自然化障碍的直接冲击

$\mathrm{NC} \subsetneq \mathrm{P}$ 若要成立，等价于证明某个显式问题（如 CVP）**不存在**多项式规模、多对数深度的电路。这是一条**电路下界**。而 Razborov–Rudich（1997）证明：若单向函数存在，则任何"自然的"组合式技术都无法证明足够强的电路下界。因此本题与 [#18 电路下界](18-circuit-lower-bounds.md) 共享**自然化障碍**这一核心难点。这也是本问题被标为 `OPEN-BARRIER` 的深层原因。

### （三）下界的"断崖"：只有最底层被解决

我们已知的电路下界，全部集中在极弱的电路类：

- $\mathrm{AC}^0$ 不能计算 **Parity**（Furst–Saxe–Sipser 1981；Ajtai 1983）——这是最底层的分离；
- $\mathrm{ACC}^0$ 不能计算某些 NEXP 问题（Williams 2011/2014）。

但**从 $\mathrm{NC}^1$ 往上，一片空白**：我们甚至无法证明 $\mathrm{NC}^1 \subsetneq \mathrm{NC}^2$，更无法证明 $\mathrm{NC} \subsetneq \mathrm{P}$。这种"低层已分离、高层全未知"的断崖式分布，是本问题最值得记住的特征。

### （四）一致性的微妙之处

NC 的定义依赖"一致性"：非一致的 NC 与非一致的多项式时间（即 $\mathrm{P/poly}$）是不同的对象。讨论本题时必须明确所采用的一致性约定，否则结论会随定义漂移。这一点常被初学者忽略。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界 | $\mathrm{NC} \subseteq \mathrm{P}$；更精细地 $\mathrm{NC}^1 \subseteq \mathrm{L} \subseteq \mathrm{NL} \subseteq \mathrm{NC}^2$ | 标准结论 |
| 下界（低层） | $\mathrm{Parity} \notin \mathrm{AC}^0$，故 $\mathrm{AC}^0 \subsetneq \mathrm{NC}^1$ | Furst–Saxe–Sipser, 1981；Ajtai, 1983 |
| 下界（更弱类） | $\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$：$\mathrm{ACC}^0$ 无法计算全部 NEXP，这是二十余年来首次突破 $\mathrm{AC}^0$ 型电路的通用下界 | Williams, 2011 / 2014 |
| 下界（$\mathrm{NC}^1$ 及以上） | **无已知非平凡结果**；连 $\mathrm{NC}^1 \subsetneq \mathrm{NC}^2$ 都未证明 | — |
| 完全性 | CVP（电路值问题）是 P 完全的（对数空间归约下） | Ladner, 1975 |

**上界与下界的区分**：上界方向给出的是"NC 能算什么 / 被 P 包含"，下界方向给出的是"某种电路类不能算什么"。在下界方向上，**只有 $\mathrm{AC}^0$、$\mathrm{ACC}^0$ 等最弱类有结果**，与分离 NC 和 P 所需的强度相去甚远。

## 解法现状与可行攻击路径

### 已解决的部分

- **最底层电路类的分离**：Parity ∉ AC⁰（Furst–Saxe–Sipser 1981；Ajtai 1983），故 $\mathrm{AC}^0 \subsetneq \mathrm{NC}^1$——包含链最底层的严格分离已被无条件证明。
- **更弱类的通用下界**：$\mathrm{NEXP} \nsubseteq \mathrm{ACC}^0$（Williams 2011/2014）——二十余年来首次突破 AC⁰ 型电路的通用下界。
- **完全性定位**：CVP 是 P 完全的（Ladner 1975），给出等价刻画：$\mathrm{NC} = \mathrm{P}$ 当且仅当 $\mathrm{CVP} \in \mathrm{NC}$。
- 已解决与未解决部分的精确分界是一条"断崖"：下界结果几乎全部止步于 AC⁰、ACC⁰；从 NC¹ 往上一片空白——连 $\mathrm{NC}^1 \subsetneq \mathrm{NC}^2$ 都未证明。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 算法化下界 | 先为某电路类（如 ACC⁰）给出非平凡 SAT 加速算法，再由算法导出下界 | Williams 的结果即此路线的成功范例 | 无法延伸到 NC¹ 及以上——那里的 SAT 算法本身就没有足够快的版本 |
| 针对具体 P 完全问题的并行算法 | 为 CVP、HORN-SAT、线性规划等设计多对数深度的并行算法 | 至今全部失败：无人找到任何一个 P 完全问题的 NC 算法 | 这既不能证明不可能，也强烈提示"P 完全 ≈ 天生串行" |
| 非自然证明技术 | 放弃构造性或广泛性之一 | 已知"非自然"下界只适用于极弱模型 | 无法扩展到 NC 或一般电路；放弃构造性丢组合意义，放弃广泛性难处理随机函数 |

### 已堵死的路径

- **相对化**（Baker–Gill–Solovay 1975）：存在使 $\mathrm{NC}^A = \mathrm{P}^A$ 与使二者分离的神谕，一切"对神谕成立"的技术（对角化、模拟）无效。
- **自然化**（Razborov–Rudich 1997）：$\mathrm{NC} \subsetneq \mathrm{P}$ 等价于证明某显式问题（如 CVP）不存在多项式规模多对数深度电路——这是一条电路下界；若单向函数存在，任何"构造性 + 广泛性"的组合式技术都无法证明足够强的电路下界。这是本题被标为 `OPEN-BARRIER` 的核心障碍。
- 研究路线图明确列为已排除的：一切相对化论证，以及所有满足"构造性 + 广泛性"的自然证明。

### 裁决

**`原理上受限`**

分离 NC 与 P 所需的电路下界正是自然化障碍的直接打击对象；已知下界止步于 AC⁰/ACC⁰，NC¹ 及以上是公认的下界真空区，且这条真空恰由已证明的障碍守护。

## 研究路线图

**路线一：算法化下界（algorithmic method）**
先为某电路类（如 ACC⁰）给出非平凡 SAT 加速算法，再由算法导出该类不能计算强问题的下界。Williams 的结果正是此路线的成功范例，但**尚无法延伸到 $\mathrm{NC}^1$ 及以上**——那里的 SAT 算法本身就没有足够快的版本。

**路线二：针对具体 P 完全问题的并行算法**
尝试为 CVP、HORN-SAT、线性规划等 P 完全问题设计多对数深度的并行算法。至今全部失败：无人找到任何一个 P 完全问题的 NC 算法。这既不能证明不可能，也强烈提示"P 完全 ≈ 天生串行"。

**路线三：非自然证明技术与"非自然"下界**
已知若干"非自然"的下界证明，但都只适用于极弱模型，无法扩展到 NC 或一般电路。卡点在于：放弃构造性或广泛性会丢失组合意义，或无法处理随机函数。

**已被排除的路线**：一切相对化论证，以及所有满足"构造性 + 广泛性"的自然证明。

## 关键文献

1. **Ladner, R.** *The circuit value problem is log space complete for P.* SIGACT News 7(1), 1975. — 定义 P 完全性，CVP 是标准 P 完全问题。
2. **Pippenger, N.** *On simultaneous resource bounds.* FOCS 1979. — 并行复杂性类的早期奠基工作，NC 因 Nick Pippenger 而得名。
3. **Cook, S.** *Towards a complexity theory of synchronous parallel computation.* L'Enseignement Mathématique, 1981. — 系统建立并行复杂性（NC）的框架。
4. **Furst, M., Saxe, J., Sipser, M.** *Parity, circuits, and the polynomial-time hierarchy.* Math. Systems Theory 17, 1984（FOCS 1981）. — Parity 不在 AC⁰ 中。
5. **Ajtai, M.** *$\Sigma^1_1$-formulae on finite structures.* Annals of Pure and Applied Logic 24, 1983. — 独立给出 AC⁰ 下界。
6. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 自然化障碍，本题的核心障碍。
7. **Williams, R.** *Nonuniform ACC circuit lower bounds.* JACM 61(1), 2014（CCC 2011）. — 三十年来的电路下界突破。
8. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍。
9. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 6 章讲电路下界与并行计算。
10. **Papadimitriou, C.** *Computational Complexity.* Addison-Wesley, 1994. — 经典教材，第 15、16 章讨论 P 完全性与并行计算。

## 常见误区

- **误区：NC 表示"非多项式"或"不可计算"。** —— NC 是 **"Nick's Class"**（因 Nick Pippenger 得名），指**多项式规模、多对数深度**的电路类，且 $\mathrm{NC} \subseteq \mathrm{P}$。它不是"难"的类，而是"高度可并行"的类。
- **误区：求解某个问题用了多个核，就说明它在 NC 中。** —— NC 要求**深度**为多对数级，且需**一致性**电路族。常数核并行、或依赖具体硬件的并行，都不满足 NC 的定义。
- **误区：CVP 是 P 完全的，所以 CVP 一定不在 NC 中。** —— P 完全性给出的是**条件性**结论：若 $\mathrm{CVP} \in \mathrm{NC}$ 则 $\mathrm{NC} = \mathrm{P}$。它**不**排除 CVP 在 NC 中；若真如此，反过来说明 $\mathrm{NC} = \mathrm{P}$。
- **误区：Parity 不在 AC⁰ 中，就说明 Parity 不能被并行化。** —— Parity ∉ AC⁰ 只说明它不在**常数深度**电路类中。Parity 实际上在 $\mathrm{NC}^1$ 中，是可并行化的。混淆"$\mathrm{AC}^0$ 下界"与"无法并行"是常见错误。
- **误区：既然我们证明了 $\mathrm{AC}^0 \subsetneq \mathrm{NC}^1$，那么 $\mathrm{NC} \subsetneq \mathrm{P}$ 也快解决了。** —— 恰恰相反。下界结果几乎全部止步于 $\mathrm{AC}^0$、$\mathrm{ACC}^0$；$\mathrm{NC}^1$ 及以上是公认的"下界真空区"。
- **误区：把非一致 NC 的结论直接搬到一致 NC。** —— 一致性是不同的约束。讨论时必须声明采用的电路族一致性，否则命题本身不明确。

## 可运行实验

**`experiments/parity_ac0_bound.py`** — 观察 Parity 需要多深的电路

脚本用**穷举搜索**小规模 Boolean 电路，统计在给定**深度上限**（如深度 2、3 的 $\mathrm{AC}^0$ 型电路）下能实现的函数数量与 Parity 的关系，并对比"常数深度"与"$\log n$ 深度"所需规模。更实用的版本是：对 $n \leq 8$ 的 Parity，枚举所有深度 $d$、扇入 $2^d$ 的决策树 / 小电路，展示 $n$ 稍增后规模急剧膨胀。

**它能验证的已知部分结果**：Parity 无法用常数深度、多项式规模的电路实现——这可以在很小的 $n$ 上经验性地观察到（规模随 $n$ 的增长明显快于多项式常数深度电路所能允许的）。

**这个实验不能说明什么**：

- 这是**有限规模的经验观察**，不能替代 Furst–Saxe–Sipser / Ajtai 的**无条件下界证明**。
- 它只涉及 $\mathrm{AC}^0$。即使完整跑通，也**不能**说明任何关于 $\mathrm{NC}^1$、NC 或 P 的事情。
- 它无法触及自然化障碍所排除的那类证明技术。

## 延伸阅读

- **教材**：Arora & Barak（文献 [9]）第 6 章；Papadimitriou（文献 [10]）第 15–16 章。
- **进阶**：Williams 的算法化下界论文（文献 [7]）及其相关讲义。
- **相关档案**：[#1 P vs NP](01-p-vs-np.md) 与本题共享电路下界的技术核心；[#18 电路下界](18-circuit-lower-bounds.md) 是本题的技术主战场；[#5 L vs NL](05-l-vs-nl.md) 处于 $\mathrm{NC}^1$ 与 $\mathrm{NC}^2$ 之间的同一窗口；[#3 P vs PSPACE](03-p-vs-pspace.md) 从空间视角切入 P 的边界。
