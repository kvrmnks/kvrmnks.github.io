---
title: Advanced Algorithm
date: 2022-9-3 10:14:00
tags: [TCS]
---

## Maximum Cut

greedy cut ->
$\frac{1}{2}$-approximation

maximization approximation ratio $\alpha$
$$\frac{SOL_{G}}{OPT_{G}} \geq \alpha$$

minimization ... $\leq$

best approximation now 0.878~ (SDP semi-definite programming)

unique games conjecture -> hard to do better.

如何设计的?

### Random Cut

Theorem for uniform random cut $E(S, T)$ in graph $G$.

$$E[|E(S, T)|] = \frac{|E|}{2}$$

Then 
#### De-randomization by conditional expectation.

Travel from root to leaf while mark the vertex on decision tree.

#### De-randomization by pairwise independence

pairwise independent $X_{v}$

mutual independent ($\log n$) -> pairwise independent ($n$)

use Parity construction 

enumerate all assignments of $\log n$ bit. 

Parity search.

## Fingerprinting

answer equality.

### AB=C ?

$O(n^{\omega})$

find a truth

Freivald's Algorithm 1979

pick a uniform random $r \in \{0, 1\}^{n}$

check $A(Br) = Cr$?

proof ???

each time $\frac{1}{2}$


### Polynomial Identity Testing (PIT)

$f, g \in F[x]$ of degree $d$

if $f = g$ ?

f and g are black-box.

You can do evaluation.

Deterministic algorithm (polynomial interpolation)

Fundamental theorem of algebra

Randomized algorithm 

pick a uniform random r

check if $f(r) = 0$

communication complexity

consider # of bits communicated

Yao 1979

Every deterministic communication protocol solving EQ communicates $n$ bits in the worst-case.

use a small field like [p] $Z_{p}$

pick a prime $p \in [n^2, 2n^2]$

probability $O(\frac{1}{n})$

what about $f \in F[x_{1}, \cdots, x_{n}]$ of degree d.

poly-time deterministic for PIT -> either NEXP != P/poly or #P != FP

means that w.h.p. there is a poly-time deterministic for PIT.

There are some unknown powerful weapons.

Vandermonde determinant (like a black block)


#### Schwartz-Zippel Theorem

$f \neq 0 \rightarrow \mathrm{Pr}[f(x_{1}, \cdots, x_{n})=0] \leq \frac{d}{|S|}$

\# of any $f \neq 0$ in any cube $S^{n}$ $\leq d |S|^{n-1}$

application of Schwartz-Zippel

graph perfect matching

isomorphism of rooted tree

Reed-Muller codes

hardness vs randomness tradeoff

PCP



### binary graph perfect matching

Hall's theorem (matching theorem!)

Hungarian method O(n^3)

Hopcroft-Karp algorithm $O(m\sqrt{n})$

Edmonds matrix 

entries are variables (n*n not same as adjacent matrix) 

perfect matching -> permutation

det(A) != 0 <=> exists a perfect matching

$$det(A):=\sum_{\pi \in S_{n}} (-1)^{sgn(\pi)} \prod_{i=1}^{n}A_{i,\pi(i)}$$

use Schwartz-Zippel to check $det(A) = 0 ?$

