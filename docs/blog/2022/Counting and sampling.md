---
title: Counting and sampling notes
date: 2022-9-15 20:31:00
tags: [tcs]
---

A notes for CSE 599: Counting and Sampling.

What is sampling: Assume there is a giant space $\Omega$(usually finite). There is a function $w: \Omega \rightarrow \mathbb{R}_{+}$. And the unknown partition function $Z = \sum_{x \in \Omega} w(x)$. We need to generate a sample $x$ with probability $\frac{w(s)}{Z}$. 

Definition of $\#P$: a function $f \in \#P$ if and only if it counts accept paths of a NTM of a problem in $NP$. Or equally count the evidences. So #Circuit-SAT is #P-complete. And if #R is #P-complete, them R is in NP-Complete.

Counting and sampling deals with some #P problems.

Definition of multiplicative error: 

real value $p$ and estimation $\tilde{p}$ with multiplicative error $1 + \epsilon$ means that 

$$(1 - \epsilon)p \leq \tilde{p} \leq (1 + \epsilon) p$$

or equally

$$ |\tilde{p} - p| \leq \epsilon p$$

$p$ with additive error $\epsilon$ means that 

$$ |\tilde{p} - p| \leq p$$


## Equivalence of Counting and Sampling

The two basic problem is FPRAS and FPAUS.

### FPRAS
Fully polynomial randomized approximation scheme.

