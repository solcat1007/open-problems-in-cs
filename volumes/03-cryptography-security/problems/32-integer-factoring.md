# #32 整数分解的多项式时间经典算法

**状态**：`OPEN`
**领域**：密码学与信息安全
**首次提出**：作为核心计算难题，其现代形式与 RSA 体制（Rivest-Shamir-Adleman, 1978）的安全性直接绑定。问题本身的朴素形式可追溯到数论早期。
**参与门槛**：需要新的数学工具

---

## 一句话概述

是否存在一台**经典**（非量子）计算机，能在多项式时间内把任意整数分解为质因数？

## 形式化陈述

给定整数 $N$，记 $n = \log N$ 为其输入长度（位数）。任务是求出质因数分解

$$N = p_1^{e_1} \, p_2^{e_2} \cdots p_k^{e_k}.$$

**判定版本**：$\mathrm{FACTOR} = \{\langle N, k \rangle : N \text{ 有一个质因子 } \le k\}$。

已知的归属关系：

- $\mathrm{FACTOR} \in \mathrm{NP}$（给出一个因子即可验证它整除 $N$ 且 $N$ 的余部也符合要求）；
- $\mathrm{FACTOR} \in \mathrm{coNP}$（其补问题的证书同样容易验证）；
- $\mathrm{FACTOR} \in \mathrm{BQP}$（Shor 给出多项式时间量子算法）。

**开放问题**：$\mathrm{FACTOR} \overset{?}{\in} \mathrm{P}$。

**必须与"素性检测"区分**：判定 $N$ 是否为素数的 $\mathrm{PRIMES}$ 已于 2002 年被证明属于 $\mathrm{P}$（Agrawal-Kayal-Saxena）。也就是说，"判断 $N$ 是不是素数"是容易的，而"找出它的因子"是否容易，至今未知。把两者混为一谈，是本题最常见的错误。

## 为什么困难

- 分解缺乏"组合完全性"这类可依托的结构。它既不像 SAT 那样有一个 NP 完全性可以借用，也不像图论问题那样有丰富的组合工具。它落在 $\mathrm{NP} \cap \mathrm{coNP}$ 之中，而对这一交集的成员，我们几乎没有任何**无条件**的下界工具。
- 已知的经典算法都是**亚指数**的，而非多项式。数域筛法的复杂度形如
  $$L_N\!\left[\tfrac13, c\right] = \exp\!\left(O\!\left((\log N)^{1/3} (\log\log N)^{2/3}\right)\right),$$
  比指数好得多，但距离多项式仍有关键差距。
- 与一切构造性下界一样，"不存在多项式算法"这一命题要面对的证明障碍，同样适用于此类问题。
- 一个常被忽略的事实：分解与 RSA 之间**没有**已被证明的等价性。破译 RSA 未必需要分解——Boneh 与 Venkatesan 在代数/一般环归约模型下给出了分离结果。

## 当前最好结果

| 方向 | 已知最好结果 | 出处 |
|---|---|---|
| 上界（量子） | 多项式时间量子算法 | Shor, FOCS 1994（正式发表 SIAM J. Comput. 1997） |
| 上界（经典，通用） | 数域筛法，亚指数复杂度 $L_N[1/3, c]$ | Lenstra-Lenstra-Manasse-Pollard, STOC 1990 |
| 上界（经典，寻找小因子） | 椭圆曲线分解法（ECM） | Lenstra, Ann. of Math. 1987 |
| 等价性 | Rabin 体制的破译等价于分解 | Rabin, MIT/LCS/TR-212, 1979 |
| 对比 | 素性检测（PRIMES）$\in \mathrm{P}$ | Agrawal-Kayal-Saxena, Ann. of Math. 2002 |
| 结构性（分离方向） | 不存在高效的代数归约把分解归约为破译 RSA | Boneh & Venkatesan, EUROCRYPT 1998 |
| 下界 | 无已知非平凡下界 | — |

