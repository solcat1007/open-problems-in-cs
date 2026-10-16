# #5 L vs NL

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论
**首次提出**：1970 年代，随空间复杂性研究出现（Savitch 1970 之后的经典问题）
**参与门槛**：需要新的数学工具

---

## 一句话概述

在图里判断"两个点是否连通"：如果允许**猜一条路径**，是否会比只能**老老实实搜索**更强大？

## 形式化陈述

**对数空间类**：

$$\mathrm{L} = \mathrm{DSPACE}(\log n), \qquad \mathrm{NL} = \mathrm{NSPACE}(\log n)$$

即图灵机可用的存储单元数随输入规模 $n$ **对数增长**（输入本身只读、不计入空间）。L 用的是确定性机器，NL 用的是非确定性机器。

**问题**：$\mathrm{L} \overset{?}{=} \mathrm{NL}$

已知包含链

$$\mathrm{L} \subseteq \mathrm{NL} \subseteq \mathrm{DSPACE}(\log^2 n) \subseteq \mathrm{NC}^2 \subseteq \mathrm{P}$$

其中 $\mathrm{NL} \subseteq \mathrm{DSPACE}(\log^2 n)$ 是 **Savitch 定理**（用 $O(s(n)^2)$ 的确定性空间模拟 $s(n)$ 的非确定性空间）。

**完全问题**：

- **有向 $s$-$t$ 连通性 STCON**（有向图上判断从 $s$ 能否到达 $t$）是 **NL 完全**的（在对数空间归约下）。因此

  > $\mathrm{L} = \mathrm{NL}$ 当且仅当 $\mathrm{STCON} \in \mathrm{L}$。

- **无向连通性 USTCON** 是 **L 完全**的——这是 2005 年的一项重大结果（下详）。

**关键结构性事实（Immerman–Szelepcsényi 1988）**：$\mathrm{NL} = \mathrm{co\text{-}NL}$。即非确定性对数空间类**在补运算下封闭**。这是一个令人意外的事实：它意味着"从 $s$ **不能**到达 $t$"这件事同样有对数空间的简短证明。

## 为什么困难

### （一）相对化障碍

取 $A$ 为一个 NL 完全集（如有向连通性）。由于 NL 在对数空间归约下封闭，可得 $\mathrm{L}^A = \mathrm{NL}^A = \mathrm{NL}$——存在**塌缩**的神谕；同时存在使 $\mathrm{L}^A \neq \mathrm{NL}^A$ 的神谕。两个方向的相对化世界都存在，故任何相对化技术都无法解决本题。

### （二）非相对化技术是唯一已知出路

Immerman–Szelepcsényi 定理（$\mathrm{NL} = \mathrm{co\text{-}NL}$）之所以重要，不仅在于结论本身，更在于它**不相对化**：存在神谕使 $\mathrm{NL}^A \neq \mathrm{co\text{-}NL}^A$。它使用了一种"归纳计数"（inductive counting）的精细技术，绕开了对角化。Reingold 关于无向连通性的结果同样是非相对化的。这提示：**解决 L vs NL 很可能必须依赖非相对化技术**，而这类技术极其稀少且难以扩展。

### （三）有向与无向的鸿沟

无向连通性 USTCON 有对数空间算法（Reingold 2005），而有向连通性 STCON 至今没有。二者形式相似，命运却截然不同。这种"无向可解、有向未知"的对比，正是本问题直觉上的难点所在：有向图的路径结构远比无向图复杂，而现有的展开图（expander）与随机游走技术**只对无向图奏效**。

### （四）计数能力的分界

L 缺乏计数能力，NL 却可以"猜一条路径"。若 $\mathrm{L} = \mathrm{NL}$，则对数空间足够完成有向可达性这类搜索。Szelepcsényi–Immerman 的计数技术虽然证明了 $\mathrm{NL}$ 对补封闭，却没有给出确定性算法——它只在非确定性一侧工作。这个"差一点点"的位置，是本问题长期停滞的技术根源。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界 | $\mathrm{NL} \subseteq \mathrm{DSPACE}(\log^2 n)$（Savitch）；$\mathrm{NL} \subseteq \mathrm{NC}^2$ | Savitch, 1970 |
| 上界（无向） | $\mathrm{USTCON} \in \mathrm{L}$，即 $\mathrm{SL} = \mathrm{L}$；无向连通性在对数空间内可解 | Reingold, 2005 |
| 结构性 | $\mathrm{NL} = \mathrm{co\text{-}NL}$（非相对化） | Immerman, 1988；Szelepcsényi, 1988 |
| 下界 | **无任何无条件分离**；连 $\mathrm{L} \neq \mathrm{NL}$ 都未证明 | — |
| 完全性 | 有向 $s$-$t$ 连通性 STCON 是 NL 完全的 | 标准结论 |
| 完全性 | 无向连通性 USTCON 是 L 完全的 | Reingold, 2005 |

