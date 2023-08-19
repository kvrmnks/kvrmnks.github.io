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
\begin{aligned}
|\mu(\Omega - X) - \nu(\Omega - X)| 
&= |\nu(\Omega - X) - \mu(\Omega - X)| \\
&= | (1 - \mu(X)) - (1 - \nu(X)) | \\
&= |\nu(X) - \mu(X)| \\
&= |\mu(X) - \nu(X)|  \\
\end{aligned}
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

**The motivation is that choose a small and count-efficient universe, then a estimator with good(polynomial) lower bound in order to use Chernoff Bound.**

This is a simple way to decrease the size of universe. 

We sample from the union of ground set instead of all the assignments.

Let the ground set(feasible solutions) of $i$ th clause be $S_{i}$.

We sample from $\sum_{i=1}^{m} S_{i}$.

The estimator is $\frac{|\bigcup_{i=1}^{m}S_{i}|}{\sum_{i=1}^{m} |S_{i}|}$. 

Obviously,

$$\frac{1}{m} \leq \frac{|\bigcup_{i=1}^{m}S_{i}|}{\sum_{i=1}^{m}S_{i}}\leq 1$$

This 'large' lower bound means that we can use Chernoff bound more effectively.

recall that $\mathbb{Pr}[|X - \mathbb{E}[x]| > \alpha \mathbb{E}[x]] < e^{-\frac{N\alpha^{2}\mathbb{E}[x]}{3}}$. To get FPRAS, we only need

$$e^{-\frac{N\epsilon^2 \mathbb{E}[x]}{3}} \leq e^{-\frac{N\epsilon^{2}}{3m}}\leq \delta$$

$$N >  3m\frac{1}{\epsilon^{2}}\log\frac{1}{\delta}$$

which achieves FPRAS

In DNF counting problem, it is easy to sample $\sum_{i=1}^{m}|S_{i}|$, we can use brute hash to exclude those same elements.

## Network Unreliability

Definition: Given a graph $G$ with a probability function states that a link $e$ disappears independently with probability $p_{e}$.

Here we assume that $\forall e\in E$, $p_{e} = p$. Now consider the probability that the surviving network is disconnected. Let $Fail(p)$ be this problem.

Network unreliability problem can be trivially expressed as a DNF problem.

Let $C_{1}, C_{2}, \cdots, C_{k}$ be $k$ cuts of graph $G$.

$x_{e}$ is the indicator variable that $e$ is broken.

Then $G$ is disconnected iff

$$\lor _{i=1}^{k} \land_{e\in C_{i}}x_{e}$$

Is it solved by the KLM algorithm?

But it does not fit the standards of FPRAS because maybe $k = \Theta(e^{n})$

### Karger's algorithm

**Motivation: divide the problem into two parts, one is small, the other is large enough. Like the tricks in calculus.**

Let $C$ be the size of the minimum cut of $G$. 

$$Fail(p) \geq p^{C} = q$$

Case 1:  $q > \frac{1}{poly(n)}$. We can use the Chernoff Bound directly because **this property actually gives a lower bound**.

$$$$

Case 2: $q < \frac{1}{poly(n)}$.

Theorem Karger's theorem. For any graph $G$ with $n$ vertices and with minimum cut $C$, and for any $\alpha \geq 1$, the number of cuts of size at most $\alpha C$ in is at most $n^{2\alpha}$.

proof: Karger's contraction algorithm 

Lemma: Let $C_{1}, C_{2}, \cdots, C_{r}$ be all the cuts of $G$ and let us sort them in the order of their size

$$|C_{1}| \leq |C_{2}| \leq \cdots \leq |C_{r}|$$

For any $\alpha \geq 1$, and $q = n^{-\beta}$ we have

$$\mathbb{Pr}[\exists i \geq n^{2\alpha}: C_{i} fails] \leq \frac{n^{2\alpha(-\frac{\beta}{2}+1)}}{\frac{\beta}{2}-1}$$

proof:

recall that the theorem above actually gives the relation between the index and the cut size.

Let $i = n^{2\alpha}$, $\alpha = \frac{\log i}{2 \log n}$. So $|C_{i}| \geq \frac{\log i}{2 \log n}C$

By union bound 

$$
\begin{aligned}
\mathbb{Pr}[\exists i \geq n^{2\alpha}: C_{i} fails] &\leq \sum_{i\geq n^{2\alpha}} \mathbb{Pr}[C_{i} \quad fails] \\
&= \sum_{i\geq n^{2\alpha}} p^{|C_{i}|} \\
&\leq \sum_{i \geq n^{2\alpha}} p^{\frac{\log i}{2\log n}C} \\
&= \sum_{i \geq n^{2\alpha}}q^{\frac{\log i}{2\log n}} \\
&\leq \int_{n^{2\alpha}}^{\infty}q^{\frac{\log i}{2\log n}} \mathrm{d}i \\
&= \frac{n^{2\alpha(-\frac{\beta}{2} + 1)}}{\frac{\beta}{2} - 1}
\end{aligned}
$$

