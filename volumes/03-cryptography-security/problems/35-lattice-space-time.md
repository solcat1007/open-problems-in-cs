# #35 格问题的时空硬度

**状态**：`OPEN`
**领域**：密码学与信息安全
**首次提出**：格问题困难性的系统研究始于 Ajtai（1990 年代）；从"时间—空间权衡"角度审视格问题，与后量子密码学对资源受限攻击者的关切相关，其确切提出者 `[待核实]`。
**参与门槛**：需要新的数学工具

---

## 一句话概述

当我们**同时**限制时间与内存（空间）时，格上的困难问题（如最短向量问题）有多难？能否证明它在两个资源维度上都难以求解？

## 形式化陈述

**格（lattice）**：由线性无关的基向量 $b_1, \dots, b_m \in \mathbb{R}^n$ 张成的离散加法子群

$$\mathcal{L} = \Big\{\textstyle\sum_{i=1}^m z_i b_i : z_i \in \mathbb{Z}\Big\}.$$

**最短向量问题（shortest vector problem, SVP）**：给定格基，求非零格向量中欧氏范数最小者。记其长度为 $\lambda_1(\mathcal{L})$。

**判定（间隙）版本 $\mathrm{GapSVP}_\gamma$**：区分"$\lambda_1(\mathcal{L}) \le 1$"与"$\lambda_1(\mathcal{L}) > \gamma$"两种情形。

**时空硬度问题（本档案的题意）**：刻画在**时间 $T(n)$ 与空间 $S(n)$ 同时受限**时求解 SVP 的可行性。一类标准形式是证明

$$\mathrm{SVP} \notin \mathrm{TISP}(T(n), S(n)),$$

即：不存在同时使用时间 $T(n)$ 与空间 $S(n)$ 的算法求解 SVP。问题是：能否对非平凡的 $(T, S)$ 证明此类结论？

（若题名"时空硬度"在原始清单中另有更具体的所指，本档案的上述形式化可能需要修正，标注 `[待核实]`。）

## 为什么困难

- **困难性基础本身是条件性的。** Ajtai 1996 给出从最坏情况到平均情况的归约（格密码学的基石），但**最坏情况近似 SVP 是否 NP 难**，只在受限意义下有结果：Ajtai 1998 在**随机归约**下证明 NP 难；Khot 2005 在**准多项式因子**下、假设 $\mathrm{NP} \not\subseteq \mathrm{RTIME}(2^{\mathrm{polylog}\,n})$ 时证明困难性。这些都是非无条件结论。
- **时空下界比时间下界更难。** 已有的时间—空间权衡下界技术（例如针对 SAT 的）非常脆弱，且同样受相对化等原理性障碍限制。
- **"时间难"不自动意味着"空间难"。** 一个算法可能时间上受限、但在内存充足时可行（格筛法正是以空间换时间的典型）。要证明时空**双重**困难，需要更强的工具。
- **与后量子密码学的关系是双刃的。** 若只能证明时间困难而无法证明空间困难，则内存充足的攻击者可能获得优势，这直接影响安全参数的选择。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（最坏—平均归约） | SVP/CVP 的最坏情况到平均情况归约 | Ajtai, STOC 1996 |
| 上界（随机归约下的 NP 难） | 近似 SVP 在随机归约下 NP 难（特定因子） | Ajtai, STOC 1998 |
| 上界（强近似因子） | SVP 在因子 $2^{(\log n)^{1-\varepsilon}}$ 下困难，假设 $\mathrm{NP} \not\subseteq \mathrm{RTIME}$ | Khot, JACM 2005 |
| 上界（最近格点问题） | CVP 的近多项式因子近似困难 | Håstad, Combinatorica 1988；Dinur-Kindler-Raz-Safra, Combinatorica 2003 |
| 下界（结构性） | SVP $\in \mathrm{NP} \cap \mathrm{coNP}$（相应因子下） | Aharonov & Regev, JACM 2005 |
| 下界（时空） | 关于格问题的精确时间—空间权衡下界 | 无已知非平凡结果 `[待核实]` |
| 条件性（密码学） | 若 LWE 假设成立（相应参数），则基于 LWE 的体制安全 | Regev, STOC 2005 |
| 构造（陷门） | 格密码所需的高效陷门 | Micciancio & Peikert, STOC 2008（扩展版 2012） |

