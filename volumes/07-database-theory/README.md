# Vol.07 数据库理论

本册收录 6 个问题。它们的共同底色只有一句话：**数据库理论把逻辑的可判定性与计算复杂度当作一等公民**。因此这一册的开放问题，几乎全部可以写成同一个形式——

> **某个查询语言的表达能力与判定复杂度，精确落在哪里？**

这不是巧合，而是数据库理论作为"应用逻辑"的必然结果。本册 README 就围绕这条主线展开：先讲这个中心视角，再讲为什么**二分定理（dichotomy）**适合回答这类问题、为什么它是本领域的核心范式，最后给出阅读顺序。

## 一、中心视角：判定性与复杂度是一等公民

一个数据库系统每时每刻都在回答同一个问题的各种变体：

- "这条查询能不能用另一条更快的查询替代？"（查询优化 → [包含](problems/74-query-containment.md)）
- "这里的缺失值会不会影响最终答案？"（[不完全信息](problems/79-incomplete-information-query.md)）
- "数据互相冲突时，哪个答案仍然可信？"（[一致性查询应答](problems/76-soft-repair-dichotomy.md)）
- "结果元组是从哪些源数据推出来的？"（[溯源](problems/78-datalog-provenance.md)）
- "如果每条记录带一个概率，答案的概率是多大？"（[概率数据库](problems/77-mpd-probabilistic-db.md)）
- "把 `SUM`、`AVG` 加进查询语言后，它到底能表达什么？"（[聚合逻辑](problems/75-fo-with-aggregates.md)）

这六个问题的**语法**各不相同，但**骨架**完全一致：都给定了(1)一个查询语言、(2)一族"合法"的数据库（受约束、含缺值、带概率、可递归），(3)一个需要判定的语义目标（包含、确定答案、最优解释、溯源等价……），然后问同一件事：**这个判定问题可判定吗？如果能，复杂度精确落在哪一档？**

这就是"逻辑作为一等公民"的具体含义。在别的领域，形式语言是分析工具；在数据库理论里，形式语言就是**被研究的对象本身**——因为系统的能力与代价，直接由这些语言的表达力和判定复杂度决定。

## 二、为什么二分定理是核心范式

一旦问题被写成"复杂度落在哪一档"，人们的期望就自然变成：**能不能给出一张完整的分类表？** 也就是：对**每一类**查询 / 约束，该问题要么在 $\mathrm{P}$ 中，要么是 NP（或 coNP、$\#\mathrm{P}$）完全，**没有中间态**。这种"非此即彼"的完整分类，就是**二分定理**。

二分定理为什么特别适合数据库理论？

**第一，问题天然带参数。** 查询类、信息模型、约束类是三个可以独立变动的维度。二分定理给出的正是"固定另外两个、按第三个维度分类"的答案，与理论问题和技术需求的形态天然吻合。