With this lemma, the "large cuts" has few probability to fail.

## Markov Chains

Markov chains is a stochastic process on the state $\Omega$. 

Markov property 

$$\mathbb{Pr}[X_{t+1} | X_{0}, \cdots, X_{t}]  = \mathbb{Pr}[X_{t+1} | X_{t}]$$


Markov kenel 

$$\mathbb{Pr}[X_{t+1}|X_{t}] = K(X_{t}, X_{t+1})$$


Also Markov chain can be represent as a weighted direct graph, if $K(x, y) = c > 0$ then there is a edge weighted $c$ from $x$ to $y$.

If we sample $X_{0} \sim p$. 

$$\mathbb{Pr}[X_{1}=x] = \sum_{y \in \Omega}p(y)K(y, x) = p^{T}K(x)$$

Corollery 

$$\mathbb{Pr}[X_{t} = y| X_{0} \sim p] = p^{T}K^{t}$$

### Stationary Distribution
Every Markov chain has a stationary distribution(may not unique).


First of all the Markov kernel must have eigenvalue $1$ and corresponding eigenvector $v$. 

It is easy to show that $\mathrm{det}(K - I) = 0$, as the sum of every column of $K$ is exactly $1$.

Now let $\pi = (|v_{1}|, |v_{2}|, \cdots, |v_{k}|)^{T}$.  We show that $\pi$ is a stationary distribution.

If $\pi^{T}\pi \neq 1$, then we can normalize it into normal vector.

$$\pi_{i} = |v_{i}| = |\sum_{j}v_{j}K(j,i)| \leq \sum_{j}|v_{j}|K(j,i) \leq \sum_{j}\pi_{j}K(j,i)$$

This is a trivial inequality. But the next one is somehow magic ...

$$
\begin{aligned}
\sum_{i}\pi_{i} &= \sum_{i}\pi_{i}(\sum_{j}K(i,j)) \\\
&= \sum_{j}\sum_{i}\pi_{i}K(i,j) \\
&\geq \sum_{j} \pi_{j}
\end{aligned}
$$

But actually the last inequality must be tight, so the it must holds that $\pi_{i} = \sum_{j}\pi_{j}K(j,i)$.

**NB: in lecture notes it chose relu(v), but here I modified a little bit.**

Definition (Reversible Markov Chains): A Markov chain is reversible iff **there exists a nonnegative weight function** $w: \Omega \rightarrow \mathbb{R}_{+}$. Such that for every $x, y$.

$$\pi(x)K(x, y) = \pi(y)K(y, x)$$

It follows that $\frac{\pi}{Z}$ is the stationary distribution. 

### Mixing of Markov Chain
Definition(Irreducible Markov Chain): A Markov chain is irreducible iff for any states $x$, $y$, it exits $t$ such that $K^{t}(x,y) > 0$.

Definition(aperiodic): A Markov Chain is aperiodic if for all $x, y$ we have $\gcd\{t|K^{t}(x,y)>0\} = 1$

Lemma: Let $K$ be an irreducible, aperiodic Markov Chain. Then there exists $t>0$ such that for all $x, y$

$$K^{t}(x,y) > 0$$

**Actually I do not know how to formally prove this...**

Theorem (Fundamental Theorem of Markov Chains): Any irreducible and aperiodic Markov chain has a **unique** stationary distribution. Futhermore, for all $x, y$,

$$K^{t}(x, y) \rightarrow \pi(y)$$

as t goes infinity. In particular, for any $\epsilon > 0$ there exits $t > 0$ such that $||K^{t}(x, .) - \pi||_{TV} < \epsilon$.

How to make an arbitrary Markov chain ergodic: 
All add a self-loop with $\frac{1}{2}$

### Metropolis Rule

Given a finite state set and a weight function $w: \Omega \rightarrow \mathbb{R}_{+}$. We would like to sample from the distribution $\pi(x) = \frac{w(x)}{Z}$. 

Metropolis rule is a general tool to construct such a ergodic Markov chain.

#### Neighborhood Structure

The first requirement is a undirected connected graph $G = (\Omega, E)$, two state are connected iff they different by some local changes. 

#### Proposal Distribution
At any vertex $x$ we require a proposal distribution, $p(x, .)$ satisfying the following properties:

1. $p(x,y) > 0$ only if $y$ is a neighbor of $x$.
2. $p(x,y) = p(y,x)$ for all $y$
3. $\sum_{y}p(x,y) = 1$


#### Metropolis chain

1. decide a propose move from $x$ to $y$ with probability $p(x, y)$.
2. accept the propose move with probability $\min\{1, \frac{\pi(y)}{\pi(x)}\}$. else reject and stay at $x$

**NB: this is like the simulated annealing ideas in optimization**

Lemma: Metropolis chain is reversible with stationary distribution $\pi$

(But how to prove that $\pi$ is the stationary distribution?)

### Coupling

Definition(Coupling): Let $\mu, \nu$ be probability distributions over $\Omega$, A coupling between $\mu, \nu$ is a probability distribution $\pi$ on $\Omega \times \Omega$ that preserves the marginals of $\mu, \nu$. 