Definition: Given a set $\Omega$ and a weight function $w: \Omega \rightarrow \mathbb{R}_{+}$ and a partition function $Z = \sum_{x \in \Omega'} w(x)$, the FPRAS is an algorithm with given error rate $\epsilon$ and confidence interval $\delta$ that return $\tilde{Z}$ , s.t.

$$\mathrm{Pr}[(1 - \epsilon)Z < \tilde{Z} < (1 + \epsilon)Z] > 1 - \delta$$

The algorithm must run in $Poly(n, \frac{1}{\epsilon}, \log \frac{1}{\delta})$

### FPAUS
Fully polynomial almost uniform sampler

Before giving the formal definition, we have to define total variance.

#### Total variance

Supppose $\mu, \nu: \Omega \rightarrow \mathbb{R}_{+}$ are two probability distribution. 

The total variance is defined as 

$$ ||\mu - \nu||_{TV} = \frac{1}{2} \sum_{x \in \Omega} |\mu(x) - \nu(x)|$$

Or equally 

$$||\mu - \nu||_{TV} = \max_{X \subset \Omega}|\mu(X) - \nu(X)|$$

Proof:

For the second formula, we can see that if we pick $X = \{x| \mu(x) > \nu(x) \}$, RHS is maximized.

$$
\begin{align}
|\mu(\Omega - X) - \nu(\Omega - X)| 
&= |\nu(\Omega - X) - \mu(\Omega - X)| \\
&= | (1 - \mu(X)) - (1 - \nu(X)) | \\
&= |\nu(X) - \mu(X)| \\
&= |\mu(X) - \nu(X)|  \\
\end{align}
$$
So 

$$\max_{X \subset \Omega}|\mu(X) - \nu(X)| = \frac{1}{2} \sum_{x \in \Omega}|\mu(x) - \nu(x)| $$


Definition of FPAUS: 

fully polynomial almost uniform sampler

There is a finite space $\Omega$ and a weight functiton $w: \Omega \rightarrow \mathbb{R}_{+}$, and a partition function $Z = \sum_{x \in \Omega}w(x)$, $\pi(x) = \frac{w(x)}{Z}$, fully polynomial almost uniform sampler is an algorithm with given error rate $\delta$ generate a sample from distribution $\nu$ s.t.

$$||\mu - \nu||_{TV} < \delta$$

running in $Poly(n, \log \frac{1}{\delta})$

For self-reducible problems, it can be proved that FPRAS means FPAUS.

#### Matching counting

In this example we show that for matching counting problem FPRAS <=> FPAUS.

For FPAUS => FPRAS

Assume we have FPAUS of matching counting problem.

We mainly consider this decomposisiont

Denote the matching set of graph $G$ as $M(G)$

$$\frac{1}{|M(G)|} = \frac{|M(G_{1})|}{|M(G_{0})|} \frac{ |M(G_{2})| }{ |M(G_{1})| }  \cdots \frac{ |M(G_{m})| }{ |M(G_{m-1})| }    $$

Lemma 1

$$\frac{ |M(G_{i})| }{ |M(G_{i-1})| } \geq \frac{1}{2}$$

proof: consider an element of $G_{i}$, it does not contain $e_{i}$. We can generate a distinctive matching by make one node of $e_{i}$ in other matching set. So 

$$ |M(G_{i})| \leq  |M(G_{i-1})| - |M(G_{i})| $$

$\blacksquare$

Lemma 2

given a FPAUS of matching counting problem, that 

$$ ||\mu - \pi||_{TV} \leq K $$

then 

$$ |\mathbb{Pr}_{x \sim \mu}[x \in M(G_{i})]  - \mathbb{Pr}_{x \sim \pi}[x \in M(G_{i})] |\leq K$$

proof:

Let $A = \{x | x \in M(G_{i})\}$, A is a subset. From total variance's definition, it's trivial.

$\blacksquare$

We have to use lemma2 to calculate the real probability because FPAUS only generates a sample.

Theorem: Chernoff bound for $X_{1}, X_{2}, \cdots, X_{n}$ i.i.d. $0 \leq X_{i} \leq 1$. Define $\bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_{i}$. Then for any $\alpha > 0$

$$\mathbb{Pr}[ |\bar{X} - \mathbb{E}[X]| \geq \alpha \mathbb{E}[X]] \leq 2e^{-n\alpha^2\mathbb{E}[X]/3}$$

Lemma 2.5

With $O(\frac{m^{2}}{\epsilon^{2}}\log \frac{m}{\delta})$ sample, we can approximate $\bar{X}$ with additive error $\frac{\epsilon}{20m}$ and confidence interval $\frac{\delta}{m}$.

Use Lemma 2 and Lemma 2.5 we can approximate $p_{i}$ with additive error $\frac{\epsilon}{10m}$ and confidence interval $\frac{\delta}{m}$



Lemma 3 

If we approximate $p$  in $1 + \frac{\epsilon}{4m}$ with error probability $\delta$, then we can approximate $\frac{1}{p}$ in $1 + \frac{\epsilon}{2m}$

proof:

$$

\mathbb{Pr}[ |\tilde{p_{i}} - p_{i} | > \frac{\epsilon}{4m}p_{i}] = \mathbb{Pr}[  (1 - \frac{\epsilon}{4m})p_{i} < \tilde{p}_{i} < (1 + \frac{\epsilon}{4m}) p_{i} ]

$$

$$\tilde{p}_{i} < (1 + \frac{\epsilon}{4m})p_{i} \rightarrow (1 - \frac{\epsilon}{4m + \epsilon})\frac{1}{p_{i}} < \frac{1}{\tilde{p}_{i}}$$

$$(1 - \frac{\epsilon}{4m + \epsilon}) > (1 - \frac{\epsilon}{2m}) $$

similar for the other side.

Lemma 4

If we approximate $p_{i}$ with additive error $\epsilon$, then we can approximate it with multiplicative error $1 + 2 \epsilon$

proof:

$$ |\tilde{p}_{i} - p_{i}| < \epsilon = \epsilon 2 \frac{1}{2}  < 2\epsilon p_{i} $$

$\blacksquare$

With lemma 2, lemma 2.5 and lemma 4, we can approximate $\frac{1}{p_{i}}$ with multiplicative error $1 + \frac{\epsilon}{5m}$ and confidence interval $\frac{\delta}{m}$

Use union bound, we can prove there is an FPRAS. 


FPRAS => FPAUS

Suppose we have a exact counter, we can derive a exact sampler by conditional probability method.

Now try to extend to approximate area.

Denote the $i$ th graph as $G^{i}$, we can formulate the probability of a sample $x$, $e_{i} = (u_{i}, v_{i})$.

$$\mathbb{Pr}[x] = \prod_{i}^{|E|}\max(\mathbb{I}[e_{i} \notin V(G_{i-1})], \frac{\mathbb{I}[e_{i} \notin x] |M(G^{i-1} / \{e^{i}\})| + \mathbb{I}[e_{i} \in x] |M(G^{i-1}/ \{u_{i}, v_{i}\})|}{|M(G^{i-1})|})$$


Using FPRAS, we can approximate $|M(.)|$ with multiplicative error $1 + \epsilon$, and confidence interval $\delta$. 

So, we can approximate $\frac{1}{\mathbb{Pr}[x]}$ with multiplicative error $(1 + \epsilon)^{n^{2}}$ and confidence interval $n^{2}\delta$(union bound).

**I think process can end at here, but the lecture brings out rejection sampling that I do not understand.**

$$ \tilde{\pi}(M) \geq \frac{(1 - \epsilon)^{n^2}}{|M(G)|} \geq \frac{(1 - \epsilon)^{n^2 + 1}}{|\tilde{M}(G)|} := \alpha$$

Once construct $M$, we construct 

$p_{accept}(M) = \frac{\alpha}{\tilde{\pi}(M)}$

So every samples has the same probability. 

## FPRAS for DNF counting

Assume there are $n$ variables and $m$ clauses.

Consider the most straight way, sample $N$ samples $X_{1}, X_{2}, \cdots, X_{n}$. $X_{i}$ contains an assignment for each variable. If DNF satisfies, then $X_{i} = 1$

So
$$\frac{1}{N}\sum_{i=1}^{N}X_{i} = \frac{ANS}{2^{n}}$$ 

According to Chernoff Bound, if we want to sample $ANS$ with multiplicative error $1 + \epsilon$ and confidence interval $\delta$. 

We need to hold

$$e^{-N\epsilon^{2}\frac{ANS}{3\times 2^{n}}} \leq \delta$$

So $N > \frac{2^{n}}{\epsilon^{2} ANS}$, but $N$ may be exp about $n$.

### Karp, Luby and Madras algorithm \[KLM\]

This is a simple way to decrease the size of universe. 

We sample from the union of ground set instead of all the assignments.

Let the ground set(feasible solutions) of $i$ th clause be $S_{i}$.

We sample from $\sum_{i=1}^{m} S_{i}$.

The estimator is $\frac{|\bigcup_{i=1}^{m}S_{i}|}{\sum_{i=1}^{m} |S_{i}|}$

In DNF counting problem, it is easy to sample $\sum_{i=1}^{m}|S_{i}|$, we can use brute hash to exclude those same elements.

## Network Unreliability

...

