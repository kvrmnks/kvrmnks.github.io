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
Every Markov chain has a stationery distribution(may not unique).


First of all the Markov kernel must have eigenvalue $1$ and corresponding eigenvector $v$. 

It is easy to show that $\mathrm{det}(K - I) = 0$, as the sum of every column of $K$ is exactly $1$.

Now let $\pi = (|v_{1}|, |v_{2}|, \cdots, |v_{k}|)^{T}$.  We show that $\pi$ is a stationery distribution.

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

It follows that $\frac{\pi}{Z}$ is the stationery distribution. 

### Mixing of Markov Chain
Definition(Irreducible Markov Chain): A Markov chain is irreducible iff for any states $x$, $y$, it exits $t$ such that $K^{t}(x,y) > 0$.

Definition(aperiodic): A Markov Chain is aperiodic if for all $x, y$ we have $\gcd\{t|K^{t}(x,y)>0\} = 1$

Lemma: Let $K$ be an irreducible, aperiodic Markov Chain. Then there exists $t>0$ such that for all $x, y$

$$K^{t}(x,y) > 0$$

**Actually I do not know how to formally prove this...**

Theorem (Fundamental Theorem of Markov Chains): Any irreducible and aperiodic Markov chain has a **unique** stationery distribution. Futhermore, for all $x, y$,

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

Lemma: Metropolis chain is reversible with stationery distribution $\pi$

(But how to prove that $\pi$ is the stationery distribution?)

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

**Also we need $q > 4\Delta + 1$**

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