$$\sum_{y} \pi(x, y) = \mu(x)$$

$$\sum_{x} \pi(x, y) = \nu(y)$$

Lemma(Coupling Lemma): Let $X \sim \mu$, $Y \sim \nu$

Then 

1. $\mathbb{Pr}[X \neq Y] \geq ||\mu - \nu||_{TV}$
2. There exists a coupling $\pi$ between $\mu$ and $\nu$ such that $\mathbb{Pr}[X \neq Y] = ||\mu - \nu||_{TV}$



proof:

A simple observation is that $\mathbb{Pr}[X=Y=a] \leq \min\{\mu(a), \nu(a)\}$

$$
\begin{aligned}
\mathbb{Pr}[X \neq Y] &= 1 - \sum_{a \in \Omega} \mathbb{Pr}[X = Y = a]\\
&\leq 1 - \sum_{a \in \Omega} \min\{\mu(a), \nu(a)\} \\
&= \sum_{a \in \Omega} (\mu(a) - \min\{\mu(a), \nu(a)\}) \\
&= ||\mu - \nu||_{TV}
\end{aligned}
$$

So we just need to "properly" set  remaining probability to let the inequality be tight.

$\blacksquare$

#### Mixing time
Terminology:

$$\Delta_{x}^{t} = ||K(x,.)^{t} - \pi||_{TV}$$

$$\tau_{x}(\epsilon) = \min\{t|\Delta_{x}^{t} < \epsilon\}$$

$$\tau (\epsilon) = \max \{\tau_{x}(\epsilon)| x\in \Omega \}$$

Definition (Mixing time): $\tau(\frac{1}{2e})$

Lemma: 

$$\Delta_{x}(t+1) \leq \Delta_{x}(t)$$

proof:

This proof shows the power of coupling.

Let $X_{0} = x$, $Y_{0} \sim \pi$.

Suppose now we get a coupling such that $\mathbb{Pr}[X_{t}\neq Y_{t}] = \Delta_{x}(t)$

Now define $X_{t+1}$, $Y_{t+1}$ as below

1. If $X_{t} = Y_{t}$, then set $X_{t+1} = Y_{t+1}$

2. else random walk independently

So 
$$\Delta_{x}(t+1) \leq \mathbb{Pr}[X_{t+1} \neq Y_{t+1}] \leq \mathbb{Pr}[X_{t}\neq Y_{t}] = \Delta_{x}(t)$$

$\blacksquare$

General bound for mixing time

Lemma:

$$\tau_{mix} \leq \frac{1}{|\Omega|\min_{x,y} K(x,y)^{2}}$$

proof:

Pick the same coupling

$$
\begin{aligned}
\Delta_{x}(t+1) &\leq \mathbb{Pr}[X_{t+1} \neq Y_{t+1}] \\
&= \mathbb{Pr}[X_{t+1}\neq Y_{t+1}|X_{t} \neq Y_{t}]\Delta_{x}(t)\\
&= (1 - \sum_{x} K(X_{t}, x) K(Y_{t}, x))\Delta_{x}(t)\\
&\leq (1 - |\Omega|\min_{x, y} K(x, y)^2)\Delta_{x}(t)
\end{aligned}
$$


So

$$\Delta_{x}(t) \leq (1 - |\Omega|\min_{x, y} K(x, y)^2)^{t}$$

Let 
$$(1 - |\Omega|\min_{x, y} K(x, y)^2)^{t} \leq \frac{1}{2e}$$

$\blacksquare$

The above also proves the Fundamental Theorem of Markov Chain.



Theorem: For any Markov Chain, $\tau(\epsilon) \leq O(\tau_{mix}\log\frac{1}{\epsilon})$

#### Coloring

Try to assign $q$ colors for a graph with maximum degree $\Delta$.

We want to sample proper color assignments.

Define the coupling as follows $(X, Y)$.

Randomly choose a vertex and a color, try to change the color in both $X$ and $Y$ of corresponding vertex.

$$
\begin{aligned}
\mathbb{E}[d(X_{t+1}, Y_{t+1})] &= \mathbb{Pr}[A](d(X_{t}, Y_{t})) + \mathbb{Pr}[B](d(X_{t}, Y_{t}) + 1) + \mathbb{Pr}[C](d(X_{t}, Y_{t}) - 1)\\
&\leq d(X_{t}, Y_{t}) + \mathbb{Pr}[B] - \mathbb{Pr}[C] \\
&\leq d(X_{t}, Y_{t}) + \frac{2\Delta d(X_{t}, Y_{t})}{nq} - \frac{d(X_{t}, Y_{t})(q - 2\Delta)}{nq}\\
&= (1 - \frac{q - 4\Delta}{nq})d(X_{t}, Y_{t})
\end{aligned}
$$

Also $d(X_{0}, Y_{0}) \leq n$

So

$$\mathbb{E}[d(X_{t}, Y_{t})] \leq n(1 - \frac{q-4\Delta}{nq})^{t}$$