**第二，二分定理给出的是"精确刻画"，而不是"上界或下界"。** 本册反复强调：**上界**（存在算法）与**下界**（不存在算法）难度相差几个量级，而**精确刻画**要求两者相接、不留缝隙。"分层查询求值在 P、非分层则 $\#\mathrm{P}$ 难"（[#77](problems/77-mpd-probabilistic-db.md)）、"固定模板的合取查询包含：P 或 NP 完全"（[#74](problems/74-query-containment.md)）就是这种精确刻画的样本。它们是本领域最有力的结论形式。

**第三，二分定理的母体范式已经成功。** 数据库理论的很多二分问题，最终都被归约到**约束满足问题（CSP, constraint satisfaction problem）**的二分。Feder–Vardi 在 1998 年提出猜想：**对每一种约束语言，CSP 要么在 P 中、要么是 NP 完全**。这个猜想后来被 **Bulatov（2017）与 Zhuk（2017/2020）独立证明**。它对数据库理论的意味是直接的：Kolaitis 与 Vardi 早已指出，"**合取查询包含 = CSP**"，因此 CSP 二分一旦成立，**固定模板的查询包含复杂度立刻获得完整二分**。

一个猜想被解决，之所以在整个领域激起回响，正是因为它是一大批"分类式开放问题"的共同地基。这也是本册把二分定理列为中心范式的根本理由：**你想问"某个查询语言落在哪一档"，最有力的办法就是把它变成 CSP，看二分能不能套上去。**

## 三、问题地图

本册六个问题，可以按"它们各自的难处在哪一层"排成一张图。

**最纯的语言层**：

- [#74 查询包含](problems/74-query-containment.md)：CQ 层已被完整解决（布尔 NP 完全、含不等式仍 NP 完全、一般版本升至 $\Pi^P_2$ 完全），开放的是**介于 CQ 与一阶演算之间**的中间层。
- [#75 聚合 FO 扩展](problems/75-fo-with-aggregates.md)：给 FO 加上 `SUM` / `AVG` 后，精确表达力与数据复杂度**尚无公认答案**——本册最"无路可循"的一题。

**数据不确定性的三种形态**：

- [#77 概率数据库 MPD](problems/77-mpd-probabilistic-db.md)：概率不确定性；存在"无投影极易、带投影跳到 $\#\mathrm{P}$ 完全"的**阶跃相变**。
- [#79 不完全信息查询应答](problems/79-incomplete-information-query.md)：缺失值不确定性；数据交换 + CQ 给出确定的 $\mathrm{P}$ 结果，一般情形开放。
- [#76 软修复全二分](problems/76-soft-repair-dichotomy.md)：冲突不确定性；**硬修复**二分已相当成熟，**软修复**完整二分仍开放。

**代数与递归层**：

- [#78 Datalog 溯源](problems/78-datalog-provenance.md)：非递归溯源半环框架完备，**递归情形**是核心难点。

一条清晰的**依赖链**贯穿全册：

- [#74](problems/74-query-containment.md) → [#76](problems/76-soft-repair-dichotomy.md) / [#79](problems/79-incomplete-information-query.md)：包含问题提供"约束下判定蕴含"的方法论原型，CQA 与确定答案都建立在它之上。
- [#77](problems/77-mpd-probabilistic-db.md) ↔ [#78](problems/78-datalog-provenance.md)：概率求值与溯源是同一代数（半环 / K-关系）的两个侧面。
- [#76](problems/76-soft-repair-dichotomy.md) ↔ [#77](problems/77-mpd-probabilistic-db.md)：软修复的"最优解释"与概率语义的"最可能世界"是对偶的优化问题。
- [#75](problems/75-fo-with-aggregates.md) ↔ [#78](problems/78-datalog-provenance.md)：聚合语义与聚合溯源共享同一套代数工具。

## 四、推荐阅读顺序

**第一阶段：看本册的"干净"样本**

1. [#74 查询包含问题](problems/74-query-containment.md)——本册的"母问题"，格式最完整，且拥有真正的精确二分（含 CSP 二分）。
2. [#77 概率数据库中的最可能数据库问题](problems/77-mpd-probabilistic-db.md)——体会"相变"：同一查询语言，投影与否决定 P 与 $\#\mathrm{P}$ 的分界。

**第二阶段：不确定性三形态**

3. [#79 不完全信息下的查询应答](problems/79-incomplete-information-query.md)（缺值）→
4. [#76 软修复的全二分定理](problems/76-soft-repair-dichotomy.md)（冲突）。

注意逐步比较：**这三题共用"对所有可能世界 / 修复取全体交集"的语义骨架**，差别只在可能世界的构造方式。

**第三阶段：代数与递归**

5. [#78 Datalog 的溯源计算](problems/78-datalog-provenance.md)——进入半环代数，理解递归为何是分水岭。
6. [#75 支持 SUM 和 AVG 聚合的 FO 扩展](problems/75-fo-with-aggregates.md)——本册最开放的一题，读完前五篇再来体会"缺乏统一工具"是什么状态。

## 五、阅读须知

**第一，二分是"精确刻画"，不等于"上界或下界"。** 本册的核心概念是**精确二分**：要么在 P 中、要么完全，没有中间档。读到某个结论时，请先分清它说的是**上界**（存在算法）、**下界**（不可能），还是**精确刻画**（两者相接）。

**第二，条件性与版本区分。** 包含问题的复杂度**随版本而变**（布尔 / 带投影 / 含不等式 / 一般有序域），概率查询求值**随查询结构而变**（分层 / 非分层），确定答案**随信息模型而变**（空值 / c-table / 数据交换）。剥离版本去引用结论，几乎必然出错。

**第三，`[待核实]` 是承诺，不是装饰。** 本册若干问题（尤其 [#76 软修复](problems/76-soft-repair-dichotomy.md)、[#78 Datalog 溯源](problems/78-datalog-provenance.md)、[#75 聚合逻辑](problems/75-fo-with-aggregates.md)）的专门文献本档案作者无法全部核对到原文，相关陈述已如实标注 `[待核实]` 或写成方向性描述。请勿把带此标记的内容当作确定结论引用。

**第四，本册不提供解法。** 这六个问题中，[#74](problems/74-query-containment.md)、[#75](problems/75-fo-with-aggregates.md)、[#77](problems/77-mpd-probabilistic-db.md)、[#78](problems/78-datalog-provenance.md)、[#79](problems/79-incomplete-information-query.md) 标为 `OPEN`，[#76](problems/76-soft-repair-dichotomy.md) 标为 `PARTIAL`，均无完整解答。本册的价值在于画出"卡点地图"——**某个查询语言的表达能力与判定复杂度，究竟精确落在哪里**——而不在于给出答案。

---

**相关阅读**：[PROBLEMS.md](../../PROBLEMS.md) 索引总表 · [METHODOLOGY.md](../../METHODOLOGY.md) 状态分级与障碍详解 · [TEMPLATE.md](../../TEMPLATE.md) 档案标准格式。跨册对照可见 [Vol.01 计算复杂性理论](../01-complexity-theory/README.md)（CSP 二分、近似硬度的方法论母体）与 [Vol.02 算法与数据结构](../02-algorithms-data-structures/README.md)（"按图类逐类定复杂度"的同构实践）。
