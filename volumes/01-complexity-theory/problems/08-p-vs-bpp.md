# #8 P vs BPP

**状态**：`CONDITIONAL`
**领域**：计算复杂性理论
**首次提出**：1970 年代末，随随机化复杂性类的定义出现（Gill 1977；Adleman 1978）
**参与门槛**：需要新的数学工具

---

## 一句话概述

抛硬币的算法，是否总能被改写成不抛硬币、同样快的算法？

## 形式化陈述

**BPP（Bounded-error Probabilistic Polynomial time）**：由**双侧错误**的概率图灵机定义，机器在多项式时间内运行，使得

$$x \in L \implies \Pr[M(x) \text{ 接受}] \geq 2/3, \qquad x \notin L \implies \Pr[M(x) \text{ 接受}] \leq 1/3$$

误差界可任取 $> 1/2$ 的常数，重复运行即可压到任意小。

**问题**：$\mathrm{P} \overset{?}{=} \mathrm{BPP}$

已知 $\mathrm{P} \subseteq \mathrm{BPP} \subseteq \mathrm{PSPACE}$，且 BPP 有两个著名的**无条件**上界：

$$\mathrm{BPP} \subseteq \mathrm{P/poly}, \qquad \mathrm{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$$

**主流猜想**：$\mathrm{P} = \mathrm{BPP}$——随机性在多项式时间下不提供额外能力。

**本问题被标为 `CONDITIONAL` 的原因**：虽然 $\mathrm{P} = \mathrm{BPP}$ 本身仍在 **未证明的假设**下成立，但在"**硬度-随机性权衡（hardness-randomness tradeoff）**"这一纲领中，已有确定的**条件性定理**：**若某些函数足够难（需要指数规模电路），则 $\mathrm{P} = \mathrm{BPP}$**。这正是本档案要同时写清假设与结论的地方。

## 为什么困难

### （一）结构性上界的"距离"

无条件结果把 BPP 放进了 $\mathrm{P/poly}$ 与 $\Sigma_2^p \cap \Pi_2^p$，但两者都**不是 P**：$\mathrm{P/poly}$ 允许**多项式规模的非一致建议**，$\Sigma_2^p$ 允许**一层量词交替**。要把 BPP 降到 P，必须**去掉建议或去掉量词**，而这恰是当前技术的极限。

### （二）相对化障碍

存在使 $\mathrm{P}^A = \mathrm{BPP}^A$ 的神谕（取 $A$ 为 PSPACE 完全集即可，此时 $\mathrm{P}^A = \mathrm{BPP}^A = \mathrm{PSPACE}$），也存在使两者分离的神谕。因此任何相对化技术都无法解决本题；解决它必须依赖**非相对化**的硬度-随机性论证。

### （三）自然的证明方向是"条件性"的

去随机化的核心思路是：**用伪随机生成器（PRG）把随机比特替换为一段短的伪随机种子**。而构造 PRG 需要"困难函数"作为原料（Nisan–Wigderson 1994）。困难函数的**存在性**本身无从证明（它与电路下界、进而与自然化障碍纠缠，见 [#18 电路下界](18-circuit-lower-bounds.md)），所以整条推理链只能给出条件性结论。这不是绕路，而是这一问题目前**唯一可行的技术形态**。

### （四）与 P vs NP 的关系

$\mathrm{P} = \mathrm{NP}$ 蕴含 $\mathrm{P} = \mathrm{BPP}$：若 $\mathrm{P} = \mathrm{NP}$，则整个多项式层级坍缩为 P，而由 $\mathrm{BPP} \subseteq \Sigma_2^p$ 立得 $\mathrm{BPP} \subseteq \mathrm{P}$。但反之不然。本问题常被视为**比 P vs NP 更"乐观"**：即使 $\mathrm{P} \neq \mathrm{NP}$，$\mathrm{P} = \mathrm{BPP}$ 仍很可能成立。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（无条件） | $\mathrm{BPP} \subseteq \mathrm{P/poly}$ | Adleman, 1978；Bennett & Gill, 1981 |
| 上界（无条件） | $\mathrm{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$ | Sipser, 1983；Gács；Lautemann, 1983 |
| **条件性** | **若**存在 $\varepsilon>0$ 使 $\mathrm{E} \nsubseteq \mathrm{SIZE}(2^{\varepsilon n})$（即 $\mathrm{E}$ 中某函数需指数规模电路），**则** $\mathrm{P} = \mathrm{BPP}$ | Impagliazzo & Wigderson, 1997 |
| 条件性（弱形式） | **若** $\mathrm{E}$ 中存在超多项式电路复杂度的函数，**则** $\mathrm{BPP} \subseteq \mathrm{SUBEXP}$ | Nisan & Wigderson, 1994 |
| 下界 | **无任何无条件分离**；不能排除 $\mathrm{P} \neq \mathrm{BPP}$ | — |

**上界与下界的区分**：上界方向已知"BPP 落在 P/poly"与"BPP 落在 $\Sigma_2 \cap \Pi_2$"，条件性方向给出"在硬度假设下 BPP 落在 P"。下界方向**完全空白**。**引用条件性结论时务必带上前提**——这是本问题最容易被误引之处。

## 解法现状与可行攻击路径

### 已解决的部分

- **无条件的结构性上界**：$\mathrm{BPP} \subseteq \mathrm{P/poly}$（Adleman 1978；Bennett & Gill 1981）与 $\mathrm{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$（Sipser 1983；Gács；Lautemann 1983）——BPP 在类层级中的位置已被无条件钉住。
- **条件性主定理已确立**：若存在 $\varepsilon>0$ 使 $\mathrm{E} \nsubseteq \mathrm{SIZE}(2^{\varepsilon n})$，则 $\mathrm{P} = \mathrm{BPP}$（Impagliazzo & Wigderson 1997）；弱形式：若 E 中存在超多项式电路复杂度的函数，则 $\mathrm{BPP} \subseteq \mathrm{SUBEXP}$（Nisan & Wigderson 1994）。
- **逻辑关系已厘清**：P = NP ⟹ P = BPP（经层级坍缩与 $\mathrm{BPP} \subseteq \Sigma_2^p$），反向不成立。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 硬度-随机性权衡（主线） | 困难函数 → 伪随机生成器 → 去随机化 BPP | Nisan–Wigderson（1994）建立范式；Impagliazzo–Wigderson（1997）把假设削弱到"E 需要指数电路"即得 P = BPP | 假设本身（存在足够难的函数）无法无条件证明，属电路下界问题，受自然化障碍限制 |
| 非一致上界的收紧 | 从 $\mathrm{BPP} \subseteq \mathrm{P/poly}$ 出发研究能否去掉"建议" | 尚未产出确定的等号 | 去掉建议或去掉量词恰是当前技术的极限 |
| 特定问题的显式去随机化 | 对素性、连通性、多项式恒等测试等给确定性算法 | 产出具体算法而非类关系 | 逐问题推进，不直接给出类等式 |

### 已堵死的路径

- **相对化**：存在使 $\mathrm{P}^A = \mathrm{BPP}^A$ 的神谕（取 PSPACE 完全集即可）与分离的神谕，任何相对化技术无效；解决本题必须依赖**非相对化**的硬度-随机性论证。
- **无条件证明"困难函数存在"的直接路线**：它与电路下界纠缠、受自然化障碍限制，故整条推理链目前只能给出条件性结论——这不是绕路，而是这一问题目前唯一可行的技术形态。

### 裁决

**`条件可解`**

Impagliazzo–Wigderson（1997）已给出确定的条件性定理：只要 E 中存在需指数规模电路的函数（一个未证实的电路下界假设），就有 P = BPP；结论被完全绑定在该假设的可证性上，这正是本问题被标为 `CONDITIONAL` 的原因。

## 研究路线图

**路线一：硬度-随机性权衡（主线）**

核心链条：**困难函数 → 伪随机生成器 → 去随机化 BPP**。

- Nisan–Wigderson（1994）建立该范式：从弱随机性/困难性构造 PRG。
- Impagliazzo–Wigderson（1997）把假设削弱到"$\mathrm{E}$ 需要指数电路"，从而得到 $\mathrm{P} = \mathrm{BPP}$。

卡点：假设本身（"存在足够难的函数"）无法无条件证明，且属于电路下界问题，受自然化障碍限制。

**路线二：非一致上界的收紧**

从 $\mathrm{BPP} \subseteq \mathrm{P/poly}$ 出发，研究能否把"建议"去掉（例如在 $\mathrm{P/poly}$ 与 P 之间寻找更紧的类）。此路线尚未产出 $n$ 与 P 之间的确定等号。

**路线三：特定问题的显式去随机化**

对具体问题（如素性、连通性、多项式恒等测试）给出确定性算法。这是最"接地气"的方向，产出具体算法而非类关系。

**已被排除的路线**：一切相对化论证。

## 关键文献

1. **Gill, J.** *Computational complexity of probabilistic Turing machines.* SIAM J. Comput. 6(4), 1977. — 概率图灵机与 BPP 类的基础。
2. **Adleman, L.** *Two theorems on random polynomial time.* FOCS 1978. — 证明 $\mathrm{BPP} \subseteq \mathrm{P/poly}$。
3. **Bennett, C., Gill, J.** *Relative to a random oracle, $\mathrm{P}^A \neq \mathrm{NP}^A \neq \mathrm{co\text{-}NP}^A$ with probability 1.* SIAM J. Comput. 10(1), 1981. — $\mathrm{BPP} \subseteq \mathrm{P/poly}$ 与随机神谕技术。
4. **Sipser, M.** *A complexity theoretic approach to randomness.* STOC 1983. — $\mathrm{BPP} \subseteq \Sigma_2^p$ 等技术。
5. **Lautemann, C.** *BPP and the polynomial hierarchy.* Information Processing Letters 17, 1983. — 独立给出 $\mathrm{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$。
6. **Nisan, N., Wigderson, A.** *Hardness vs randomness.* J. Comput. Syst. Sci. 49(2), 1994. — 硬度-随机性权衡范式的奠基。
7. **Impagliazzo, R., Wigderson, A.** *P = BPP if E requires exponential circuits: Derandomizing the XOR lemma.* STOC 1997. — **本档案的核心条件性定理**。
8. **Impagliazzo, R.** *A personal view of average-case complexity.* Structures 1995. — "五个世界"框架，解释硬度与随机性的关系。
9. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 7、20 章。
10. **Goldreich, O.** *Computational Complexity: A Conceptual Perspective.* Cambridge University Press, 2008. — 随机化与去随机化的系统讨论。

## 常见误区

- **误区：$\mathrm{P} = \mathrm{BPP}$ 已被证明。** —— **未证明**。已知的是**条件性**定理："若 E 需要指数电路，则 P = BPP"。去掉前提的引用是错误引用。
- **误区：$\mathrm{BPP} \subseteq \mathrm{P/poly}$ 说明 $\mathrm{P} = \mathrm{BPP}$。** —— $\mathrm{P/poly}$ 允许非一致的建议串，比 P 更强。BPP 落在 P/poly 只说明"存在小电路"，不说明"存在多项式时间算法"。
- **误区：$\mathrm{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$ 说明 BPP 已接近 P。** —— $\Sigma_2$ 与 P 之间隔着整个多项式层级，这一步"降不下去"正是难点。
- **误区：既然去随机化需要"困难函数"，而困难函数是否存在未知，所以 $\mathrm{P} = \mathrm{BPP}$ 很可能不成立。** —— 逻辑关系搞反了。困难函数存在 → $\mathrm{P} = \mathrm{BPP}$；这只说"若假设成立则结论成立"。假设不成立也**不**意味着 $\mathrm{P} \neq \mathrm{BPP}$。
- **误区：随机性在实践中很有用，所以 $\mathrm{P} \neq \mathrm{BPP}$。** —— 实践中的随机算法之所以有效，是因为"真随机种子"易得；理论问题是**能否用确定性算法达到同样效率**。经验上的好用与类是否相等是两回事。
- **误区：把 BPP 与 RP、ZPP 混为一谈。** —— RP 是**单侧**错误，ZPP 是**零侧**错误（期望多项式时间）。$\mathrm{ZPP} \subseteq \mathrm{RP} \subseteq \mathrm{BPP}$，它们与 P 的关系各自独立，不能互相替换。

## 可运行实验

**`experiments/derandomize_identity_test.py`** — 随机多项式恒等测试的确定性改造

脚本实现**随机多项式恒等测试（Polynomial Identity Testing, PIT）**：对给定的算术电路或多项式表达式，随机代入若干点并检验是否恒为零，随后用**穷举小域**或**确定性枚举**在小规模上核对结果。统计随机算法的成功概率随试验次数的变化。

**它能验证的已知部分结果**：随机 PIT 用少量随机点即可高概率判定恒等（Schwartz–Zippel 引理），并可**重复运行**把错误率压到任意小——这是 BPP 算法的典型形态。

**这个实验不能说明什么**：

- 它演示的是**随机算法有效**，**完全不能**说明存在**确定性**多项式时间算法（即不能触及 $\mathrm{P} = \mathrm{BPP}$）。
- 有限规模与特定实例上的成功，无法推出渐近结论。
- 它无法触及硬度-随机性假设，也无法验证或否证 Impagliazzo–Wigderson 的条件性定理。

## 延伸阅读

- **教材**：Arora & Barak（文献 [9]）第 7、20 章；Goldreich（文献 [10]）关于伪随机与去随机化的章节。
- **框架**：Impagliazzo 的"五个世界"（文献 [8]）是理解硬度-随机性权衡的最佳入口。
- **相关档案**：[#1 P vs NP](01-p-vs-np.md) 是本题的母问题；[#13 单向函数](13-one-way-functions.md) 与本题共享"困难函数是否存在"这一假设基础；[#18 电路下界](18-circuit-lower-bounds.md) 是硬度假设的技术来源；[#6 L vs RL](06-l-vs-rl.md) 是对数空间版本的去随机化问题。