$$\mathbb{Pr}[d(X_{t}, Y_{t}) \geq 1] \leq \mathbb{E}[d(X_{t}, Y_{t})] \leq n(1 - \frac{q-4\Delta}{nq})^{t} \leq \delta$$


So to achieve $\frac{1}{n}$ error, we need $O(nq\log n)$ steps. 

**Also we need $q \geq 4\Delta + 1$**

### Path coupling

Path coupling is defined on the pre-metric. And it is the property that holds for adjacent vertices and can be extend to the whole $\Omega$.

Definition (pre-metric): A pre-metric defined on $\Omega$ holds that for any adjacent edge $uv$, $d(uv) = d(u, v)$.


Definition (path coupling): Define $(X', Y')$ is a coupling define on a pre-metric graph. If for any adjacent vertices $(x, y)$ holds that 

$$\mathbb{E}[d(X', Y')|(x, y)] \leq (1 - \alpha)d(x, y)$$

Then for every pair vertices, they all hold the above inequality.

insight: The original coupling is about to converge. And the uniform weighted graph is naturally holds the pre-metric.

proof:

For any pair of vertices $(s, t)$. 

Chose an arbitrary shortest path $(s=u_{0}, u_{1}, u_{2}, \cdots, u_{k}, t=u_{k+1})$.



Naturally extend the coupling into multi-vertices coupling $(U_{0}, U_{1}, U_{2}, \cdots, U_{k}, U_{k+1})$.



$$
\begin{aligned}
\mathbb{E}[d(S, T)] &= \mathbb{E}[\sum_{i=0}^{k}d(U_{i}, U_{i+1})] \\
&= \sum_{i=0}^{k}\mathbb{E}[d(U_{i}, U_{i+1})] \\
&\leq \sum_{i=0}^{k}(1-\alpha)d(u_{i}, u_{i+1})\\
&= (1-\alpha)d(s, t)
\end{aligned}
$$

$\blacksquare$

#### Coloring with Path coupling theorem

Theorem: If $q \geq 2\Delta + 1$, then the metropolis rule mixes in time $O(n\log n)$.

First we need to modify the graph to let it be a pre-metric graph in order to use path coupling theorem. 

Consider the metric $d(X, Y)$ calculating how many different colors of color configuration $X$ and $Y$. Sometime we cannot find a path of proper exchange, so we need to allow improper color configuration. Such that there are total $q^{n}$ vertices in the graph.

We can use metropolis rules to let their probability is $0$ in $\pi$. Also if we bound the total variance, we can still bound the "real" total variance. 

Then we need to design the path coupling procedure. We can only consider $d(X', Y'|x, y)$, $x$ and $y$ are adjacent with path coupling.

Assume the exact different color of $x$ and $y$ are on the vertex $u$.

In general, we choose a vertex $v$ and a color $c$ randomly, then try to change $v$'s color into $c$.

This is not the complete procedure, but we can try to analyze this. We denote $N(u) \bigcup \{u\} = N^{*}(u)$. 

If $v$ is not in $N^{*}(u)$, then $d(X', Y') = d(x, y)$. 

If $v = u$, then $\mathbb{E}[d(X', Y')] \leq \frac{\Delta}{q}d(x, y) + (1 - \frac{\Delta}{q})(d(x, y) - 1)$.

If $v \in N^{*}(u)$, but $u \neq v$, if $c = c_{x}$ or $c = c_{y}$ then $d(X, Y) \leq d(x, y) + 1$ otherwise $d(X, Y) = d(x, y)$.

Sum all the inequalities above, we get

$$\mathbb{E}[(X', Y')|(x, y)] \leq d(x, y) - \frac{q - 3\Delta}{nq} = 1 - \frac{q - 3\Delta}{nq} \leq (1 - \frac{1}{nq})d(x, y)$$

When $q \geq 3\Delta + 1$.

To improve this bound, we need to specify when $c = c_{x}$ or $c = c_{y}$, we can reorder the configuration. To achieve

$$\mathbb{E}[(X', Y')|(x, y)] \leq d(x, y) - \frac{q - 3\Delta}{nq} = 1 - \frac{q - 3\Delta}{nq} \leq (1 - \frac{1}{nq})d(x, y)$$

Which we only need $q \geq 2\Delta + 1$.


### Coloring with Heat bath chain

The main motivation of the path of metropolis rule is that try to construct a coupling such that the probability of $d(x, y) + 1$ is low.

One trivial way is to increase $q$. Beyond that path coupling consider just consider vertices pairs that are adjacent in order to decrease the "controversy".

Now let's focus on heat bath chain.

Instead of metropolis rule that randomly pick a vertex and a color then change the configuration. Heat bath chain randomly chooses a vertex then samples from the proper color.

(Obviously it may break the pre-metric requirement)

Here is a simple way: randomly chooses a vertex $u$. Denote the proper colors for $u$ under configuration $X$ as $A(X, u)$. 