**关键事实**：我们既不知道 $\mathrm{FACTOR}$ 是否在 $\mathrm{P}$ 中，也**不知道**它是否 $\mathrm{NP}$ 难。事实上，它普遍**不**被认为是 $\mathrm{NP}$ 难的。它在密码学中的地位，完全建立在"未证明的困难性假设"之上。

## 解法现状与可行攻击路径

### 已解决的部分

- **量子情形已完整解决**：Shor（FOCS 1994 / SIAM J. Comput. 1997）给出多项式时间量子算法——"分解在 BQP 中"这一真子情形已封顶。
- **相关的真子问题（素性检测）已解决**：$\mathrm{PRIMES} \in \mathrm{P}$（Agrawal–Kayal–Saxena, 2002/2004）——"判定 $N$ 是否为素数"与"找出它的因子"已被明确分离。
- **等价性刻画**：破译 Rabin 体制等价于分解（Rabin, 1979）。
- **受限情形**：寻找小因子有高效算法（椭圆曲线分解法 ECM, Lenstra, 1987）；经典通用算法达到亚指数 $L_N[1/3, c]$（数域筛法）。

### 可行的攻击路径

| 路径 | 核心手段 | 当前状态 | 卡点 |
|---|---|---|---|
| 改进经典算法的复杂度 | 改进数域筛法的 $L_N[\cdot]$ 指数 | 数域筛法自 1990 年代起基本主导 | 是否存在更好的指数尚无定论 |
| 下界与归约 | 把分解归约为已知困难问题，或利用与离散对数的（反方向）归约联系 | 仅有零散联系（如合数模下离散对数与分解的关系 `[待核实]`） | 无有效的无条件下界工具；分解落在 NP ∩ coNP，对这类成员几乎无下界技术 |
| 理解与 RSA 的分离 | 在更宽的模型下扩展 Boneh–Venkatesan 的分离 | 代数/一般环归约模型下已有分离（1998） | 更宽的模型下能否给出更强分离不清楚 |
| 量子路线 | Shor 算法 | 已多项式时间 | 剩余是工程问题（#59），非本题的理论内容 |

### 已堵死的路径

- **依托 NP 完全性的困难性论证**：分解落在 NP ∩ coNP 中，且普遍不被认为是 NP 难的——"证明分解 NP 难以借力组合完全性"不是可行路线（该方向也没有任何已知结果）。
- **"破译 RSA ⇒ 分解"的代数归约方向**：Boneh–Venkatesan（EUROCRYPT 1998）在代数/一般环归约模型下给出分离——在受限定模型中，"分解是 RSA 安全的必经之路"已被否定（但这不是一般模型下的分离）。

### 裁决

**路径已知，尚需突破**

攻击方向清楚（改进 $L_N$ 指数、寻找归约、扩展与 RSA 的分离），量子侧已彻底解决；卡点是分解落入 NP ∩ coNP 后无条件与条件性下界工具双双缺位，且它与 RSA 的关系在一般模型下未定。

## 研究路线图

**路线一：改进经典算法的复杂度。** 数域筛法自 1990 年代起基本主导；是否存在更好的 $L_N[\cdot]$ 指数，尚无定论。

**路线二：下界。** 目前没有有效工具。可以尝试的角度是把分解归约为某个已知困难问题；但迄今为止更常见的是反方向的关系——例如在合数模下，求解离散对数与分解之间存在归约联系，其精确归属与成立条件需核对原始文献 `[待核实]`。

**路线三：理解与 RSA 的分离。** Boneh-Venkatesan 的分离限于代数/一般环模型。在更宽的模型下能否给出更强的分离，尚不清楚。