**关键事实**：格密码学的安全基础是一系列**条件性**归约。其中"时空硬度"这一更强的命题，目前**没有**与纯时间硬度同等地位的、被广泛接受的结果。

## 解法现状与可行攻击路径

### 已解决的部分

- **平均情况困难性的基础已建立**：Ajtai（STOC 1996）的最坏情况到平均情况归约——格密码学大厦的地基，已封顶。
- **受限意义下的 NP 难已有确定结论**：Ajtai（STOC 1998）在**随机归约**下证明近似 SVP NP 难；Khot（JACM 2005）在准多项式因子下、假设 $\mathrm{NP} \not\subseteq \mathrm{RTIME}(2^{\mathrm{polylog}\,n})$ 时证明困难性——均带前提，但受限版本的困难性是确定的。
- **结构性刻画**：SVP（相应因子下）$\in \mathrm{NP} \cap \mathrm{coNP}$（Aharonov–Regev, JACM 2005）。
- **密码学应用侧已建成**：LWE 条件安全（Regev, STOC 2005）、高效陷门（Micciancio–Peikert, STOC 2008/2012）。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 强化最坏情况归约 | 在更弱的假设、更广的问题类上建立归约 | Ajtai 1996/1998 的地基已有 | 无条件的 NP 难仍缺；现有结果均为受限或条件性 |
| 移植时空权衡技术 | 把针对 SAT 等组合问题的时间—空间权衡下界搬到格问题 | 技术存在（Buss–Williams 结果方向） | 格问题缺少 SAT 式规整组合结构；时空下界技术本身脆弱且受相对化等原理性障碍限制 |
| 分析筛法的时空权衡 | 刻画格筛法的内存—时间权衡 | 可产出攻击上界，反过来约束安全参数 | 方向与下界相反，只能约束参数、不能证硬度 |
| 条件性下界 | 在 LWE/SIS 等假设成立的前提下导出时空下界 | 被认为目前最有可能产出成果的路线 | 尚无与纯时间硬度同等地位、被广泛接受的结果 |

### 已堵死的路径

- **"时间难 ⇒ 空间也难"的自动推广**：时间下界不自动给出时空双重下界——格筛法正是以空间换时间的典型，内存充足的攻击者可能获得优势；该推广路线被问题结构本身阻断。
- **无条件的（一般近似因子）NP 难**：目前只有随机归约（Ajtai 1998）与附加假设（Khot 2005）下的受限结果——直接的无条件困难性路线没有产出。
- **直接套用现有的时空下界通用技术**：已有技术非常脆弱且受相对化等原理性障碍限制——不加改造地搬用现有工具证明格问题 TISP 下界的路线被工具现状阻断。

### 裁决

**路径已知，尚需突破**

时间维度的困难性基础（最坏—平均归约、受限 NP 难）已建成，条件性路线（从 LWE/SIS 导出时空下界）方向明确；卡点是"时间与空间同时受限"的要求超出当前下界技术的射程，且格问题缺乏 SAT 式的规整结构可供移植。

## 研究路线图

**路线一：强化最坏情况归约。** Ajtai 的归约是整座格密码学大厦的地基。能否在更弱的假设下、对更广的问题类建立归约？