Then for configuration $X, Y$, we sample from $\max(|A(X, u)|, |A(Y, u)|)$. With probability $\frac{|A(X, u) \bigcap A(Y, u)|}{\max(|A(X, u)|, |A(Y, u)|)}$ we choose the same color. Obviously we can properly assign other events.

Then we analyze this coupling

$$\mathbb{E}[d(X', Y')|(x, y)] = \sum_{v}\mathbb{E}[c_{X'}(v) \neq c_{Y'}(v)]$$

$$\mathbb{E}[c_{X'}(v) \neq c_{Y'}(v)] = \mathbb{Pr}[u=v]\mathbb{Pr}[c_{X'}(v) \neq c_{Y'}(v)|u=v] + \mathbb{Pr}[u\neq v]\mathbb{Pr}[c_{X'}(v) \neq c_{Y'}(v)|u\neq v]$$

$$
\begin{aligned}
\mathbb{Pr}[c_{X'}(v)\neq c_{Y'}(v)|u=v] &= 1 - \frac{|A(X, u) \bigcap A(Y, u)|}{\max(|A(X, u)|, |A(Y, u)|)} \\
&\leq \frac{1}{q - \Delta}|u\sim v: c_{x}(v) \neq c_{y}(u)|
\end{aligned}
$$

$$
\mathbb{Pr}[c_{X'}(v) \neq c_{Y'}(v)|u\neq v] = \frac{d(x, y)}{n}
$$

Sum all these equalities and inequalities

$$
\mathbb{E}[d(X', Y')|(x, y)] \leq \frac{\Delta d(x, y)}{n(q - \Delta)} + (1 - \frac{1}{n})d(x, y)
$$

If $q \geq 2\Delta + 1$,

$$
\mathbb{E}[d(X', Y')|(x, y)] \leq (1 - \frac{1}{n(\Delta + 1)})d(x, y)
$$

So for heat-bath, $q \geq 2\Delta + 1$ and trivial coupling method lead to $\Theta(n \log n)$ mixing time.

#### Triangle-free graph

Now image that the given graph is triangle-free. Then $A(X, u)$ can be very large. Maybe better than $q - \Delta$ which can leads to a better result.

Now analyze the $A(X, u)$

$$A(X, u) = \sum_{c} \prod_{v \sim u} (1 - X_{v, c})$$

For triangle-free graph $\mathbb{E}[\prod_{v \sim u} (1 - X_{v, c})] = \prod_{v \sim u} (1 - \mathbb{E}[X_{v, c}])$

We denote the information about $V - N^{*}(u)$ as $\mathcal{F}$.

$$
\begin{aligned}
\mathbb{E}[A(X, u)|\mathcal{F}] &= \sum_{c}\prod_{v\sim u}(1 - \mathbb{E}[X_{v, c}]) \\
&= \sum_{c}\prod_{v\sim u}(1 - \frac{1}{|A(X, v)|}) \\
&\leq  q\prod_{c}\prod_{v\sim u}(1 - \frac{1}{|A(X, v)|})^{\frac{1}{q}} \\
&= q \prod_{v\sim u}\prod_{c\in A(X, v)} (1 - \frac{1}{|A(X, v)|})^{\frac{1}{q}} \\
&\leq q e^{-\frac{\Delta}{q}}
\end{aligned}
$$

Recall the McDiarmid's inequality. 

Let $X_{v,c}$ s be the variables (NB: here are actually $d(u)$ variables), $f(.) = |A(X, u)|$.  

$f$ is 1-Lipschitz function.

So 

$$\mathbb{Pr}[|f(x_{1}, \cdots, x_{n}) - \mathbb{E}f(x_{1}, \cdots, x_{n})| \geq t ] \leq 2e^{-\frac{t^{2}}{2\Delta}}$$

So 

$$\mathbb{Pr}[|A(X, u)| \leq q e^{-\frac{\Delta}{q}}(1 - \epsilon)] \leq 2e^{-\epsilon^{2}q}$$

By union bound,

$$\mathbb{Pr}[\exists u:|A(X, u)| \leq q e^{-\frac{\Delta}{q}}(1 - \epsilon)] \leq 2ne^{-\epsilon^{2}q}$$

$\blacksquare$

### Mixing time using eigenvalues

Here we consider **reversible Markov Chains**.

For any function $f, g$, we consider inner-product space as

$$\langle f, g \rangle = \sum_{x} f(x)g(x)\pi(x)$$

$$||f|| = \langle f, f \rangle = \sum_{x}f^{2}(x)\pi(x)$$

It follows that $K$ is self-adjoint.

With spectral theorem, $K$ has $n$ eigenvalues.

By stochasticity, $\forall i \leq n, |\lambda_{i}| \leq 1$

Some results about the characteristics of reversible Markov Chain.

irreducible <-> $\lambda_{2} < 1$

aperiodic <-> $\lambda_{|\Omega|} > -1$

Why eigenvalues are "$l_{2}$ properties" about the chain?

Definition: ($l_p$- distance) 

