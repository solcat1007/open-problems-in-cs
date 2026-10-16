# #9 PH vs PSPACE

**状态**：`OPEN-BARRIER`
**领域**：计算复杂性理论
**首次提出**：1970 年代，随多项式层级与空间复杂性的研究出现（Stockmeyer 1976；Stockmeyer–Meyer 1973）
**参与门槛**：需要新的数学工具

---

## 一句话概述

用"每一层量词交替"逐层堆积起来的**多项式层级**，最终能否覆盖整个**多项式空间**？

## 形式化陈述

**多项式层级 PH（Polynomial Hierarchy）** 递归定义为

$$\Sigma_0^p = \Pi_0^p = \mathrm{P}, \qquad \Sigma_{k+1}^p = \mathrm{NP}^{\Sigma_k^p}, \qquad \Pi_{k+1}^p = \mathrm{co\text{-}}\Sigma_{k+1}^p$$

$$\mathrm{PH} = \bigcup_{k \geq 0} \Sigma_k^p$$

直观上，$\Sigma_k^p$ 对应"存在 $k$ 个量词、以 $\exists$ 开头、每个量词后用多项式时间谓词"的判定问题，即量词交替层数为 $k$。已知

$$\mathrm{P} \subseteq \mathrm{NP} \subseteq \Sigma_2^p \subseteq \cdots \subseteq \mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}} \subseteq \mathrm{PSPACE}$$

其中 $\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}}$ 是 **Toda 定理**（1991）。

**问题**：$\mathrm{PH} \overset{?}{=} \mathrm{PSPACE}$

**关键等价刻画**：由于 TQBF（量化布尔公式）是 PSPACE 完全的，而 TQBF 的判定恰好是"量词交替"问题，有

> $\mathrm{PH} = \mathrm{PSPACE}$ 当且仅当存在某个 $k$ 使 $\Sigma_k^p = \mathrm{PSPACE}$。

也就是说，**$\mathrm{PH} = \mathrm{PSPACE}$ 等价于多项式层级坍缩到某个有限层**。反过来，若 PH 坍缩（$\mathrm{PH} = \Sigma_k^p$）并**不**自动推出 $\mathrm{PH} = \mathrm{PSPACE}$——坍缩只是必要条件。

这是一个极有价值的观察：它把"层级能否覆盖空间"的问题，转化成了"层级是否坍缩"的问题，后者是复杂性理论中最古老的结构性问题之一。

## 为什么困难

### （一）相对化障碍

取 $A$ 为 PSPACE 完全集（如 TQBF）。由于 $A \in \mathrm{PSPACE}$ 且 PSPACE 相对 $A$ 不增大，可得 $\mathrm{PH}^A = \mathrm{PSPACE}^A = \mathrm{PSPACE}$——存在**塌缩**的神谕世界；同时存在使 $\mathrm{PH}^A \neq \mathrm{PSPACE}^A$ 的神谕。两个方向都存在，故任何相对化技术都无法解决本题。

### （二）继承三重障碍

$\mathrm{NP} \subseteq \mathrm{PH} \subseteq \mathrm{PSPACE}$，所以 $\mathrm{PH} \neq \mathrm{PSPACE}$ 蕴含 $\mathrm{P} \neq \mathrm{NP}$。任何分离 PH 与 PSPACE 的论证也都分离 P 与 NP，因此自然化（Razborov–Rudich 1997）与代数化（Aaronson–Wigderson 2009）障碍在此**全部适用**。本问题与 P vs PSPACE 一样，属于"比 P vs NP 更强"的一类。

### （三）层级坍缩后果的"反向不对称"

证明 $\mathrm{PH} = \mathrm{PSPACE}$ 会**引发坍缩**（层级塌到某有限层），这在结构上是一个极强的后果。而证明 $\mathrm{PH} \neq \mathrm{PSPACE}$ 需要展示"无限层"区别于"多项式空间"——同样是硬骨头。由于坍缩与相等互为条件，本问题在双向都缺乏可行路线。

### （四）与坍缩假设的纠缠

已知若干假设会导致 PH 坍缩：

- $\mathrm{NP} = \mathrm{co\text{-}NP} \Rightarrow \mathrm{PH} = \mathrm{NP}$（坍缩到第一层）；
- $\mathrm{NP} \subseteq \mathrm{P/poly} \Rightarrow \mathrm{PH} = \Sigma_2^p$（Karp–Lipton 定理）。

