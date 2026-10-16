# Vol.03 密码学与信息安全 · 领域综述

> 本册收录 8 个开放问题（#31 密钥交换 – #38 ZPR 分类），档案位于 [`problems/`](problems/)。状态分级见 [METHODOLOGY.md](../../METHODOLOGY.md)。

---

## 一、本册的中心张力

密码学是全部分册中最特殊的一册。它有一个几乎所有工程领域都不具备的特点：

> **它的绝大部分实际安全性，建立在"未经证明的假设"之上。**

我们用 RSA 加密、用 Diffie-Hellman 协商密钥、用椭圆曲线签名、用格密码抵御量子计算机——而支撑这一切的，是若干**没有人在数学上证明过**的困难性假设：

- "整数分解没有多项式时间经典算法"（见 [#32](problems/32-integer-factoring.md)）；
- "离散对数在相应群上困难"（[#31](problems/31-key-exchange-from-owf.md)）；
- "格上的最短向量问题难以近似"（[#35](problems/35-lattice-space-time.md)）；
- "虽然存在单向函数，但它不足以黑盒地构造出密钥交换"（[#31](problems/31-key-exchange-from-owf.md)）。

这些假设有两个共同特征：**第一，它们从未被证明；第二，它们很可能在很长时间内都不会被证明。** 这不是悲观，而是由复杂性理论自身的现状决定的——证明"某个问题不存在快速算法"，恰恰是计算复杂性理论大半世纪以来最不擅长的事情。

于是产生了本册的核心张力：

$$\underbrace{\text{密码学需要"困难"，且必须相信困难}}_{\text{工程上必须落注}} \quad \text{vs.} \quad \underbrace{\text{复杂性理论无法证明"困难"}}_{\text{理论上无法保证}}$$

工程上必须落注：你不能等到假设被证明才去部署加密系统。理论上无法保证：至今没有任何一个实际使用的密码学困难性假设，被**无条件地**证明。这是一个结构性的、而非暂时的缺口。

---

## 二、这与复杂性理论的开放问题是什么关系

本册与 Vol.01 的问题几乎一一对应，只是站在了**建设者**而非**证明者**的角度。

| 复杂性理论的开放问题 | 密码学中的对应 | 关系 |
|---|---|---|
| [#13 单向函数是否存在](../../01-complexity-theory/problems/13-one-way-functions.md) | 一切计算性密码学的地基 | 若不存在单向函数，则几乎所有实用密码学**在原理上**就不安全 |
| [#14 公钥密码学是否可能](../../01-complexity-theory/problems/14-public-key-crypto.md) | RSA、DH、格密码的存在性 | 公钥密码学是"存在单向函数"之外的更强要求 |
| [#1 P vs NP](../../01-complexity-theory/problems/01-p-vs-np.md) | 困难性假设的强度 | 若 P = NP，则一切计算性密码学**在原理上**不可能 |

这里的因果关系必须说清楚，否则极易误读：

- **若 $\mathrm{P} = \mathrm{NP}$**，则不存在单向函数，因而**不存在**任何计算性密码学。这是一条**条件性**结论——它的前提至今未被证明，也**普遍不被相信**（见 [#1](../../01-complexity-theory/problems/01-p-vs-np.md)）。
- **若单向函数存在**，则至少可以做对称密码学（伪随机生成器、签名、承诺）。这一点已有构造（见 [#31](problems/31-key-exchange-from-owf.md)）。
- 但"**单向函数存在**"**不**能黑盒地推出密钥交换与公钥加密——这是 Impagliazzo 与 Rudich 1989 年的分离结果（见 [#31](problems/31-key-exchange-from-owf.md)）。

最后一条是理解本册的钥匙：**密码学并非一个由单一假设支撑的整体，而是一座分层的建筑。** 每一层原语所需的假设强度不同，而许多层级之间的连接**已被证明无法用最自然的方法打通**。Impagliazzo 用"五个世界"（Algorithmica / Heuristica / Pessiland / Minicrypt / Cryptomania）刻画了这种分层，是理解本题图景的最佳入口。

这也解释了一个常见的困惑：为什么"用格问题做密码学"和"用单向函数做密码学"看起来都在讲"困难问题"，地位却如此不同。答案是：它们处在假设阶梯的不同高度，而**阶梯上多数的台阶只能用假设而非证明来跨过**。

---

## 三、本册的问题地图

八个问题可按"攻击对象"分为三类。

**（一）直接支撑现有密码学的基础假设**

- [#32 整数分解的多项式时间经典算法](problems/32-integer-factoring.md)：RSA 的地基。它的状态是：**既不知道是否在 $\mathrm{P}$ 中，也不认为它 $\mathrm{NP}$ 难**，且与素性检测（已在 $\mathrm{P}$ 中）形成鲜明对比。
- [#31 从任意单向函数构造密钥交换](problems/31-key-exchange-from-owf.md)：把"最弱假设能走多远"这一纲领推到极致。

**（二）新兴或另类的困难性来源**

- [#35 格问题的时空硬度](problems/35-lattice-space-time.md)：后量子密码学的安全基础，问题问的是"时间与空间同时受限时是否仍难"。
- [#34 热带密码学中的离散对数问题](problems/34-tropical-cryptography.md)与 [#36 强正则图族的安全参数选择](problems/36-strongly-regular-graph-parameters.md)：两例以"新颖代数 / 组合结构"替代有限域的尝试。它们共同的问题是：**结构新颖不等于问题困难**，而困难性必须证明。
- [#33 细粒度密码学的基础](problems/33-fine-grained-crypto.md)：试图用"具体运行时间"这种更弱的假设支撑密码学。

**（三）量子与元层面的边界问题**

- [#37 非关联 Oracle 模型中的 Grover 下界](problems/37-grover-exact-lower-bound.md)：这里有一个关键定位——标准无序搜索的 $\Theta(\sqrt N)$ 紧界**已经解决**（Grover 给出上界、BBBV 给出下界），真正开放的只是非关联等更细粒度模型下的界。
- [#38 ZPR 决策的复杂性分类](problems/38-zpr-complexity.md)：关于零知识相关判定问题复杂度的分类，题名所指本身尚待核实。

---

## 四、后量子密码学带来的新问题图景

量子计算给本册带来了第二重张力。

**第一重冲击来自 Shor。** 1994 年的 Shor 算法在**多项式时间**内解决了整数分解与离散对数。这意味着：若大规模容错量子计算机可被建造，则**基于分解与离散对数的全部密码学（RSA、经典 DH、椭圆曲线）将被攻破**。这不是渐进的威胁，而是**多项式时间**的灭顶——见 [#32](problems/32-integer-factoring.md) 与 [#31](problems/31-key-exchange-from-owf.md)。

**第二重冲击来自 Grover。** Grover 算法对无序搜索给出平方根加速：对 $n$ 比特密钥的穷举搜索从 $2^{n}$ 降到约 $2^{n/2}$ 次查询。这是**平方根**级别的削弱，而非致命一击——但它迫使**对称**密码的安全参数加倍。值得注意的是，这一加速的紧性**已经确立**（Grover 上界 + BBBV 下界），是少数"完全清楚"的量子威胁；真正开放的是更精细的模型（见 [#37](problems/37-grover-exact-lower-bound.md)）。

**应对之道，以及随之而来的新问题。**

后量子密码学（post-quantum cryptography）选择把安全假设迁移到**相信量子计算机也难以攻破**的问题上，主流候选是基于格的问题（[#35](problems/35-lattice-space-time.md)）。

但这一迁移并没有消除根本张力，反而使它更复杂：

- 格密码的安全性依然建立在**未证明的**平均情况假设上（如 LWE），而这些假设背后是条件性的最坏—平均归约；
- 量子算法也可能对格问题带来加速，攻击复杂度分析因此更难；
- 时空硬度（[#35](problems/35-lattice-space-time.md)）成为新的关键问题：若只能证明"时间难"而无法证明"空间难"，则内存充足的攻击者可能占优；
- 一旦把安全性迁移到新假设，"这个假设究竟有多可信"就成为整个系统的单点故障。

**换句话说：量子计算并未让密码学更接近"可证明安全"，它只是把赌注换了一张桌子。**

---

## 五、如何阅读本册

- **想理解"为什么密码学不安全也可以很安全"**：先读 [#31](problems/31-key-exchange-from-owf.md)，再读 Impagliazzo 的"五世界"框架。
- **想了解自己每天在用的加密**：读 [#32](problems/32-integer-factoring.md)，重点看"常见误区"节中"分解与 RSA 不等价"。
- **想看清"新密码方案"的成色**：读 [#34](problems/34-tropical-cryptography.md) 与 [#36](problems/36-strongly-regular-graph-parameters.md)——它们示范了如何判别一个"新颖困难问题"是否真的困难。
- **想动手**：[#34](problems/34-tropical-cryptography.md) / [#36](problems/36-strongly-regular-graph-parameters.md)（`experiments/dlp_small_scale.py`）、[#32](problems/32-integer-factoring.md)（`experiments/factoring_scaling.py`）、[#37](problems/37-grover-exact-lower-bound.md)（`experiments/grover_amplitude_amplification.py`）都指向可运行的脚本。**但请务必读完每个实验的"绝不能说明"一节**——在密码学里，小规模实验几乎从不构成安全性证据。

---

## 六、一句话总结

本册八个问题的共同底色是：

> **几乎所有实用密码学的安全性，都建立在未经证明的假设之上；而"证明这些假设"的困难，正是计算复杂性理论中那些最深刻的开放问题（[#1](../../01-complexity-theory/problems/01-p-vs-np.md)、[#13](../../01-complexity-theory/problems/13-one-way-functions.md)、[#14](../../01-complexity-theory/problems/14-public-key-crypto.md)）本身。**

理解了这一点，就能同时理解两件事：为什么密码学在实践中可靠，以及为什么它在理论上始终悬着一把剑。
