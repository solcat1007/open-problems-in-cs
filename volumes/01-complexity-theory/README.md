# Vol.01 计算复杂性理论

本册收录 20 个问题，全部围绕一条主线：**计算的资源边界画在哪里**。这一册也是整个仓库"障碍"含量最高的一册——前 10 题中有 8 个被标为 `OPEN-BARRIER`。读这一册之前，强烈建议先读 [METHODOLOGY.md 第二节](../../METHODOLOGY.md)，否则很容易把"障碍"误读成"不可解"。

## 一、核心张力

### 张力一：上界丰富，下界贫血

复杂性理论有一副失衡的骨架：**我们能算出的东西，远远多于我们能证明算不出的东西**。

- 上界方向成果密集：Savitch 让 $\mathrm{PSPACE} = \mathrm{NPSPACE}$；Reingold 让 $\mathrm{SL} = \mathrm{L}$；Impagliazzo–Wigderson 在硬度假设下让 $\mathrm{P} = \mathrm{BPP}$；Shor 让分解与离散对数落进 $\mathrm{BQP}$。
- 下界方向却近乎空白：对于 [#1 P vs NP](problems/01-p-vs-np.md)、[#3 P vs PSPACE](problems/03-p-vs-pspace.md)、[#4 NC vs P](problems/04-nc-vs-p.md)、[#5 L vs NL](problems/05-l-vs-nl.md)、[#9 PH vs PSPACE](problems/09-ph-vs-pspace.md)，我们**连一个无条件分离都拿不出来**。

这不是"某几个问题没解决"，而是一种**系统性的方法论不对称**。记住这条张力，就能理解本册几乎每一题为什么写着"下界：无已知非平凡结果"。

### 张力二：三个原理性障碍

为什么下界这么难？因为最自然的证明技术已被**原理性地排除**：

1. **相对化障碍**（Baker–Gill–Solovay 1975）：任何对任意神谕都成立的技术，都证不出 P ≠ NP。整个 1970 年代的对角化方法就此出局。
2. **自然化障碍**（Razborov–Rudich 1997）：若单向函数存在，则任何"构造性 + 广泛性"的组合式技术都证不出足够强的电路下界。它揭示了一个深刻对立：**密码学的存在性，与证明电路下界的能力相互排斥**。
3. **代数化障碍**（Aaronson–Wigderson 2009）：把相对化推广到"允许低次多项式扩张"的技术，堵住了用交互式证明绕过前两关的希望。

三者叠加，造就了本册最实用的筛选规则：**任何声称解决这些问题的论证，若只用到上述三类技术，必然有错**。

### 张力三：条件性结论的双刃性

本册大量结论是**条件性**的：

- [#8 P vs BPP](problems/08-p-vs-bpp.md)：**若** E 需要指数电路，**则** P = BPP。
- [#10 UGC](problems/10-ugc.md)：**若** UGC 成立，**则** Max-Cut、顶点覆盖等的近似比下界成立。
- [#11 ETH](problems/11-eth.md)、[#12 SETH](problems/12-seth.md)（见索引）：是细粒度复杂性**全部**条件性下界的假设来源。

这些结论本身是可靠的，但**它们的可靠性完全绑定在假设上**。去掉前提去引用，就变成了错误陈述。这是本领域最容易被误引的一类内容，也是 METHODOLOGY 反复强调的一点。

### 张力四：空间与时间的不对称

时间与空间这两种资源的处境截然不同。

**空间方向拥有无条件结果**：空间层级定理（Stearns–Hartmanis–Lewis 1965）无条件地给出 $\mathrm{L} \subsetneq \mathrm{PSPACE}$；Savitch 定理无条件地让 $\mathrm{PSPACE} = \mathrm{NPSPACE}$；Immerman 与 Szelepcsényi 无条件地让 $\mathrm{NL} = \mathrm{co\text{-}NL}$；Reingold 无条件地让 $\mathrm{SL} = \mathrm{L}$。这些结果**不依赖任何未证明假设**，而且其中若干（$\mathrm{NL} = \mathrm{co\text{-}NL}$、$\mathrm{SL} = \mathrm{L}$）恰恰是**非相对化**的。

**时间方向则几乎全是条件性的**：$\mathrm{P} = \mathrm{BPP}$ 需要硬度假设；$\mathrm{P} \neq \mathrm{NP}$ 缺乏任何下界；连 $\mathrm{P}$ 与 $\mathrm{PSPACE}$ 的分离都做不出来。

为什么空间更好办？一个直觉是：空间受限会**强制**随机游走快速混合，也会让计算过程可以被"计数"与"归纳"地分析，从而给非相对化技术留出缝隙。这一不对称，是 [#5 L vs NL](problems/05-l-vs-nl.md) 与 [#6 L vs RL](problems/06-l-vs-rl.md) 能在本册中呈现"真实的、无条件的进展"的原因，也是理解本册整体格局的一把钥匙。

## 二、问题地图

本册 10 篇新档案，可以按"资源类型"与"结构层级"排成一张图。

### 按资源：时间、空间、并行、量子、随机

- **时间**：[#1 P vs NP](problems/01-p-vs-np.md)、[#2 NP vs Co-NP](problems/02-np-vs-conp.md)、[#3 P vs PSPACE](problems/03-p-vs-pspace.md)。
- **空间**：[#3](problems/03-p-vs-pspace.md)、[#5 L vs NL](problems/05-l-vs-nl.md)、[#9 PH vs PSPACE](problems/09-ph-vs-pspace.md)。
- **并行**：[#4 NC vs P](problems/04-nc-vs-p.md)。
- **随机**：[#6 L vs RL](problems/06-l-vs-rl.md)、[#8 P vs BPP](problems/08-p-vs-bpp.md)。
- **量子**：[#7 BQP vs NP](problems/07-bqp-vs-np.md)。
- **近似/PCP**：[#10 UGC](problems/10-ugc.md)。

### 按层级：一条包含链

这些类可以串成一条链，本册各题正是问这条链上每一段是否严格：

$$\mathrm{NC}^1 \subseteq \mathrm{L} \subseteq \mathrm{NL} \subseteq \mathrm{NC}^2 \subseteq \mathrm{NC} \subseteq \mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PH} \subseteq \mathrm{PSPACE} \subseteq \mathrm{EXP}$$

叠加随机与量子维度后：

$$\mathrm{P} \subseteq \mathrm{BPP} \subseteq \mathrm{BQP} \subseteq \mathrm{PP} \subseteq \mathrm{PSPACE}$$

**链上没有任何一段被无条件证明为严格**（除最底层的 $\mathrm{AC}^0 \subsetneq \mathrm{NC}^1$ 等少数分离）。这就是本册问题的整体图景。

### 关键依赖关系

- [#1](problems/01-p-vs-np.md) → [#2](problems/02-np-vs-conp.md) / [#3](problems/03-p-vs-pspace.md) / [#4](problems/04-nc-vs-p.md) / [#9](problems/09-ph-vs-pspace.md)：P vs NP 的结论会连带影响整个层级。其中 [#2](problems/02-np-vs-conp.md) 更弱（$\mathrm{NP} \neq \mathrm{co\text{-}NP} \Rightarrow \mathrm{P} \neq \mathrm{NP}$），[#3](problems/03-p-vs-pspace.md) 与 [#9](problems/09-ph-vs-pspace.md) 更强。
- [#4 NC vs P](problems/04-nc-vs-p.md) 与 [#5 L vs NL](problems/05-l-vs-nl.md) 通过包含链 $\mathrm{NC}^1 \subseteq \mathrm{L} \subseteq \mathrm{NL} \subseteq \mathrm{NC}^2$ 相连——[#5](problems/05-l-vs-nl.md) 恰好卡在 $\mathrm{NC}^1$ 与 $\mathrm{NC}^2$ 之间。
- [#6 L vs RL](problems/06-l-vs-rl.md) 与 [#8 P vs BPP](problems/08-p-vs-bpp.md) 是同一去随机化主题的**空间版与时间版**：空间版已有 Reingold 的无条件突破，时间版只能条件性地解决。
- [#7 BQP vs NP](problems/07-bqp-vs-np.md) 的上界 $\mathrm{BQP} \subseteq \mathrm{PSPACE}$ 直接接到 [#3](problems/03-p-vs-pspace.md)。
- [#10 UGC](problems/10-ugc.md) 蕴含 $\mathrm{P} \neq \mathrm{NP}$，因此它的证明必然背负 [#1](problems/01-p-vs-np.md) 所面临的障碍。
- [#8](problems/08-p-vs-bpp.md) 的硬度假设与 [#13 单向函数](problems/13-one-way-functions.md)、[#18 电路下界](problems/18-circuit-lower-bounds.md) 共享同一块地基："存在足够难的函数"。

## 三、推荐阅读顺序

**第一阶段：建立骨架**

1. 先读 [METHODOLOGY.md](../../METHODOLOGY.md) 第二节，弄清楚三个障碍到底限制的是什么。
2. 读 [#1 P vs NP](problems/01-p-vs-np.md)——它是本册的"母问题"，格式也最完整。
3. 读 [#2 NP vs Co-NP](problems/02-np-vs-conp.md)，体会"更弱的命题同样被障碍锁死"。

**第二阶段：把层级补齐**

4. [#3 P vs PSPACE](problems/03-p-vs-pspace.md) → [#9 PH vs PSPACE](problems/09-ph-vs-pspace.md)：理解时间与空间、层级与空间之间的关系。
5. [#4 NC vs P](problems/04-nc-vs-p.md)：进入"并行 vs 串行"，也是电路下界的主战场。
6. [#5 L vs NL](problems/05-l-vs-nl.md)：空间复杂性的核心，认识"非相对化技术"（Immerman–Szelepcsényi、Reingold）。

**第三阶段：随机与量子**

7. [#6 L vs RL](problems/06-l-vs-rl.md)：接触一个**没有原理性障碍**的 `OPEN` 问题，理解 `OPEN` 与 `OPEN-BARRIER` 的区别。
8. [#8 P vs BPP](problems/08-p-vs-bpp.md)：理解**条件性结论**的正确表述方式（必须带前提）。
9. [#7 BQP vs NP](problems/07-bqp-vs-np.md)：量子视角下的同一批问题。

**第四阶段：近似与硬度假设**

10. [#10 UGC](problems/10-ugc.md)：进入 PCP 与近似算法的世界，理解"若 UGC 成立，则……"这一条件性体系。
11. 延伸至 [#11 ETH](problems/11-eth.md)、[#12 SETH](problems/12-seth.md)、[#13 单向函数](problems/13-one-way-functions.md)、[#18 电路下界](problems/18-circuit-lower-bounds.md)。

## 四、阅读须知

**第一，`OPEN-BARRIER` 不等于"问题不可解"。** 障碍限制的是**证明技术**，不是**答案**。一个带此标记的问题，明天仍可能被一种全新的、非相对化的技术解决。本册把"哪些锤子敲不动"讲清楚，正是为了帮助后来者避开已被堵死的路。

**第二，严格区分上界与下界。** "存在算法做到 X"与"不存在算法做到 X"是两个量级不同的命题。本册每篇的"当前最好结果"表都刻意分行列出，引用时请勿混用。

**第三，条件性结论必须带前提。** 看到"证明了 X 不可能"时，请先确认它前面有没有"若……成立"。

**第四，本册不提供解法。** 这些问题中多个是千禧年大奖问题，逾半个世纪未有实质进展。任何声称用文档解决它们的说法，都应当先接受三个障碍的检验。本册的价值在于画出"卡点地图"，而不在于给出答案。

---

**相关阅读**：[PROBLEMS.md](../../PROBLEMS.md) 索引总表 · [METHODOLOGY.md](../../METHODOLOGY.md) 状态分级与障碍详解 · [TEMPLATE.md](../../TEMPLATE.md) 档案标准格式。
