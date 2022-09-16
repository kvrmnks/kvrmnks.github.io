---
title: Counting and sampling notes
date: 2022-9-15 20:31:00
tags: [tcs]
---

A notes for CSE 599: Counting and Sampling.

What is sampling: Assume there is a giant space $\Omega$(usually finite). There is a function $w: \Omega \rightarrow \mathbb{R}_{+}$. And the unknown partition function $Z = \sum_{x \in \Omega'} w(x)$. We need to generate a sample $x$ with probability $\frac{w(s)}{Z}$. 

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
|\mu(\Omega - X) - \nu(\Omega - X)| &= |\nu(\Omega - X) - \mu(\Omega - X)| \\
&= | (1 - \mu(X)) - (1 - \nu(X)) | \\
&= |\nu(X) - \mu(X)| \\
&= |\mu(X) - \nu(X)| 
\end{align}
$$
So 

$$\max_{X \subset \Omega}|\mu(X) - \nu(X)| = \frac{1}{2} \sum_{x \in \Omega}|\mu(x) - \nu(x)| $$


Definition of FPAUS: 