(Chistov's algorithm) to solve det(A) parallel!

Fingerprinting: hidden requisite: random function

another fingerprint （通信协议那里）

直接解读成为2进制表示，pick random prime $p \in [k]$

Karp-Rabin algorthm (pattern-matching)


## Balls into Bins

birthday 单射

coupon collector 满射

occupancy 最大值

$$\frac{1}{|[m]\rightarrow[n]|}$$

1-1 birthday

on-to coupon collector

pre-image size  occupancy

### Birthday Paradox

$m > 57$ more than 99% two same birthday
 
$$\prod_{i=0}^{n-1} (1 - \frac{i}{m})$$

use chain rule

### Perfect Hashing

$m = n^2$ Pr[no collision]

Simple Uniform Hash Assumption

H(|[n] - > [m]|) = nlogm

Break the assumption !

Universal Hashing (Universal hash family)

k-universal 

Linear congruential model

Proposal Algorithm (Gale-Shapley algorithm)

Conwey Lattice theorem

Principle of Deferred Decisions

### Poisson approximation

m balls into n bins $\sim Bin(m, \frac{1}{n})$

i.i.d. Poisson random variables $Y_{1}, \cdots, Y_{n} \sim Pois(\frac{m}{n})$

$$\mathbb{Pr}[Y=k] = \frac{e^{-\lambda}\lambda^{k}}{k!}$$ 

for $k \in \mathbb{Z}^{+}$

$$\mathbb{E}[Y] = \mathbb{Var}[Y] = \lambda$$

Coupon collector:

$$\mathbb{Pr}[\land_{i=1}^{n}Y_{i}>0] = (1 - e^{-\frac{m}{n}})^{n}$$

(Poisson approximation brings independence here)

So

$$\lim_{n \rightarrow \infty} \mathbb{Pr}[X \geq n\ln n + cn] = 1 - e^{-e^{-c}}$$

(sharp threshold like monotonous properties in random graph)

像是水龙头调参！

Occupancy problems:

$$\mathbb{Pr}[\max_{1 \leq i \leq n} Y_{i} < L] = (\mathbb{Pr}[Y_{i} < L])^{n} \leq (1 - \mathbb{Pr}[Y_{i} = L])^{n}$$

wtf...

Theorem: $\forall m_{1}, \cdots, m_{n} \in \mathbb{N}$ s.t. $\sum_{i=1}^{n}m_{i} = m$

$$\mathbb{Pr}[\land_{i=1}^{n} X_{i} = m_{i}] = \mathbb{Pr}[\land_{i=1}^{n}Y_{i}=m_{i} | \sum_{i=1}^{n}m_{i} = m]$$

When $m = n \ln n + cn$

i.i.d. $Y_{1}, \cdots, Y_{n} \sim Pois(\frac{m}{n})$ and $Y = \sum_{i=1}^{n} Y_{i}$


$$\mathbb{Pr}[\land_{i=1}^{n}Y_{i} > 0] = \mathbb{Pr}[\land_{i=1}^{n} Y_{i} > 0 | Y = m] \pm o(1)$$

Theorem: $Y_{1}, \cdots, Y_{n} \sim Pois(\frac{m}{n})$, $\forall$ nonnegative function $f$

$$\mathbb{E}[f(X_{1}, \cdots, X_{n})] \leq e \sqrt{m} \mathbb{E}[f(Y_{1}, \cdots, Y_{n})]$$

Occupancy problem:

$$\mathbb{Pr}[\max_{i=1}^{n}X_{i} < L] \leq e\sqrt{m} \mathbb{Pr}[\max_{i=1}^{n} Y_{i} < L]$$

$\mathbb{E}$ becomes $\mathbb{Pr}$ when $f$ is an indicator.

### Load Balancing

application:

HashTable's query time complexity

Distributed computation (namely load balancing )

$Y_{i,j}$ iff ball $j$ lands in bin $i$.

$$\mathbb{E}[\max] \neq \max \mathbb{E}[]$$

Conclusion

$m = \Theta(n)$, $O(\frac{\log n}{\log \log n})$ whp

$m = \Omega(n\log n)$, $O(\frac{m}{n})$ whp

whp $1 - \frac{1}{n}$ or $1 - \frac{1}{n^{c}}$ usually c does not have influence on time complexity.

$$\frac{1}{nn^{c-1}} \leq \frac{1}{100n^{c-1}} \leq \frac{1}{100}$$

why such definition? usually polynomial false examples

wlp

wvlp(exp) whlp

$$\mathbb{P^{i}}(\exists i:X_{i}>t) \leq \sum_{i=1}^{n}\mathbb{P}(X_{i}\geq t) \leq \frac{1}{n}$$

$C_{m}^{t} \leq \frac{em}{t}^{t}$

### Concentration

Chernoff Bounds (Herman Chernoff) much stronger thant Markov's inequality (linear descent)

convenient chernoff bounds (when $\mathbb{E} \in \Omega(\log n)$, somehow linear)

Moment generating function + extended Markov's inequality

1.Use Markov's inequality on moment generating function

2.use independence of $X_{i}$, (NOT linearity of expectation)

3.$1+y \leq e^{y}$

4.optimize $\lambda$

(More) Chernoff Bounds

negatively associated r.v.

Hoeffding's inequality

Hoeffding's lemma

$X \in [a, b]$, $\mathbb{E}[X]=0$

$$\mathbb{E}[e^{\lambda X}] \leq exp(\frac{\lambda^{2}(b-a)^{2}}{8})$$

Hoeffding's inequality in Action:

Randomized Quicksort

$\Theta (n\log n)$ whp

proof: consider every path then union bound

Power of two choices

place the ball in the less loaded bin.

Power of d choices $O(\log^{d}(n))$?    X!

## Hashing and Sketching

based on random mapping 

### Count distinct elements
input: $x_{1}, \cdots, x_{n} \in U = [n]$

output: $Z = |\{x_{1}, \cdots, x_{n}\}|$

Data stream model: input date item comes one at a time.

Naive alg: $\Omega(z\log N)$

Sketch: (lossy) representation of data using space << Z

Is it possible? No

Lower bound: (Alon-Matias-Szegedy Godel prize): any deterministic(exact or approx) alg must use $\Omega(N)$ bits of space in the worst case. (Intuition: communication complexity set disjoin)

must use both random and approx

Sketcher!:
fu jian yi bo, yi quan chao ren 

$(\epsilon, \delta)$-estimator: $\hat{Z}$

$$\mathbb{Pr}[(1 - \epsilon)z \leq \hat{Z} \leq (1 + \epsilon)z] > 1 - \delta$$

PAC learning 

insight: need both random and approx

Shakespeare: 30k words

(idealized)uniform hash function h: $U \rightarrow [0,1]$

$\{h(x_{1}), \cdots, h(x_{n})\}$ 

estimator:

$$\mathbb{E}[\min h(x_{i})] = \mathbb{Pr}[] = \frac{1}{z+1}$$

First order approximation

$\hat{Z} = \frac{1}{\min_{i} h(x_{i})} - 1$ 

estimator variance is too large!

Markov's inequality

$$\mathbb{Pr}[X > t] \leq \frac{\mathbb{E}[X]}{t}$$

Corollary

$f(x) \geq 0$

$$\mathbb{Pr}[f(X) > t] \leq \frac{\mathbb{E}[f(X)]}{t}$$

Chebyshev's inequality

$$\mathbb{Pr}[|X-\mathbb{E}[X]| \geq t] \leq \frac{\mathrm{Var}[X]}{t^{t}}$$

<!-- $$\mathrm{Var}[Y]$$/ -->

variance cannot be bounded.

找找是哪里贡献过去的

exchange of sum and variance needs only pair-wise independent.



### 超纲内容 Universal Hash family (Carter and Wegman 1979) Flajolet-Martin algorithm

k-universal

strong k-universal

Linear congruential hashing:

Degree-k polynomial in finite field with random coefficients

zeros(y) = max(i: 2^{i}|y) denote # of trailing 0's

$$\mathbb{Pr}[\hat{Z} < \frac{z}{C} \lor \hat{Z} > C z] \leq \frac{3}{C}$$

一个函数能做到的最好的了

### BJKST Algorithm

2-wise independent hash function $h: [N] \rightarrow [M]$

$$\hat{Z} = \frac{kM}{Y_{k}}$$

对理想化的 min sketch 的离散化.

定义一个随机变量, 写成 pair-wise 事件的和. (方便求期望和方差)

### Frequency Moments

Data stream: $x_{1}, x_{2}, \cdots, x_{n} \in U$

for each $x \in U$, define frequency of $x$ as $f_{x} = |\{i: x_{i} = x\}|$

k-th frequency moments: $F_{k} = \sum_{x \in U} f^{k}_{x}$

Space complexity for $(\epsilon, \delta)$-estimation: constant $\epsilon, \delta$

for $k \leq 2$: polylog(N) AMS'96

for $k > 2$: $\theta(N^{1 - \frac{2}{k}})$ Indyk-Woodruff'05

Count distinct elements: $F_{0}$

optimal algorithm \[Kane-Nelson-Woodruff'10\] $O(\epsilon^{-2}+\log N)$

### Frequency estimation

output estimator of $f_{x}$ within **additive error**

multiplicative error 太难了

Heavy hitters: items that appears $> \epsilon n$ times.

防止ddos

### Data Structure for set

look CS168 Tool box!

bloom filter

数据库

bloom counter 

count min sketch (CMS) 为什么这里只需要 2-universal 呢??? 感觉是因为扩大了内存




## Concentration of Measure
概率论沉思录

Chernoff Bound

Bernstein Inequality

sum of independent trials

### Sub-Gaussian Random variables

A centered($\mathbb{E}[Y] = 0$) random variable Y is said to be sub-Gaussian with variance factor $\nu$ if 

$$\mathbb{E}[e^{\lambda Y}] \leq \exp\frac{\lambda^{2} \nu}{2}$$

Another interpretation of Chernoff-Hoeffding


### The method of bounded differences

(McDiarmid's Inequality)

任何 lipschitz function 在 prod measure 都接近一个常函数

即使 alg 不随机, data 也可能随机.


Chernoff -> 1-Lipschitz

Hoeffding -> $(b_{i} - a_{i})$-Lipschitz


心理史学(?)

consider \# empty bins in Balls into Bins

$$Y = f(X_{1}, \cdots, X_{m}) = n - |\{X_{1}, \cdots, X_{m}\}|$$

is 1-Lipschitz.

Pattern Matching

k-Lipschitz

Sprinkling Points on Hypercube

iso pari metric

Harper's inequality (iso pari metric in Hamming Space)

telagrand inequality

### McDiarmid's Inequality (worst-case)
For independent random variable $X_{1}, X_{2}, \cdots, X_{n}$, if n-variate function $f$ satisfies the Lipschitz condition: for every $1 \leq i \leq n$,

$$|f(x_{1}, \cdots, x_{n}) - f(x_{1}, \cdots, x_{i-1}, y_{i}, x_{i+1}, \cdots, x_{n})| \leq c_{i}$$

for any possible $i$ and $y_{i}$.

Then for any $t > 0$,
$$\mathbb{Pr}[|f(x_{1}, \cdots, x_{n}) - \mathbb{E}f(x_{1}, \cdots, x_{n})| \geq t ] \leq 2e^{-\frac{t^{2}}{2\sum_{i=1}^{n}c_{i}^{2}}}$$

This is a very powerful tool which can directly lead to Chernoff bound and Hoeffding bound.

### Martingale

A sequence of random variables $X_{0}, X_{1}, \cdots$ is a martingale if for all $t>0$,

$$\mathbb{E}[X_{t}|X_{0}, X_{1}, \cdots, X_{t-1}] = X_{t-1}$$

This expectancy is actually a function.

$f(X_{0}, X_{1}, \cdots, X_{t-1})$

$$\mathbb{E}[\mathbb{E}[X|Y]] = \mathbb{E}[X]$$

$$\mathbb{E}[\mathbb{E}[X|Y, Z]|Z] = \mathbb{E}[X|Z]$$

e.g. Fair gambling game 

Super-Martingale

$$\mathbb{E}[X_{t}|X_{0}, X_{1}, \cdots, X_{t-1}] \geq X_{t-1}$$

Sub-Martingale 

$$\mathbb{E}[X_{t}|X_{0}, X_{1}, \cdots, X_{t-1}] \leq X_{t-1}$$

Martingale (Generalized Version) (filtration of a sequence of $\sigma$-algebra):

A sequence of random variables $Y_{0}, Y_{1}, \cdots$ is a martingale

w.r.t. to $X_{0}, X_{1}, \cdots$ if for all $t \geq 0$,

$Y_{t}$ is a function of $X_{0}, \cdots, X_{t}$

$$\mathbb{E}[Y_{t+1}|X_{0}, \cdots, X_{t}] = Y_{t}$$

A fair gambling game:

$X_{i}$: outcome (win/loss) of the $i$-th betting

$Y_{i}$: capital after the $i$-th betting

#### Azuma's Inequality

For martingale $Y_{0}, Y_{1}, \cdots$ (w.r.t. $X_{0}, X_{1}, ...$) satisfying:

$$\forall i \geq 0, |Y_{i} - Y_{i-1}| \leq c_{i}$$

for any $n\geq 1$ and $t > 0$:

$$\mathbb{Pr}[|Y_{n} - Y_{0}| \geq t] \leq \exp (-\frac{t^{2}}{2\sum_{i=1}^{n}c_{i}^{2}})$$

Martingale rules: 如何必胜!

赌输了就加倍, 赢了立马跑路! 

所以下注是有上限的...

(别想了别想了)

#### Doob Martingale

A Doob sequence $Y_{0}, Y_{1}, \cdots, Y_{n}$ of an $n$-variate function $f$ w.r.t. a random vector $(X_{1}, ..., X_{n})$ is:

$$\forall 0 \leq i \leq n, Y_{i} = \mathbb{E}[f(X_{1}, \cdots, X_{n})|X_{1}, \cdots, X_{i}]$$
<!-- 
$Y_{0} = \mathbb{E}[]$ -->

Theorem:

The Doob sequence $Y_{0}, Y_{1}, \cdots, Y_{n}$ is a martingale w.r.t. $X_{1}, X_{2}, \cdots, X_{n}$. 

### Dimension reduction

#### Metric embedding

$d(x, x) = 0$

$d(x, y) = d(y, x)$

$d(x, y) + d(y, z) >= d(x, y)$

low-distortion: for small $\alpha \geq 1$

$\forall x_{1}, x_{2} \in X$, $\frac{1}{\alpha}d_{X}(x_{1}, x_{2}) \leq d_{Y}(\phi(x_{1}), \phi(x_{2})) \leq \alpha d_{X}(x_{1}, x_{2})$

somehow approximation

spherical -> planar ? exists such $\alpha$?: **NO**

convert the problem from a hard metric space into a easy metric space. (find a low distortion mapping)

#### Euclidean embedding

Input: n points $x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}^{d}$

Output: $y_{1}, \cdots, y_{n} \in \mathbb{R}^{k}$

$$(1 - \epsilon)||x_{i} - x_{j}|| \leq ||y_{i} - y_{j}|| \leq (1 + \epsilon)||x_{i} - x_{j}||$$

usually k << d (the curse of dimensionality)

consider how small can k be

For what distance || . ||

The embedding should be efficiently constructible.

#### Johnson-Lindenstrauss Theorem 1984 (also check CS168Toolbox)

$$(1 - \epsilon)||x_{i} - x_{j}||^{2}_{2} \leq ||y_{i} - y_{j}||^{2}_{2} \leq (1 + \epsilon)||x_{i} - x_{j}||^{2}_{2}$$

k = $O(\frac{\log n}{\epsilon^{2}})$ optimal! (k is irrelevant to $d$!)

A linear transformation!

The probabilistic method: for random $A \in \mathbb{R}^{k \times d}$

$$\mathbb{P}[\forall x, y \in S: (1 - \epsilon)||x - y||^{2}_{2} \leq ||Ax - Ay||^{2}_{2} \leq (1 + \epsilon)||x - y||^{2}_{2}] = 1 - O(\frac{1}{n})$$

We just need to prove this probability is greater than 0 in order to prove this theorem.

What kind of "random"?

Efficient construction of random $A \in \mathbb{R}^{k \times d}$

1. projection onto uniform random k-dimensional subspace; (Johnson-Lindenstrauss, Dasgupta-Gupta)
1. independent Gaussian entries; (Indyk-Motwani)
1. i.i.d. -1/+1 entries (Achlioptas)


independent Gaussian entries

For some suitable k = $O(\frac{\log n}{\epsilon^2})$

Entries of $A \in \mathbb{R}^{k \times d}$ are choosen i.i.d. from $\mathcal{N}(0, \frac{1}{k})$

$$1 - \epsilon \leq \frac{||Ax - Ay||^{2}_{2}}{||x - y||^{2}_{2}} \leq 1 + \epsilon$$

$$\frac{||Ax - Ay||^{2}_{2}}{||x - y||^{2}_{2}} = ||A \frac{x - y}{||x - y||_2}||_2^2$$

$$\mathbb{P}[| ||Au||_2^2 - 1| > \epsilon] \leq \frac{1}{n^3}$$

Here we use concentration of measurement

Chernoff bound for $\chi^2$ distributions

