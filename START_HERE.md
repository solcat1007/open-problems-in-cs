# 从这里开始 · 5 分钟导读

> v2.0 新增。第一次打开这个仓库？先读这一页，再决定往哪走。

---

## 30 秒版本

这是一个**开放问题档案库**，不是解题集。100 个问题，每个一份档案，
讲清楚四件事：**到底在问什么、为什么难到没人解出来、目前最好的结果是什么、哪些路走不通**。

**本仓库不声称解决任何问题。** 如果你在找「P vs NP 的证明」，这里恰好是告诉你为什么那种证明大概率错的地方。

---

## 三条阅读路线

### 路线 A：5 分钟速览（推荐所有人）

1. 读 [README.md](README.md) 的「这个仓库不是什么」一节（1 分钟）
2. 读 [PROBLEMS.md](PROBLEMS.md) 的统计表和 Vol.01 表格（2 分钟）
3. 随手打开 [Indexed 索引](INDEX.md) 里你听说过的一个编号，只看「一句话概述」和「常见误区」（2 分钟）

读完你应该能回答：**为什么「相对化障碍」让很多 P vs NP 的证明一提出就死掉。**

### 路线 B：1 小时深入理解一个问题

1. 先读 [METHODOLOGY.md](METHODOLOGY.md) 第二节「三个原理性障碍」
2. 从 [INDEX.md](INDEX.md) 的「可以立刻上手做实验」里挑一个问题
3. 按档案的七栏顺序读：形式化陈述 → 为什么困难 → 当前最好结果 → 研究路线图 → 关键文献 → 常见误区
4. 打开档案提到的 `experiments/` 代码，亲手跑一遍

### 路线 C：想贡献内容

直接看 [CONTRIBUTING.md](CONTRIBUTING.md)。**准确性是唯一的卖点**，宁可标 `[待核实]` 也不要编。

---

## 术语速查

| 术语 | 一句话解释 |
|---|---|
| `OPEN` | 完全开放，没有任何方向的确定性结论 |
| `OPEN-BARRIER` | 开放，且已知存在原理性障碍（某些证明路线不可能成功） |
| `CONDITIONAL` | 在某个尚未证明的假设下已有结论（如「若 ETH 成立则……」） |
| `PARTIAL` | 有重要部分结果，但核心未解 |
| `SETTLED-RECENT` | 近年已解决，档案保留作历史记录 |
| 相对化障碍 | 若某证明对任意预言机都成立，则它无法解决 P vs NP（Baker-Gill-Solovay） |
| 自然化障碍 | 大多数「对角化」证明无法区分 P 与 NP（Razborov-Rudich） |
| 代数化障碍 | 证明若只依赖多项式的代数性质，不足以分离复杂度类 |
| `[待核实]` | 结论来自二手来源，尚未核对原始论文，**不要引用** |

---

## 三种人分别该看什么

- **学生 / 科普读者**：[#1 P vs NP](volumes/01-complexity-theory/problems/01-p-vs-np.md) 的「常见误区」，[#45 LLM 幻觉](volumes/04-ai-machine-learning/problems/45-llm-hallucination.md) 的「形式化陈述」。
- **研究者**：先读 [METHODOLOGY.md](METHODOLOGY.md)，再按领域进入 `volumes/`，关注「研究路线图」与「文献」。
- **工程师 / 动手派**：从 [INDEX.md](INDEX.md) 的「可以立刻上手做实验」入口，跑 `experiments/` 里的代码。

---

## 仓库导航

| 我想…… | 去哪里 |
|---|---|
| 看全部 100 题 | [PROBLEMS.md](PROBLEMS.md) |
| 按状态 / 门槛 / 编号查找 | [INDEX.md](INDEX.md) |
| 了解分级标准与障碍 | [METHODOLOGY.md](METHODOLOGY.md) |
| 新增或修改档案 | [CONTRIBUTING.md](CONTRIBUTING.md) / [TEMPLATE.md](TEMPLATE.md) |
| 看可运行实验 | [experiments/README.md](experiments/README.md) |
| 找隐藏彩蛋 | [EASTER_EGG.md](EASTER_EGG.md)（先自己试试 ↑↑↓↓←→←→BA） |