$$ \Vert  \frac{K^t(x, \cdot)}{\pi(\cdot)} - 1 \Vert_p = \left (\sum_{y} \pi(y) |\frac{K^{t}(x, y)}{\pi(y)} - 1|^p \right )^{\frac{1}{p}}$$

Compare with $|| \cdot ||_{TV}$

$\cdot||_{TV} = \frac{1}{2} ||\cdot||_1 \leq \frac{1}{2}||\cdot||_2$

Is this a general rule?

Theorem: Let $\lambda^{*} = \max\{\lambda_{2}, |\lambda_n|\}$, 

$$\Vert \frac{K^{t}(x, \cdot)}{\pi(\cdot)}  - 1\Vert_{2} \leq \frac{\lambda^{*^{2t}}}{\pi(x)}$$

Consider

$$\Vert \frac{K^{t}(x, \cdot)}{\pi(\cdot)}  - 1\Vert_{2} = \langle \frac{K^{t}(x, \cdot)}{\pi(\cdot)}  - 1, \frac{K^{t}(x, \cdot)}{\pi(\cdot)}  - 1\rangle$$

Then project $\frac{K^{t}(x, \cdot)}{\pi(\cdot)}  - 1$ into $K$ space. 

Notice: $\boldsymbol{1} = \psi_1$

$$ \frac{K^t(x, \cdot)}{\pi(\cdot)} - 1 = \sum_{i > 1} \langle \frac{K^t(x, \cdot)}{\pi(\cdot)}, \psi_i  \rangle  \psi_i  = \sum_{i > 1}\lambda_i^t \psi_i(x)\psi_i$$

$$\Vert \frac{K^t(x, \cdot)}{\pi(\cdot)} - 1  \Vert_2 = \sum_{i > 1}\lambda_i^{2t} \psi_i^2(x) \leq \lambda^{*} \sum_{i>1} \psi_i^2(x) \leq \frac{\lambda^{*^{2t}}}{\pi(x)}$$

Such a magic

$$
\begin{aligned}
\sum_{i} \psi_i^2(x) &= \sum_{i} \langle \psi_i, \frac{1_x}{\pi} \rangle ^2 \\
&= 
\Vert \sum_i \langle \psi_i, \frac{1_x}{\pi} \rangle \psi_i \Vert ^2 \\
&= 
\Vert \frac{1_x}{\pi} \Vert ^2 \\
&= \frac{1}{\pi(x)}
\end{aligned} 
$$

select a vertex with high probability as warm start.

## Path technology

### Dirichlet Form

For two functions $f, g$, define 

$$\mathcal{E}(f,g) = \left \langle (I - K)f, g \right \rangle$$

(easy to see that $I - K$ is self-adjoint)

$\mathcal{E}(f, g) = \frac{1}{2}\sum_{x, y} (f(x) - f(y))(g(x) - g(y))\pi(x)K(x, y)$

NB: actually we just need to enumerate all the edge. The reason is that if $(x, y) \notin E$, then $K(x, y) = 0$

Dirichlet form of $f$

$\mathcal{E}(f, f) = \frac{1}{2}\sum_{x, y} (f(x) - f(y))^2 \pi(x) K(x, y)$


Variance of $f$

$$Var(f) = \Vert f - \mathbb{E}_{\pi}f  \Vert^2 = \frac{1}{2}\sum_{x, y}(f(x) - f(y))^2\pi(x)\pi(y)$$


Definition: Poincare constant 

$$\alpha = \min_{f} \frac{\mathcal{E}(f, f)}{Var(f)}$$

If $K$ is reversible, then poincare constant is $1 - \lambda_2$

For a lazy chain with Poincare constant $\alpha$,

$$\tau_x(\epsilon) \leq O(\frac{\log \frac{1}{\epsilon \pi(x)}}{\alpha})$$

So if we can bound the poincare constant, we can bound the mixing time.

Consider the multicommodity flow problem(reversible Markov chain),

Define 

$$f(e) = \sum_{e \in P_{x, y}}\pi(x)\pi(y)$$

$$Q(e=uv) = \pi(u)K(u, v) = \pi(v)K(v, u)$$

Define the congestion of an edge $e$ as $\frac{f(e)}{Q(e)}$

For any reversible Markov chain, for any two states $x, y \in \Omega$, 

$$\frac{1}{\alpha} \leq \max_{e} \frac{f(e)}{Q(e)} \cdot \max_{x, y}|P_{x, y}|$$

Actually, $P_{x, y}$ can be bounded by the diameter of the graph then the $n$.

proof:
For any function $f$