这些结论说明：**PH 坍缩是"低成本"的假设**，而 $\mathrm{PH} = \mathrm{PSPACE}$ 要求坍缩同时等于整个 PSPACE，比单纯坍缩更强。这层加码，正是本问题难以推进的又一原因。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界 | $\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}} \subseteq \mathrm{PSPACE}$ | Toda, 1991（$\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}}$） |
| 上界 | $\mathrm{PSPACE}$ 有完全问题 TQBF；$\mathrm{PSPACE} = \mathrm{NPSPACE}$ | Savitch, 1970 |
| 结构性 | $\mathrm{PH} = \mathrm{PSPACE} \iff \exists k,\ \Sigma_k^p = \mathrm{PSPACE}$（即层级坍缩） | 标准结论 |
| 结构性 | $\mathrm{NP} = \mathrm{co\text{-}NP} \Rightarrow \mathrm{PH} = \mathrm{NP}$ | 标准结论 |
| 结构性 | $\mathrm{NP} \subseteq \mathrm{P/poly} \Rightarrow \mathrm{PH} = \Sigma_2^p$ | Karp & Lipton, 1980 |
| 下界 | **无任何无条件分离**；不能排除 $\mathrm{PH} = \mathrm{PSPACE}$ | — |

**上界与下界的区分**：上界方向已把 PH 牢牢夹在 $\mathrm{P}^{\#\mathrm{P}}$ 与 PSPACE 之间（Toda 定理是关键）；下界方向**完全空白**。

## 解法现状与可行攻击路径

### 已解决的部分

- **上界定位已解决**：Toda 定理（1991）证明 $\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}} \subseteq \mathrm{PSPACE}$，把 PH 在计数类与 PSPACE 之间的位置无条件钉住。
- **等价刻画已确立**：PH = PSPACE 当且仅当存在 $k$ 使 $\Sigma_k^p = \mathrm{PSPACE}$（即层级坍缩到某有限层）——"层级能否覆盖空间"已被转化为"层级是否坍缩"这一结构问题。
- **条件性坍缩定理**：NP = co-NP ⟹ PH = NP；NP ⊆ P/poly ⟹ PH = Σ₂ᵖ（Karp–Lipton 1980）——"坍缩是低成本的假设"这一图景已经清楚。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 坍缩假设下的结构研究 | 研究 PH 坍缩到第 $k$ 层的后果（近似算法、布尔函数分析等） | 产出条件性结论 | 不直接推进无条件分离 |
| 算法化下界 | 沿 Williams（2011）思路为更强电路类给出 SAT 加速算法以导出下界 | 强度不足以区分 PH 与 PSPACE | 所需强度远超当前水平 |
| 计数与层级的关系 | 利用 Toda 定理（PH ⊆ P^#P）研究 PH 在计数类中的位置，作为证明 PH ≠ PSPACE 的潜在跳板 | PH ⊆ P^#P 已证 | P^#P 与 PSPACE 之间的确切关系同样未知 |

### 已堵死的路径

- **相对化**：存在塌缩神谕（取 PSPACE 完全集 $A$，$\mathrm{PH}^A = \mathrm{PSPACE}^A = \mathrm{PSPACE}$）与分离神谕，两个方向的相对化世界都存在。
- **三重障碍全部适用**：$\mathrm{PH} \neq \mathrm{PSPACE}$ 蕴含 $\mathrm{P} \neq \mathrm{NP}$，故任何分离 PH 与 PSPACE 的论证也都分离 P 与 NP，自然化（Razborov–Rudich 1997）与代数化（Aaronson–Wigderson 2009）所排除的技术在此同样无效。
- 研究路线图明确列为已排除的：一切相对化或代数化论证。
- **"证明相等"一侧同样受阻**：PH = PSPACE 会引发层级坍缩到有限层这一极强的结构性后果，且坍缩只是必要条件——双向都缺乏可行路线。

### 裁决

**`原理上受限`**

本题与 P vs PSPACE 同属"比 P vs NP 更强"的一类，相对化、自然化、代数化三重障碍全部适用；上界方向已被 Toda 定理钉住，下界方向完全空白。

## 研究路线图

**路线一：坍缩假设下的结构研究**

研究"PH 坍缩到第 $k$ 层"会带来哪些后果（如对近似算法、对布尔函数分析的影响）。此路线产出**条件性结论**，不直接推进无条件分离。

**路线二：算法化下界**

沿用 Williams（2011）的思路，为更强电路类给出 SAT 加速算法以导出下界。目前强度不足以区分 PH 与 PSPACE。

**路线三：计数与层级的关系**