**路线四：量子路线。** Shor 已给出多项式时间上界；工程上如何在足够大的整数上真正运行，是 [#59 量子纠错](../../05-quantum-computing/problems/59-quantum-error-correction.md) 的问题，而非本题的问题。

## 关键文献

1. **Rivest, R., Shamir, A., Adleman, L.** *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*. Commun. ACM, 1978. — RSA，把分解困难性变成密码学安全性假设。
2. **Lenstra, H. W.** *Factoring Integers with Elliptic Curves*. Annals of Mathematics, 1987. — ECM，适合寻找小因子。
3. **Lenstra, A. K., Lenstra, H. W., Manasse, M., Pollard, J.** *The Number Field Sieve*. STOC 1990. — 经典通用算法的最优代表。
4. **Shor, P.** *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*. SIAM J. Comput., 1997（FOCS 1994）. — 多项式时间量子上界。
5. **Rabin, M.** *Digitalized Signatures and Public-Key Functions as Intractable as Factorization*. MIT/LCS/TR-212, 1979. — 提供了"破译 ⟺ 分解"的严格等价。
6. **Agrawal, M., Kayal, N., Saxena, N.** *PRIMES is in P*. Annals of Mathematics, 2004（预印本 2002）. — 素性检测属于 P，与分解形成鲜明对比。
7. **Boneh, D., Venkatesan, R.** *Breaking RSA May Not Be Equivalent to Factoring*. EUROCRYPT 1998. — 在代数归约模型下的分离。
8. **Boneh, D.** *Twenty Years of Attacks on the RSA Cryptosystem*. Notices of the AMS, 1999. — 综述，讲清 RSA 假设与分解假设的关系。
9. **Goldreich, O.** *Foundations of Cryptography, Vol. 2*. Cambridge University Press, 2004. — 教材。

## 常见误区

- **误区：分解已被证明是 NP 难的。** —— 没有这样的结果。它甚至普遍**不**被认为 NP 难；它落在 $\mathrm{NP} \cap \mathrm{coNP}$ 里，直觉上比 NP 完全问题"更容易"。
- **误区：素性检测很难，所以分解很难。** —— $\mathrm{PRIMES} \in \mathrm{P}$（AKS 2002）。两者难度不等价。
- **误区：RSA 的安全性严格等价于分解。** —— 没有证明。已知的是反方向：存在代数模型下的分离（Boneh-Venkatesan 1998）。破译 RSA 未必需要分解。
- **误区：量子计算机已经（或即将）实际破解 RSA。** —— Shor 是理论多项式算法；实际所需规模本质上是量子纠错工程问题（见 #59），与"分解是否在 P 中"无关。
- **误区：某次大数分解跑得快，就说明分解不难。** —— 具体实例的表现与问题整体的复杂性是两回事。
- **混淆上界与下界。** Shor 给出的是**上界**（存在多项式量子算法），不是下界；它不说明经典计算机做不到。

## 可运行实验

**`experiments/factoring_scaling.py`** — 小整数分解的复杂度实测

脚本实现试除法与 Pollard rho 法，对随机的 $b$ 位整数测量分解时间随位数 $b$ 的增长。建议同时记录"最坏情形"（如两个大素数之积）与"平均情形"的数据。

**能观察到**：试除法所需步数随 $b$ 呈指数增长；Pollard rho 呈约 $N^{1/4}$ 量级的亚指数增长——与已知的算法分析一致。

**绝不能说明**：

- 有限位数的实测**无法**推出渐近结论；
- 它**无法**证明不存在多项式算法，也**无法**为任何体制给出可供参考的"安全参数"；
- 换一个数论结构相近的数，实测量级可能显著不同——"具体实例"不等于"问题本身"。

跑这个实验的意义，不是得到结论，而是亲手体感"经验性能"与"复杂性下界"之间的距离。

## 延伸阅读

- **了解实际关系**：Boneh 的综述（文献 [8]），讲清分解、RSA 与各种攻击的地图。
- **经典算法**：文献 [2][3] 是数域筛法与 ECM 的原始来源。
- **相关档案**：[#14 公钥密码学](../../01-complexity-theory/problems/14-public-key-crypto.md)、[#35 格问题的时空硬度](35-lattice-space-time.md)、[#37 非关联 Oracle 模型中的 Grover 下界](37-grover-exact-lower-bound.md)、[#59 量子纠错](../../05-quantum-computing/problems/59-quantum-error-correction.md)。