$$
\begin{aligned}
Var(f) 
&= 
\frac{1}{2}\sum_{x, y} (f(x) - f(y))^2\pi(x)\pi(y) \\
&= 
\frac{1}{2}\sum_{x, y} (\sum_{e \in P_{x,y}}(f(e^+) - f(e^-)) )^2\pi(x)\pi(y) \\
&\leq \frac{1}{2}\sum_{x, y} |P_{x,y}|\sum_{e \in P_{x,y}}(f(e^+) - f(e^-))^2\pi(x)\pi(y) \\
&\leq  \max_{x,y}|P_{x,y}| \cdot \frac{1}{2}\sum_{x, y} \sum_{e \in P_{x,y}}(f(e^+) - f(e^-))^2\pi(x)\pi(y) \\
& \leq \max_{x,y}|P_{x,y}| \cdot \frac{1}{2} \sum_{e}(f(e^+) - f(e^-))^2 \sum_{e \in P_{x, y}} \pi(x)\pi(y) \\
&= \max_{x,y}|P_{x,y}| \cdot \frac{1}{2} \sum_{e}(f(e^+) - f(e^-))^2 Q(e) \frac{f(e)}{Q(e)} \\
&= \max_{x,y}|P_{x,y}| \cdot \frac{1}{2} \sum_{e=(x,y)}(f(e^+) - f(e^-))^2 \pi(x)K(x, y) \frac{f(e)}{Q(e)} \\
&= \max_{x,y}|P_{x,y}| \cdot \mathcal{E}(f, f) \frac{f(e)}{Q(e)} (\text{If x, y are not connected then} K(x,y)=0) \\
\end{aligned}
$$

Fractional version

Define $\mu_{x, y}(P)$ as the probability of choosing $P$ as the path from $x \rightarrow y$.

Then update the definition for $f(e)$

$$f(e) = \sum_{x, y} \pi(x) \pi(y)\sum_{e\in P \sim \mu_{x,y}} \mu_{x, y}(P)$$

Now calculate the Poincare constant

$$
\begin{aligned}
Var(f) 
&= 
\frac{1}{2}\sum_{x, y} (f(x) - f(y))^2\pi(x)\pi(y) \\
&= 
\frac{1}{2} \pi(x)\pi(y) \sum_{x, y} (\sum_{P}\mu_{x, y}(P)\sum_{e\in P}(f(e^+) - f(e^-)) )^2 \\
&\leq \frac{1}{2}\sum_{x, y} |P_{x,y}|\sum_{e \in P_{x,y}}(f(e^+) - f(e^-))^2(\sum_{P}\mu_{x, y}^{2}(P))\pi(x)\pi(y) \\
&\leq \frac{1}{2}\sum_{x, y} |P_{x,y}|\sum_{e \in P_{x,y}}(f(e^+) - f(e^-))^2\pi(x)\pi(y) \\
&\leq  \max_{x,y}|P_{x,y}| \cdot \frac{1}{2}\sum_{x, y} \sum_{e \in P_{x,y}}(f(e^+) - f(e^-))^2\pi(x)\pi(y) \\
& \leq \max_{x,y}|P_{x,y}| \cdot \frac{1}{2} \sum_{e}(f(e^+) - f(e^-))^2 \sum_{e \in P_{x, y}} \pi(x)\pi(y) \\
&= \max_{x,y}|P_{x,y}| \cdot \frac{1}{2} \sum_{e}(f(e^+) - f(e^-))^2 Q(e) \frac{f(e)}{Q(e)} \\
&= \max_{x,y}|P_{x,y}| \cdot \frac{1}{2} \sum_{e=(x,y)}(f(e^+) - f(e^-))^2 \pi(x)K(x, y) \frac{f(e)}{Q(e)} \\
&= \max_{x,y}|P_{x,y}| \cdot \mathcal{E}(f, f) \frac{f(e)}{Q(e)} (\text{If x, y are not connected then} K(x,y)=0) \\
\end{aligned}
$$

So the same theorem holds.

$\blacksquare$

There are some intrinsic gaps between this bound and the tight bound by $\log n$.

### All or nothing theorem

Def of self-reducible problem:

For every instance of one specific NP search problem, if the set of its solutions can be divided into polynomial size subsets corresponding to the same NP search problem with smaller instances(these instances can be generated in polynomial time). Then this NP search problem is self-reducible problem.

Is this def the same as Sipser?

Thm: For any self-reducible problem, if there exists a polynomial time counting algorithm that gives $1 + poly(n)$ multiplicative error, then there is an FPRAS.

(Recall that for self-reducible problem, $\text{FPRAS}  \leftrightarrow \text{FPAUS}$)

The basic intuition is that we prove that there is a FPAUS.

If we can use the polynomial approximation factor to build a Markov chain with fast mixing time.

The good situation is that every vertex(state) in Markov chain represents a proper answer(element needed to be counted).

Of the proportion of proper vertices is large enough, like $\frac{1}{poly(n)}$.

So we can derive the FPRAS.

Here We will use the DNF(different from the counting problem in the notes) as a demonstration. 

Consider a tree from the root to the leaves, one step downward means that a variable is assigned. 

Define a order of variables $l_1, l_2, \cdots, l_n$, At level $i$, assign the $v_i$ true of false.

Basically this is a decision tree, every node in the tree is a configuration.

Denote the actual count of configuration $x$ as $N(x)$, the FPRAS with parameter $\alpha$ returns a answer $\hat{N}(x)$, $\frac{N(x)}{\alpha} \leq \hat{N}(x) \leq \alpha N(x)$.