**上界与下界的区分**：上界方向已经相当强（Savitch 的 $\log^2 n$、Reingold 的无向情形），下界方向则**完全空白**——我们甚至不能排除 $\mathrm{L} = \mathrm{NL}$。这种"上界丰富、下界缺失"的格局是空间复杂性研究的典型特征。

## 解法现状与可行攻击路径

### 已解决的部分

- **无向特例完全解决**：USTCON ∈ L，即 $\mathrm{SL} = \mathrm{L}$（Reingold 2005）——"非确定性/随机性在对数空间下是否有用"的一个真子情形被彻底攻克，且给出的是构造性算法。
- **补封闭性**：$\mathrm{NL} = \mathrm{co\text{-}NL}$（Immerman–Szelepcsényi 1988）——"从 $s$ 不能到达 $t$"同样有对数空间的简短证明；该结果不相对化，用的是归纳计数技术。
- **上界已确立**：$\mathrm{NL} \subseteq \mathrm{DSPACE}(\log^2 n)$（Savitch 1970），且 $\mathrm{NL} \subseteq \mathrm{NC}^2$。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 把无向技术推广到有向 | 展开图：无向图藏进常数度数展开图，随机游走快速混合 | Reingold 的方法在无向情形完全成功 | 有向图没有已知的展开图类似物——这是本路线最大的技术障碍 |
| 非相对化下界技术 | 寻找能"看见"对数空间计算细节、区分 L 与 NL 的技术 | 已知非相对化结果（Immerman–Szelepcsényi、Reingold）都指向此方向 | 它们都只给出包含关系而非分离；此类技术极其稀少且难以扩展 |
| 结构性质研究 | 研究 L = NL 的后果（确定性对数空间能否做某些搜索、对层级的影响） | 产出条件性结论 | 不直接推进无条件分离 |

### 已堵死的路径

- **相对化**（Baker–Gill–Solovay 1975）：存在塌缩神谕（$\mathrm{L}^A = \mathrm{NL}^A = \mathrm{NL}$）与分离神谕，两个方向的相对化世界都存在；研究路线图明确列为已排除的：一切相对化论证（对角化、模拟）。
- 一个"差一步"的信号：Szelepcsényi–Immerman 的归纳计数技术虽证明 NL 对补封闭，却只在非确定性一侧工作，给不出确定性算法——这个"差一点点"的位置是本问题长期停滞的技术根源。

### 裁决

**`原理上受限`**

相对化障碍排除了主流证明技术，而已知唯一有效的非相对化技术（归纳计数、展开图）都止步于包含关系与无向情形——NL 完全的有向连通性 STCON 成为现有技术无法跨越的鸿沟，下界方向完全空白。

## 研究路线图

**路线一：把无向技术推广到有向**
Reingold 的算法核心是**展开图（expander）**：无向图可以藏进一个常数度数的展开图，使随机游走快速混合，从而在 $\log$ 空间内判断连通性。关键卡点在于：**有向图没有已知的展开图类似物**。如何在有向图上构造所需的"伪随机游走"结构，是本路线最大的技术障碍。

**路线二：非相对化下界技术**
寻找能"看见"对数空间计算细节、从而区分 L 与 NL 的非相对化技术。已知的非相对化结果（Immerman–Szelepcsényi、Reingold）都指向这个方向，但都只给出包含关系而非分离。

**路线三：结构性质研究**
研究 $\mathrm{L} = \mathrm{NL}$ 的后果（如确定性对数空间能否做某些搜索、对层级的影响）。此路线产出条件性结论。

**已被排除的路线**：一切相对化论证（对角化、模拟）。

## 关键文献

