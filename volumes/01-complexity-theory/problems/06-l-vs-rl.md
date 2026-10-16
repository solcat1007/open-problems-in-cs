# #6 L = RL？

**状态**：`OPEN`
**领域**：计算复杂性理论
**首次提出**：1980 年代前后，随随机化复杂性类 RL 的定义出现（Aleliunas 等 1979；Gill 1977 对概率图灵机的奠基）
**参与门槛**：需要新的数学工具

---

## 一句话概述

如果允许算法抛硬币，它是否能在**对数空间**内解决确定性算法解决不了的问题？

## 形式化陈述

**RL（随机对数空间，Randomized Logarithmic-space）**：由**单侧错误**的概率图灵机定义，机器在对数空间、多项式时间内运行，且

$$x \in L \implies \Pr[M(x) \text{ 接受}] \geq 1/2, \qquad x \notin L \implies \Pr[M(x) \text{ 接受}] = 0$$

即机器**永不错误接受**，只可能错误拒绝。误差界常数可任取 $(0,1)$，重复运行即可把错误率压到任意小。

**BPL** 是相应的**双侧错误**版本：两类错误都允许。

**问题**：$\mathrm{L} \overset{?}{=} \mathrm{RL}$

已知包含链

$$\mathrm{L} \subseteq \mathrm{RL} \subseteq \mathrm{BPL} \cap \mathrm{NL}$$

即 RL 夹在 L 与 BPL / NL 之间。普遍猜想 $\mathrm{L} = \mathrm{RL} = \mathrm{BPL}$：**随机性在对数空间下不提供额外能力**。

**核心特例**：无向连通性 USTCON 有随机对数空间算法（随机游走，Aleliunas 等 1979），因此 $\mathrm{USTCON} \in \mathrm{RL}$；而它又被证明属于 L（Reingold 2005）。这为猜想提供了迄今最强的一类证据。

## 为什么困难

### （一）"恰好差一步"的结构位置

RL 卡在 L 与 BPL 之间，且 $\mathrm{RL} \subseteq \mathrm{NL}$。要证明 $\mathrm{L} = \mathrm{RL}$，需要把随机游走"去随机化"成一个确定性对数空间算法。已知的去随机化结果都只在一个方向上逼近：

- Nisan（1992）证明 $\mathrm{RL} \subseteq \mathrm{SC}$（多项式时间、多对数空间）；
- Saks–Zhou（1999）进一步给出 $\mathrm{BPL} \subseteq \mathrm{DSPACE}(\log^{3/2} n)$。

这些上界把 $\log n$ 抬到 $\log^{3/2} n$ 或"多对数空间"，**始终回不到 $\log n$**。这条"差一个 $\log$ 因子"的鸿沟，是本问题长期停滞的直接原因。

### （二）为什么随机性可能是"免费"的