利用 Toda 定理（$\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}}$）研究 PH 在计数类中的位置，作为证明 $\mathrm{PH} \neq \mathrm{PSPACE}$ 的潜在跳板。卡点在于：$\mathrm{P}^{\#\mathrm{P}}$ 与 PSPACE 之间的确切关系同样未知。

**已被排除的路线**：一切相对化或代数化论证。

## 关键文献

1. **Stockmeyer, L.** *The polynomial-time hierarchy.* Theoretical Computer Science 3(1), 1976. — 多项式层级的系统定义与研究。
2. **Stockmeyer, L., Meyer, A.** *Word problems requiring exponential time.* STOC 1973. — 引入多项式层级并证明 TQBF 是 PSPACE 完全的。
3. **Karp, R., Lipton, R.** *Some connections between nonuniform and uniform complexity classes.* STOC 1980. — Karp–Lipton 定理。
4. **Toda, S.** *PP is as hard as the polynomial-time hierarchy.* SIAM J. Comput. 20(5), 1991. — $\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}}$。
5. **Savitch, W.** *Relationships between nondeterministic and deterministic tape complexities.* J. Comput. Syst. Sci. 4(2), 1970. — $\mathrm{PSPACE} = \mathrm{NPSPACE}$。
6. **Baker, T., Gill, J., Solovay, R.** *Relativizations of the P =? NP question.* SIAM J. Comput. 4(4), 1975. — 相对化障碍。
7. **Razborov, A., Rudich, S.** *Natural proofs.* J. Comput. Syst. Sci. 55(1), 1997. — 自然化障碍。
8. **Aaronson, S., Wigderson, A.** *Algebrization: A New Barrier in Complexity Theory.* ACM Trans. Comput. Theory 1(1), 2009. — 代数化障碍。
9. **Arora, S., Barak, S.** *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009. — 标准教材，第 3、5 章。
10. **Papadimitriou, C.** *Computational Complexity.* Addison-Wesley, 1994. — 经典教材，第 17 章系统讨论多项式层级。

## 常见误区

- **误区：PH 是一个具体的类，像 NP 一样。** —— PH 是**无穷多个类的并**（$\bigcup_k \Sigma_k^p$），不是一个有限的、有完全问题的类（除非它坍缩）。
- **误区：$\mathrm{PH} = \mathrm{PSPACE}$ 只是一个"等号"，无关紧要。** —— 它等价于**层级坍缩到某有限层**，是一个极强的结构断言。因此它比普通的类相等假设"更重"。
- **误区：若 PH 坍缩，则 $\mathrm{PH} = \mathrm{PSPACE}$。** —— 方向错。$\mathrm{PH} = \mathrm{PSPACE}$ **蕴含**坍缩；坍缩**不蕴含** $\mathrm{PH} = \mathrm{PSPACE}$。坍缩只是必要条件。
- **误区：$\mathrm{PH} \subseteq \mathrm{PSPACE}$ 说明"PH 就是 PSPACE 的弱化版"。** —— 包含关系不等于相等。$\mathrm{PH} \subsetneq \mathrm{PSPACE}$ 是主流猜想，但**未被证明**；下界方向无任何无条件结果。
- **误区：Toda 定理"解决"了 PH vs PSPACE。** —— 它给出 $\mathrm{PH} \subseteq \mathrm{P}^{\#\mathrm{P}}$，是一个**上界**；它把 PH 放进计数类，但 $\mathrm{P}^{\#\mathrm{P}}$ 与 PSPACE 的关系仍然未知，问题并未解决。
- **误区：把 Karp–Lipton 定理读成"PH 会坍缩"。** —— 它是**条件性**结论："**若** $\mathrm{NP} \subseteq \mathrm{P/poly}$，**则** $\mathrm{PH} = \Sigma_2^p$"。去掉前提即错误。

## 可运行实验

**`experiments/ph_levels_game.py`** — 用"量词博弈"区分层级与 PSPACE

脚本实现小型**量词交替博弈**：参数 $k$ 控制量词交替层数。对固定输入长度，比较 $k$ 层交替（对应 $\Sigma_k^p$ 型问题）与一般 TQBF（对应 PSPACE）在**判定复杂度**上的差异——例如用带记忆化的 minimax 搜索，观察状态空间随 $k$ 与输入规模的膨胀。

**它能验证的已知部分结果**：量词交替层数确实对应"博弈的回合数"，第 $k$ 层对应 $k$ 个回合的博弈；层数增加会显著扩大所需的状态空间。这与 $\Sigma_k^p$ 的直觉一致。

**这个实验不能说明什么**：

- 它只演示了**定义层面的对应关系**，**完全不能**推出 PH 与 PSPACE 的类关系，更无法触及坍缩问题。
- 有限规模、特定实例的性能与渐近类分离无关。
- 它无法触及由相对化/自然化/代数化障碍限制的任何证明路线。

## 延伸阅读

- **教材**：Arora & Barak（文献 [9]）第 3 章（层级）、第 5 章；Papadimitriou（文献 [10]）第 17 章。
- **进阶**：Toda 定理（文献 [4]）与计数复杂性是理解 PH 上界的必读内容。
- **相关档案**：[#2 NP vs Co-NP](02-np-vs-conp.md) 描述第一层的坍缩；[#3 P vs PSPACE](03-p-vs-pspace.md) 是本题的直接母问题；[#1 P vs NP](01-p-vs-np.md) 的结论会连带影响整个层级图景；[#18 电路下界](18-circuit-lower-bounds.md) 与 Karp–Lipton 型坍缩结论相关。