For simplicity, we can assume $\hat{N}(x)$ is deterministic. (Otherwise we can run $\log \frac{1}{\epsilon}$ to boost).

For an edge $(e, v)$, w.l.o.g. $e$ is the father of $v$. 

Define $w(e, v) = \hat{N}(v)$. To make it a Markov chain, for a specific vertex $x$, whose father is $a$, sons are $b$ and $c$. Define $Z_{x} = \hat{N}(x) + \hat{N}(b) + \hat{N}(c)$, $K(x, a) = \frac{\hat{N}(x)}{Z_{x}}$, $K(x, b) = \frac{\hat{N}(b)}{Z_{x}}$ and $K(x, c) = \frac{\hat{N}(c)}{Z_{x}}$.


Now consider random walk on this graph. Define $Z = \sum_{x}Z_{x}$. It follows that $\pi(x) = \frac{Z_{x}}{Z}$. 

Assume $x$ is the father of $y$ in the following equation.

$$\sum_{(x, y) \in E} \pi(x)K(x, y) = \sum_{(x, y) \in E} \frac{Z_{x}}{Z} \frac{\hat{N}(y)}{Z_{x}} = \frac{Z_{y}}{Z} = \pi(y)$$

Each assignment is actually a leaf. Because leaves have the same level, so they has the same probability(has only one edge connecting to its father).

Then we need to bound the sum of leaves' probability.

Lemma: random walk ends at leaves with probability $\frac{O(1)}{\alpha n}$

proof:

Use $L$ to denote the actual amount of leaves. 

Observe that the sum of the weight of edges from level $i$ to level $i+1$ is at most $\alpha L$.

Because there are at $n$ levels, so sum of all the weight is at most $2\alpha Ln$

The probability that ends at leaves is at least $\frac{1}{2\alpha n}$

$\blacksquare$

That's $\frac{1}{poly(n)}$

Now we need to bound the mixing time.

Although the structure of tree means that there is only simple path, it seems not easy to use the path coupling lemma.

We choose path technology here.

For a specific edge $e = (u, v)$, $u$ is the father of $v$.

$f(e) = (\sum_{x \in son(v)} \pi(x)) (1 - \sum_{x \in son(v)} \pi(x)) \leq \frac{1}{Z}2\alpha n N(v)$

$Q(e) = \pi(u)K(u,v) = \frac{Z_u}{Z} \frac{\hat{N}(v)}{Z_{u}} = \frac{\hat{N}(v)}{Z}$

$\max_{e} \frac{f(e)}{Q(e)} \leq 2\alpha^2 n$

$\max_{x, y} |P_{x, y}| \leq 2n$

By the path technology

$$\tau_x(\epsilon) \leq O(2\alpha^2n^2\log \frac{1}{\epsilon \pi(x)})$$

Choose x as root. Then $\pi(root) = \frac{Z_{root}}{Z} \geq \frac{1}{2\alpha n}$

So,

$$\tau_x(\epsilon) \leq O(2\alpha^2n^2\log \frac{2\alpha n}{\epsilon})$$

So we can get a FPAUS.


### Implementation

Random walk on hypercube.

First consider using the path coupling.

Obviously the metric satisfies the pre-metric constrains.

consider an edge $e = (x, y)$.

coupling with randomly picking a bit then turn to the same neighbor.

$$
\begin{aligned}
\mathbb{E}[d(X, Y|x, y)] &= (1 - \frac{1}{n})d(x, y)
\end{aligned}
$$

So $d(X, Y) \leq n(1 - \frac{1}{n})^{T}$, $T = O(n\log n)$



<!-- $$
\begin{aligned}
\mathbb{E}[A(X, u)] &= \mathbb{E}[\sum_{c} \prod_{v \sim u} (1 - X_{v, c})] \\
&= \mathbb{E}[\sum_{c} \prod_{v \sim u} (1 - X_{v, c})]
\end{aligned}
$$ -->

<!-- Let  $W = \frac{|A(X, u) \bigcap A(Y, u)|}{\max(|A(X, u)|, |A(Y, u)|)}$

$$
\begin{aligned}
\mathbb{E}[d((X', Y')|(x, y))] &= \mathbb{Pr}[c_{X}(u) \neq c_{Y}(u)](W(d(x, y) - 1) + (1 - W)d(x, y)) + \mathbb{Pr}[c_{X}(u) = c_{Y}(u)](W(d(x, y)) + (1 - W)(1 + d(x, y)))\\
&\leq \mathbb{Pr}[c_{X}(u) \neq c_{Y}(u)][d(x, y) - 1] + 1 - W\\
&\leq \frac{d(x, y)}{n} [d(x, y) - 1] + \frac{d(x, y)}{n(q - \Delta)}

\end{aligned}
$$ -->


<!-- d(x, y) + (1 - \frac{|A(X, u) \bigcap A(Y, u)|}{\max(|A(X, u)|, |A(Y, u)|)})  -->