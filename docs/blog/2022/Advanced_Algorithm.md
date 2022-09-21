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





