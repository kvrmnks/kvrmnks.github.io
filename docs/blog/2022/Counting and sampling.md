---
title: Counting and sampling notes
date: 2022-9-15 20:31:00
tags: [tcs]
---

A notes for CSE 599: Counting and Sampling.

What is sampling: Assume there is a giant space $\Omega$(usually finite). There is a function $w: \Omega \rightarrow \mathbb{R}_{+}$. And the unknown partition function $Z = \sum_{x \in \Omega} w(x)$. We need to generate a sample $x$ with probability $\frac{w(s)}{Z}$. 

Definition of $\#P$: a function $f \in \#P$ if and only if it counts accept paths of a NTM of a problem in $NP$. Or equally count the evidences. So #Circuit-SAT is #P-complete. And if #R is #P-complete, them R is in NP-Complete.

Counting and sampling deals with some #P problems.

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

#### Cut counting

In this example we show that for cut counting problem FPRAS <=> FPAUS.

For FPAUS => FPRAS

Assume we have FPAUS of cut counting problem.

We mainly consider this decomposisiont

Denote the cut set of graph $G$ as $M(G)$

$$\frac{1}{|M(G)|} = \frac{|M(G_{1})|}{|M(G_{0})|} \frac{ |M(G_{2})| }{ |M(G_{1})| }  \cdots \frac{ |M(G_{m})| }{ |M(G_{m-1})| }    $$

Lemma 1

$$\frac{ |M(G_{i})| }{ |M(G_{i-1})| } \geq \frac{1}{2}$$

proof: consider an element of $G_{i}$, it does not contain $e_{i}$. We can generate a distinctive cut by make one node of $e_{i}$ in other cut set. So 

$$ |M(G_{i})| \leq  |M(G_{i-1})| - |M(G_{i})| $$

$\blacksquare$

Lemma 2

given a FPAUS of cut counting problem, that 

$$ ||\mu - \pi||_{TV} \leq K $$

then 

$$ |\mathbb{Pr}_{x \sim \mu}[x \in M(G_{i})]  - \mathbb{Pr}_{x \sim \pi}[x \in M(G_{i})] |\leq K$$

proof:

Let $A = \{x | x \in M(G_{i})\}$, A is a subset. From total variance's definition, it's trivial.

$\blacksquare$

We have to use lemma2 to calculate the real probability because FPAUS only generates a sample.

Theorem: Chernoff bound for $X_{1}, X_{2}, \cdots, X_{n}$ i.i.d. $0 \leq X_{i} leq 1$. Define $\bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_{i}$. Then for any $\alpha > 0$

$$\mathbb{Pr}[ |\bar{X} - \mathbb{E}[X]| \geq \alpha \mathbb{E}[X]] \leq 2e^{-n\alpha^2\mathbb{E}[X]/3}$$

Lemma 3 

If we approximate $p$  in $1 + \frac{\epsilon}{4m}$ with error probability $\delta$, then we can approximate $\frac{1}{p}$ in $1 + \frac{\epsilon}{2m}$

proof:

$$

\begin{aligned}

\mathbb{Pr}[ |\tilde{p_{i}} - p_{i} | > \frac{\epsilon}{4m}p_{i}] &= \mathbb{Pr}[  (1 - \frac{\epsilon}{4m})p_{i} < \tilde{p}_{i} < (1 + \frac{\epsilon}{4m}) p_{i} ]

\end{aligned}

$$

$$\tilde{p}_{i} < (1 + \frac{\epsilon}{4m})p_{i} \rightarrow (1 - \frac{\epsilon}{4m + \epsilon})\frac{1}{p_{i}} < \frac{1}{\tilde{p}_{i}}$$

$$(1 - \frac{\epsilon}{4m + \epsilon}) > (1 - \frac{\epsilon}{2m}) $$

similar for other side.

Lemma 4

If we approximate $p_{i}$ with additive error $\epsilon$, then we can approximate 