**路线二：移植时空权衡技术。** 把针对 SAT 等组合问题的时间—空间权衡技术（参见 [#1 P vs NP](../../01-complexity-theory/problems/01-p-vs-np.md) 中 Buss-Williams 的结果方向）搬到格问题上。卡点：格问题缺少 SAT 那样规整的组合结构。

**路线三：分析筛法的时空权衡。** 格筛法（lattice sieving）本身就有内存与时间的权衡。这条路线产出的是**算法上界**（即更快的攻击），与下界方向相反，但能反过来约束安全参数。

**路线四：条件性下界。** 在 LWE/SIS 等假设成立的前提下，能导出哪些时空下界？这是目前最有可能产出成果的路线。

## 关键文献

1. **Ajtai, M.** *Generating Hard Instances of Lattice Problems*. STOC 1996. — 格密码学的基石：最坏—平均归约。
2. **Ajtai, M.** *The Shortest Vector Problem in $L_2$ is NP-hard for Randomized Reductions*. STOC 1998. — 随机归约下的 NP 难。
3. **Håstad, J.** *Dual Vectors and Lower Bounds for the Nearest Lattice Point Problem*. Combinatorica, 1988. — 近似困难性的早期工作。
4. **Khot, S.** *Hardness of Approximating the Shortest Vector Problem in Lattices*. JACM, 2005. — 准多项式因子下的困难性。
5. **Regev, O.** *On Lattices, Learning with Errors, Random Linear Codes, and Cryptography*. STOC 2005. — LWE，后量子密码学的核心假设。
6. **Micciancio, D., Regev, O.** *Worst-Case to Average-Case Reductions Based on Gaussian Measures*. FOCS 2004. — 归约技术。
7. **Micciancio, D., Peikert, C.** *Trapdoors for Hard Lattices and New Cryptographic Constructions*. STOC 2008（扩展版 2012）. — 高效陷门构造。
8. **Aharonov, D., Regev, O.** *Lattice Problems in NP ∩ coNP*. JACM, 2005. — 结构性结果。
9. **Dinur, I., Kindler, G., Raz, R., Safra, S.** *Approximating CVP to Within Almost-Polynomial Factors is NP-Hard*. Combinatorica, 2003.
10. **Micciancio, D., Goldwasser, S.** *Complexity of Lattice Problems: A Cryptographic Perspective*. Kluwer, 2002. — 格问题复杂性的标准专著。

## 常见误区

- **误区：格问题已被证明是 NP 难的。** —— 只有受限结果（随机归约、特定近似因子、或附加假设），没有无条件结论。
- **误区：格密码是"信息论安全"的。** —— 它是**计算性**安全，建立在未证明、且属于**平均情况**的假设上；平均情况困难性由最坏—平均归约建立，而这些归约本身也是条件性的。
- **误区：时间难就意味着空间也难。** —— 这正是本题要问的。两者能否**同时**受限，目前没有定论。
- **误区：筛法的最新加速证明格密码不安全。** —— 算法加速给出的是**上界**（攻击更快）。需要与具体安全参数规模对比；单个加速不等于"被攻破"。
- **条件性提醒**：凡"基于 LWE 的安全性"这类表述，都必须带上前提——"**若 LWE 假设（在相应参数下）成立**，则……"。省略前提就是错误的。

## 可运行实验

**`experiments/lattice_svp_small.py`** — 小维度 SVP 的精确求解与增长实测

脚本对小维度格（例如 $n \le 20$）用枚举法精确求最短向量，测量运行时间随维数增长（枚举法最坏情形为指数级）。

**能观察到**：最坏情形枚举成本随维数快速增长；而 LLL 等**近似**算法在典型随机格基上往往远快于最坏情形。

**绝不能说明**：

1. 有限维数的实测**无法**推出渐近结论；
2. "近似算法在典型实例上很快"恰恰说明"具体实例易"与"最坏情况难"是两回事，但它**不构成**对最坏情况下界的任何证据；
3. 该实验**无法**为任何密码系统提供安全参数——安全参数需要的是**攻击复杂度的下界**（或至少是基于已知最优攻击的严格估计），而非小规模曲线。

## 延伸阅读

- **专著**：Micciancio & Goldwasser（文献 [10]）系统讲解格问题的复杂性。
- **假设来源**：Regev 的 LWE 论文（文献 [5]）是现代格密码学的起点。
- **相关档案**：[#32 整数分解](32-integer-factoring.md)、[#13 单向函数](../../01-complexity-theory/problems/13-one-way-functions.md)、[#14 公钥密码学](../../01-complexity-theory/problems/14-public-key-crypto.md)、[#59 量子纠错](../../05-quantum-computing/problems/59-quantum-error-correction.md)。