在**多项式时间**里，随机性是否可去（$\mathrm{P} = \mathrm{BPP}$）被广泛认为成立，且可由电路下界假设推出（见 [#8 P vs BPP](08-p-vs-bpp.md)）。在**对数空间**里，情形更为乐观：因为空间受限会强制随机游走快速混合，展开图等组合工具可以真正发挥作用。Reingold 的 $\mathrm{SL} = \mathrm{L}$ 正是这种"空间限制帮助去随机化"的典范——在有向图这一尚未解决的邻域之外，无向情形已被完全攻克。

### （三）本问题没有明确的原理性障碍（这是它被标为 OPEN 的原因）

与 [#1](01-p-vs-np.md)–[#5](05-l-vs-nl.md) 不同，**尚无被证明的原理性障碍**（如相对化、自然化）直接适用于 L vs RL。这体现在两个事实：

1. 已有的进展（$\mathrm{SL} = \mathrm{L}$、$\mathrm{RL} \subseteq \mathrm{SC}$）都是**无条件**的，不依赖任何未证明假设；
2. 这类空间去随机化问题常常能被"局部"攻克，而不像 P vs NP 那样被全局障碍锁死。

相对化障碍对本问题的适用性**尚未明确** [待核实]。因此本仓库将其归为 `OPEN` 而非 `OPEN-BARRIER`：我们不知道哪一类证明技术被原理性地排除，也因此不能排除"明天就有人解决它"。

### （四）有向随机游走的陷阱

无向图的随机游走能在多项式步数内混合（因为没有"单向陷阱"）；有向图的随机游走可能长期困在某个局部区域。RL 的算法（如 USTCON 的随机游走）恰好利用了无向结构。要把这些技术推广到 BPL 或更一般的 RL 实例，必须处理有向结构带来的陷阱问题——这正是核心难点。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（去随机化） | $\mathrm{RL} \subseteq \mathrm{SC}$（多项式时间、多对数空间） | Nisan, 1992 |
| 上界（去随机化） | $\mathrm{BPL} \subseteq \mathrm{DSPACE}(\log^{3/2} n)$，故 $\mathrm{RL} \subseteq \mathrm{DSPACE}(\log^{3/2} n)$ | Saks & Zhou, 1999 |
| 上界（包含） | $\mathrm{L} \subseteq \mathrm{RL} \subseteq \mathrm{BPL}$ 且 $\mathrm{RL} \subseteq \mathrm{NL}$ | 标准结论 |
| 上界（无向特例） | $\mathrm{USTCON} \in \mathrm{L}$，即 $\mathrm{SL} = \mathrm{L}$ | Reingold, 2005 |
| 下界 | **无任何无条件分离**；不能排除 $\mathrm{L} = \mathrm{RL}$ | — |

**上界与下界的区分**：上界方向（存在算法 / 包含关系）成果丰富，下界方向（不存在算法）完全空白。这正是 `OPEN` 类问题的典型形态：**没有障碍，只是没人成功**。

## 解法现状与可行攻击路径

### 已解决的部分

- **无向特例完全解决**：USTCON 有随机对数空间算法（Aleliunas 等 1979）且已被证明在 L 中（Reingold 2005，$\mathrm{SL} = \mathrm{L}$）——RL 型问题的一个真子情形被彻底去随机化，为猜想提供迄今最强的一类证据。
- **弱去随机化已完成（无条件）**：$\mathrm{RL} \subseteq \mathrm{SC}$（Nisan 1992，多项式时间、多对数空间）；$\mathrm{BPL} \subseteq \mathrm{DSPACE}(\log^{3/2} n)$（Saks–Zhou 1999）。这些结果都不依赖任何未证明假设。
- **包含结构已钉住**：$\mathrm{L} \subseteq \mathrm{RL} \subseteq \mathrm{BPL} \cap \mathrm{NL}$。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 推广 Reingold 的展开图技术 | 之字形积等"伪随机游走"结构处理更一般的 RL | Reingold–Trevisan–Vadhan（2006）已把伪随机游走推广到正则有向图 | 有向图的展开图类似物尚不完善 |
| PRG 路线的空间版本 | Nisan（1990）空间受限 PRG，种子 $O(\log^2 n)$ 位 | 已直接给出 RL ⊆ SC 型结果 | 要把空间降到 $\log n$，需把种子降到 $O(\log n)$——种子长度下界正是当前做不到的地方 |
| 结构性研究 | 研究 L = RL 的后果及其对 BPL、NL 图景的影响 | 产出条件性结论 | 不直接推进无条件分离 |

### 已堵死的路径

暂无已知的原理性排除结果——这正是本问题被标为 `OPEN` 而非 `OPEN-BARRIER` 的原因：尚无被证明的原理性障碍（如相对化、自然化）直接适用，相对化障碍对本问题的适用性尚未明确 [待核实]。已有进展（$\mathrm{SL} = \mathrm{L}$、$\mathrm{RL} \subseteq \mathrm{SC}$）都是无条件的，这类空间去随机化问题常能被"局部"攻克。

### 裁决

**`路径已知，尚需突破`**

两条明确的攻击路线（展开图推广、PRG 种子缩短）都已推进到有形位置，且不存在原理性障碍；硬卡点一致地落在"有向结构"与"一个 log 因子"上——所有已知去随机化都停在 $\log^{3/2} n$ 或多对数空间，始终回不到 $\log n$。

## 研究路线图

**路线一：把 Reingold 的展开图技术推广到 BPL / RL**

Reingold 用**展开图（expander）**与**之字形积（zig-zag product）**在 $\log$ 空间内求解无向连通性。自然的想法是构造类似的"伪随机游走"结构来处理更一般的 RL。Reingold、Trevisan 与 Vadhan（2006）把伪随机游走推广到正则有向图的工作，是此路线的重要进展。卡点在于：**有向图的展开图类似物尚不完善**。

**路线二：伪随机生成器（PRG）路线的空间版本**

Nisan（1990）为空间受限计算构造了 PRG，其种子只需 $O(\log^2 n)$ 位，这直接给出 RL ⊆ SC 型结果。要把空间降到 $\log n$，需要种子长度降到 $O(\log n)$——这正是当前做不到的地方。卡点在于 PRG 的种子长度下界。

**路线三：结构性研究**

研究 $\mathrm{L} = \mathrm{RL}$ 的后果，例如它如何影响 BPL、NL 的图景。此路线产出条件性结论。

## 关键文献

1. **Aleliunas, R., Karp, R., Lipton, R., Lovász, L., Rackoff, C.** *Random walks, universal traversal sequences, and the complexity of maze problems.* FOCS 1979. — 用随机游走给出无向连通性的随机对数空间算法，RL 的起点。
2. **Gill, J.** *Computational complexity of probabilistic Turing machines.* SIAM J. Comput. 6(4), 1977. — 概率图灵机与随机化复杂性类的奠基工作。
3. **Nisan, N.** *Pseudorandom generators for space-bounded computation.* Combinatorica 12(4), 1992（STOC 1990）. — 空间受限的 PRG；并证明 $\mathrm{RL} \subseteq \mathrm{SC}$。
4. **Nisan, N.** *RL ⊆ SC.* STOC 1992. — 直接的弱去随机化结论。
5. **Nisan, N., Szemerédi, E., Wigderson, A.** *Undirected connectivity in $O(\log^{1.5} n)$ space.* FOCS 1992. — 无向连通性的空间改进。
6. **Saks, M., Zhou, S.** *$\mathrm{BP}_H\mathrm{SPACE}(S) \subseteq \mathrm{DSPACE}(S^{3/2})$.* J. Comput. Syst. Sci. 58(2), 1999. — 双侧错误空间类的去随机化，给出 $\log^{3/2} n$。
7. **Reingold, O.** *Undirected connectivity in log-space.* JACM 55(4), 2008（STOC 2005）. — $\mathrm{SL} = \mathrm{L}$，本领域最重要的无条件去随机化成果。
8. **Reingold, O., Trevisan, L., Vadhan, S.** *Pseudorandom walks on regular digraphs and the RL vs. L problem.* STOC 2006. — 把伪随机游走推广到正则有向图，直接针对 RL vs L。
9. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 4、20 章。
10. **Goldreich, O.** *Computational Complexity: A Conceptual Perspective.* Cambridge University Press, 2008. — 随机化与去随机化的系统讨论。

## 常见误区

- **误区：RL 表示"随机线性空间"。** —— RL 是 **Randomized Logarithmic-space**，即以**对数空间**为界的单侧错误随机类。它与线性空间（Linear space，即 L 的另一含义）无关。
- **误区：$\mathrm{L} \neq \mathrm{RL}$ 已被证明，"随机性一定有用"。** —— 恰恰相反，主流猜想是 $\mathrm{L} = \mathrm{RL}$；且在下界方向**没有任何无条件分离**。过度乐观与过度悲观在这里都无据。
- **误区：$\mathrm{RL} \subseteq \mathrm{SC}$ 说明 RL 已被去随机化。** —— SC 允许**多对数**空间，而 RL 要求**对数**空间。$\log^2 n$ 与 $\log n$ 相差无穷大，所以这只是一次**弱**去随机化，不是本问题的解。
- **误区：Reingold 的 $\mathrm{SL} = \mathrm{L}$ 顺带解决了 $\mathrm{L} = \mathrm{RL}$。** —— SL 是**对称**对数空间（无向连通性的类）；RL 是**随机**对数空间。两者相关但不同。Reingold 解决的是无向情形，不覆盖一般 RL。
- **误区：把 $\mathrm{RL} \subseteq \mathrm{NL}$ 读成 $\mathrm{RL} = \mathrm{NL}$。** —— $\subseteq$ 不是 $\subseteq$ 的反向。"随机对数空间 ⊆ 非确定性对数空间"是标准结论；等号未知。
- **误区：既然本问题标为 OPEN 而非 OPEN-BARRIER，就说明"没有障碍，很容易"。** —— 错。`OPEN` 的含义是"尚未发现原理性障碍"，即我们不知道哪把锤子被原理性排除；这既不表示容易，也不表示难。L vs NL 同样是"无下界"，却已停滞数十年。

## 可运行实验

**`experiments/random_walk_mixing.py`** — 随机游走混合时间 vs 图结构

脚本构造三类图：(a) **无向连通图**（如随机正则图、路径图）；(b) **有向强连通图**；(c) **lollipop 等近似陷阱结构**。对每类运行随机游走，统计**覆盖时间（cover time）**与达到均匀分布所需的**混合步数**，并对比"记忆当前位置所需的空间"与实际图规模。

**它能验证的已知部分结果**：无向图随机游走的覆盖时间是多项式的（Aleliunas 等 1979），因此在多项式步数内、用 $O(\log n)$ 的计数器空间即可高概率判断连通性——这正是 RL 算法的经验基础。有向图上的游走则可能因陷阱而指数级变慢。

**这个实验不能说明什么**：

- 它只展示**随机算法**的行为，**完全不能**说明确定性算法能否做到同样的事（即不能触及 $\mathrm{L} = \mathrm{RL}$）。
- 它是**有限规模、特定分布**的模拟，无法推出渐近结论。
- 它无法触及任何非相对化证明技术，也无法验证或不验证 Reingold 的登录空间算法（那是构造性的、需精确证明的）。

## 延伸阅读

- **教材**：Arora & Barak（文献 [9]）第 4、20 章；Goldreich（文献 [10]）关于随机化的章节。
- **进阶**：Reingold–Trevisan–Vadhan（文献 [8]）是直接针对 RL vs L 的技术入口。
- **相关档案**：[#5 L vs NL](05-l-vs-nl.md) 是本题的直接邻居（同处对数空间）；[#8 P vs BPP](08-p-vs-bpp.md) 讨论多项式时间下的同一类去随机化问题；[#4 NC vs P](04-nc-vs-p.md) 从并行视角看对数空间与 NC 的相邻关系。