1. **Savitch, W.** *Relationships between nondeterministic and deterministic tape complexities.* J. Comput. Syst. Sci. 4(2), 1970. — $\mathrm{NL} \subseteq \mathrm{DSPACE}(\log^2 n)$。
2. **Immerman, N.** *Nondeterministic space is closed under complementation.* SIAM J. Comput. 17(5), 1988. — $\mathrm{NL} = \mathrm{co\text{-}NL}$，非相对化的典范结果。
3. **Szelepcsényi, R.** *The method of forced enumeration for nondeterministic automata.* Acta Informatica 26(3), 1988. — 独立证明同一结果。
4. **Reingold, O.** *Undirected connectivity in log-space.* JACM 55(4), 2008（STOC 2005）. — 证明 $\mathrm{SL} = \mathrm{L}$，用展开图技术。
5. **Aleliunas, R., Karp, R., Lipton, R., Lovász, L., Rackoff, C.** *Random walks, universal traversal sequences, and the complexity of maze problems.* FOCS 1979. — 用随机游走给出无向连通性的随机对数空间算法。
6. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍。
7. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 4 章讲空间复杂性。
8. **Papadimitriou, C.** *Computational Complexity.* Addison-Wesley, 1994. — 经典教材，第 16 章讨论空间类与补封闭性。

## 常见误区

- **误区：L 表示"线性空间"（Linear space），NL 表示"非线性空间"。** —— 都错。L 与 NL 中的 **L** 是 **Logarithmic（对数）空间**，NL 是 **Nondeterministic Logarithmic** 空间。二者都以 $\mathcal{O}(\log n)$ 为界，区别只在确定性 vs 非确定性。
- **误区：$\mathrm{L} \neq \mathrm{NL}$ 已被证明。** —— 无任何无条件分离。本题在下界方向完全空白。
- **误区：既然无向连通性在做对数空间内，有向连通性自然也可以。** —— 恰恰相反。有向连通性 STCON 是 **NL 完全**的，无人给出对数空间算法；它正是 L vs NL 的核心难点。无向情形的成功依赖展开图，而这些技术对**有向图不适用**。
- **误区：$\mathrm{NL} = \mathrm{co\text{-}NL}$ 说明 $\mathrm{L} = \mathrm{NL}$。** —— 不是。补封闭性只在**非确定性**一侧成立。它甚至不相对化，恰恰说明这类问题的证明需要非相对化技术，而非"顺理成章"。
- **误区：$O(\log^2 n)$ 空间是"接近对数空间"所以差不多。** —— $\log^2 n$ 与 $\log n$ 在渐近意义下相差一个无穷大的因子。用 $\log^2 n$ 模拟 $\log n$ 非确定性**不能**推出两者相等。
- **误区：把 SL（对称对数空间）当作一个仍然独立的类。** —— Reingold（2005）已证明 $\mathrm{SL} = \mathrm{L}$。SL 现在是 L 的另一个名字；无向连通性因此是 L 完全的。

## 可运行实验

**`experiments/reachability_random_walk.py`** — 随机游走在无向图上有向图上的对比

脚本对两类图各生成一批实例：(a) **无向连通图**；(b) **有向强连通 / 一般有向图**。然后运行极低内存的随机游走（每次只记住当前位置），统计在给定步数上限内到达目标的比例，并记录所需的"记忆"（位置 + 步数计数器）。

**它能验证的已知部分结果**：无向图的随机游走能在多项式步数内以高概率找到目标（Aleliunas 等 1979 的无向连通性随机算法），且其正确性依赖无向图**没有"单向陷阱"**这一结构。有向图上随机游走会因陷阱而失败。

**这个实验不能说明什么**：

- 它只是**有限规模上的经验观察**，不能推出任何关于 L vs NL 的渐近结论。
- 随机游走上界**不能**推出确定性对数空间算法；Reingold 的算法用的是展开图而非朴素随机游走。
- 模拟"低内存"是**算法实现层面的**，与复杂性类的严格定义（图灵机磁带单元数）不同；不要据此宣称"已验证 STCON 难"。

## 延伸阅读

- **教材**：Arora & Barak（文献 [7]）第 4 章；Papadimitriou（文献 [8]）第 16 章。
- **进阶**：Reingold 的 STOC 2005 论文（文献 [4]）及其后续讲义，是理解"展开图 + 对数空间"的必读材料。
- **相关档案**：[#4 NC vs P](04-nc-vs-p.md) 讨论 $\mathrm{NC}^1$、$\mathrm{NC}^2$ 与本题同处一个窗口；[#6 L vs RL](06-l-vs-rl.md) 关注随机性能否在对数空间内被去除；[#9 PH vs PSPACE](09-ph-vs-pspace.md) 从层级视角承接空间类。
