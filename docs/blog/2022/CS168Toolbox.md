---
title: CS168 The Modern Algorithmic Toolbox
date: 2022-9-7 10:14:00
tags: [TCS]
---

This is my notes about the CS168 in Stanford University

## Dimensionality Reduction

Want to reduce the large dimension into small dimension ( usually independent with input size )  while preserving distance.

### Distance

distance or similarity

**exact** distance: 1 - [x==y]

similarity of set ( or multi-set ): Jaccard Similarity $J(S,T) = \frac{|S \bigcap T|}{|S\bigcup T|}$


$l_{p}$ distance.

### framework

reduce dimension while preserving expect.

Then use independent trials.

### exact distance

use universal hash function assumption

assume $h: U \rightarrow [b]+1$

k hash function $h_{1}, h_{2}, ... , h_{k}$

#### $\epsilon$ -  Heavy Hitters


$$\# = \min_{i=1}^{k} B(f_{i}(x)) = \min_{i=1}^{k} \sum_{j=1}^{n}[f_{i}(x) = f_{j}(x)]$$

$$E[\#] = \min_{i=1}^{k} \sum_{j=1}^{n}E[[f_{i}(x) = f_{j}(x)]] = \#x + \frac{n-\#x}{b} \leq \#x + \frac{n}{b}$$

use Markov's inequality

$$\mathrm{Pr}[\# - \#x > \delta \frac{n}{b}] \leq \frac{1}{\delta}$$

to achieve $(\delta, \epsilon)$, let $b = \frac{2}{\epsilon}$, $\delta = 2$.

Then use independent trials $\frac{1}{2^{p}} < \delta$, then $p = \log(\frac{1}{\delta})$.

### Jaccard similarity

pick a random permutation of $U$. 

hash each element to the smallest element.

### $l_{2}$ distance - Johnson-Lindenstrauss transform 

motivation: random projection (inner product with a vector generated by standard Gaussian distribution)

random vector  $\textbf{r} \sim N^{n}(0, 1)$

$$X = \textbf{x}_{1}\textbf{r} - \textbf{x}_{2}\textbf{r} = \sum_{i=1}^{n} (x_{1,i} - x_{2, i})r_{i} \sim N(0, l_{2}^2)$$

which means that $X$ is an unbiased estimator of $l^{2}_{2}$.

### other distances ...
what about cosine similarity, edit distance and wasserstein distance.


## Learning (Binary classification here)

Assume data are samples from a prior distribution $D$ on the universe $U$.

element has its only label.

mainly cares about the sample complexity.
### finite well-separated case

finite: there is a function set $\{f_{1}, ..., f_{h}\}$ including the ground truth $f^{*}$.

well-separated: if $f_{i} \neq f^{*}$, then the generalization error is at least $\epsilon$.

Theorem: if

$$n \geq \frac{1}{\epsilon}(\ln h+\ln \frac{1}{\delta} )$$

Then with probability $1 - \delta$, the output $f = f^{*}$.

PROOF:

$Pr[ f=^{X}f^{*} | f\neq f^{*}] \leq (1-\epsilon)^{n} \leq e^{-\epsilon n}$

$Pr[\exists f_{i} = f^{*}] \leq (h-1)e^{-\epsilon n} \leq he^{-\epsilon n}$

$he^{-\epsilon n} \leq \delta$

$n \geq \frac{1}{\epsilon}(\ln h + \ln \frac{1}{\delta})$

Q.E.D

### finite case

Theorem: if

$$n \geq \frac{c}{\epsilon}(\ln h+\ln \frac{1}{\delta})$$

Then with probability $1 - \delta$, the output $f$'s generalization error is less than $\epsilon$.

easy to drive from previous theorem.

### Linear Classifiers

Throw the assumption of finite function set.

However there is still the ground true that has the form of linear classifier.

Theorem: if

$$n \geq \frac{c}{\epsilon}(d + \ln \frac{1}{\delta})$$

Then there is a constant $c$, with probability $1 - \delta$, the generalization error is less than $\epsilon$.

proof motivation: the curse of dimensionality (approximation).

note the number of samples is linear to the dimension.

(because we use about $e^{d}$ functions to approximate in theory, but we usually calculate the superplane to express the function)

### Non-Zero Training Error and the ERM Algorithm

ERM (empirical risk minimization)

just output the function with minimum training error.

Theorem (Uniform Convergence):

if

$$n \geq \frac{c}{\epsilon ^2}(d + \ln \frac{1}{\delta})$$

then for every linear classifier, it holds that 

generalization error in training error +- $\epsilon$

Theorem (PAC for non-zero training error):

easy to drive from previous theorem

### Increasing Dimensionality

according to the previous section, when samples are larger than (or linear to) dimension, it will lead to best-fit.

but for non-zero error case, we do not know the dimension exactly. 

So we may need to flirt with line between overfitting and generalization.

when n << d, we need to increase the dimension.

#### Polynomial embedding

just add cross-product into the higher dimension.

It is better when the dimension is meaningful.

#### JL transform
actually we need to apply some non-linear operator to each dimension.

Because JL transform actually the combination of each dimension.

In real world, the kernel function is a good way to implement.


### Regularization

Regularization states that you have some preference of your model.

There are usually two views about the effect of regularization.

Bayesian view and frequentist view

#### Bayesian view

Here the regularization comes naturally from the likelihood.

For example, we assume the model is $y = \left \langle x, a\right \rangle + z$

$z \sim N(0, 1)$, $a_{i} \sim N(0, \sigma^2)$

we assume that $x$'s are fixed for simplicity.

The likelihood is 

$$\mathrm{Pr}(a)\mathrm{Pr}(\frac{data}{a}) = \prod_{i}^{d}e^{-\frac{a^2_{i}}{2\sigma^2}}\prod_{i}^{n}e^{-\frac{(y_{i}-\left \langle x_{i}, a \right \rangle)^{2}}{2}}$$

max this likelihood means minimize $\sum_{i=1}^{d}\frac{a_{i}^{2}}{2\sigma^2} + \sum_{i=1}^{n} (y_{i} - \left \langle x_{i}, a\right \rangle)^2$

The first part is regularization.

Also it shows that the regularization may depend on the hypothesis of model.
#### Frequentist view
The given example is about $l_{0}$ regularization. (define $0^0 = 0$)

$l_{0}$ regularization shows the sparsity. 

##### $l_{1}$ regularization

it can be a proxy of $l_{0}$ regularization.

## Principle Component Analysis

The motivation is that we want to map the data into a $d$ - dimension vector space.

Somehow we want to preserve the $|\prod_{S}v| \sim |v|$

Luckily, we know that $d$ - dimension space can be interpret into a span of d vectors $v_{1}, ..., v_{d}$.

And the objective function is $\max \sum_{i=1}^{n} \sqrt{\sum_{j=1}^{d} \left \langle x_{i}, v_{j} \right \rangle ^{2}}$.

why max? Because of the triangle inequality.

Usually we compact the data as a matrix $A$ whose columns states for attributes and row stand for pieces of data.

We create a new matrix $X$ of vectors $v$ whose $i$ th column is $v_{i}$, in order to model the objective function as matrix operation.

The objective function is $(AX)^{T}AX = X^{T}A^{T}AX = X^{T}U^{T}DUX$ according to spectrum theorem.

$U$ is orthogonal matrix and $D$ is diagonal matrix. 

Basically $X$ is variable that we can choose.

If $d=1$, $|Ux| = |x|$, denote $u = Ux$the objective function becomes $u^{T}Du$. 

Assume the elements of $D$ are sorted as decreasing order. $u = e_{1}$.

So $x = U^{T}e_{1}$ or x is the first column of $U$.

### Implementation (The Power Iteration)

The key problems of PCA are singular values and singular vectors.

Singular polynomial is hard to find roots ...

Maybe there are some ways to find reductions.

But here the motivation is that we pick a vector $x$ and apply to operator many times.

Theorem, for any $\delta, \epsilon > 0$, letting $v_{1}$ denote the top eigenvector of $A$, with probability at least $1-\delta$ over the choice of $u_{0}$,

$$|\langle \frac{A^{t}u_{0}}{|A^{t}u_{0}|}, v_{1} \rangle| \geq 1 - \epsilon$$

provided 

$$t > O(\frac{\log d + \log \frac{1}{\epsilon} + \log \frac{1}{\delta}}{\log \frac{\lambda_{1}}{\lambda_{2}}})$$

where $\frac{\lambda_{1}}{\lambda_{2}}$ is the spectral gap.


proof 

let $v_{1}, \cdots, v_{k}$ be k orthonormal vectors.

$$
\begin{aligned}
|\langle \frac{A^{t}u_{0}}{|A^{t}u_{0}|}, v_{1} \rangle | 
&= |\frac{\langle u_{0}, v_{1} \rangle \lambda_{1}^{t}}{\sqrt{\sum_{i=1}^{d}\langle u_{0}, v_{i} \rangle^{2} \lambda_{i}^{2t}}}| \\
&\geq |\frac{\langle u_{0}, v_{1}\rangle \lambda^{t}}{\sqrt{\langle u_{0}, v_{1} \rangle^2 \lambda_{1}^{2t} + \lambda_{2}^{2t}}}| \\
&\geq |\frac{\langle u_{0}, v_{i} \rangle \lambda^{t}}{|\langle u_{0}, v_{1} \rangle| \lambda_{1}^{t} + \lambda_{2}^{t}}|\\
&= |\frac{1}{1 + \frac{1}{\langle u_{0}, v_{1} \rangle } \frac{\lambda_{2}}{\lambda_{1}}^{t}}|
\end{aligned}
$$

So, let this < $\epsilon$.

$$ t > \frac{\log |\frac{1}{\langle u_{0}, v_{1} \rangle}| + \log \frac{1}{\epsilon}}{\log |\frac{\lambda_{1}}{\lambda_{2}}|}$$

Someone told me that $\langle u_{0}, v_{1} \rangle > \frac{\delta}{2\sqrt{d}}$ with probability $1 - \delta$. (I do not how to prove this.) 

so $\log \frac{1}{\langle u_{0}, v_{1} \rangle}  < \log d + \log \frac{1}{\delta}$ which completes the proof.

## Low-rank Matrix Decomposition

### SVD

The key method is the SVD(Singular Value Decomposition) which states that every matrix $A$ can be interpreted as $USV^{T}$

I do not willing to include the proof here, because that the constructive proof shows few motivation.

Some motivations are here 

$$A^{T}A = (USV^{T})^{T} USV^{T} = VS^{T}SV^{T}$$

According to PCA, V contains eigen-vectors of $A$.

Also 

$$ AA^{T} = (VS^{T}U^{T})^{T}(VS^{T}U^{T}) = USS^{T}U^{T} $$

The similarity holds for $U$.

Actually SVD links the eigenvalues of $A$ and $A^{T}$

Also these facts help us to calculate the SVD(just use power iteration).

### Low-rank Matrix

Recall the matrix with rank $k$ can be interpret as $\sum_{i=1}^{k}\textbf{u}_{i} \textbf{v}_{i}^{T}$.

under Frobenius norm, it can be shown the SVD derives the best approximation.

Frobenius norm 

$$||M||_{F} = \sqrt{\sum_{i,j}m^{2}_{i,j}}$$

for any matrix $A$ and its rank-k approximation using SVD $A_{k}$.

Then for any rank-k matrix $B$.

Then 

$$||A - A_{k}||_{F} \leq ||A - B||_{F}$$

---
Although we can approximate the matrix under Frobenius norm, but the decomposition is not unique.

$$A_{k} = U_{k}V^{T}_{k} = U_{k}B^{-1}BT^{T}_{k} = (U_{k}B^{-1})(T_{k}B^{T})^{T}$$

But if we extend matrix to tensor, something will happen.


## Low-rank tensor Decomposition

A rank-k $n \times n \times n$ tensor $A$ can be interpret as 

$$A_{x,y,z} = \sum_{i=1}^{k} u_{i}(x)v_{i}(y)w_{i}(z) $$

ATTENTION: $(u_{1}, \cdots, u_{k})$ linearly independent, same for $v's$ and $w's$

And we can use the notation $\oplus$.

$$A = \sum_{i=1}^{k} u_{i} \oplus v_{i} \oplus w_{i}$$

Theorem: Given a 3-tensor with rank $k$, the decomposition is unique(up to scale a constant)

### Jenrich's algorithm

1. random two unit vectors $x, y \in \mathbb{R}^{n}$ 

2. define $A_{x}, A_{y}$.

$$A_{x}(a, b) = \sum_{i=1}^{k} u_{i}(a) v_{i}(b)\sum_{j=1}^{n}w_{i}(j)x(j) = \sum_{i=1}^{k} u_{i}(a) v_{i}(b) \langle w, x_{i} \rangle$$

$$A_{y}(a, b) = \sum_{i=1}^{k} u_{i}(a) v_{i}(b)\sum_{j=1}^{n}w_{i}(j)y(j) = \sum_{i=1}^{k} u_{i}(a) v_{i}(b) \langle w, y_{i} \rangle$$


3. compute 

$$A_{x}A_{y}^{-1} = QSQ^{-1}$$

$$A_{x}^{-1}A_{y} = (Y^{T})^{-1}TY^{T}$$

4. with probability 1, $Q$ describes $(u_{1}, u_{2}, \cdots, u_{k})$ and $Y$ describes $(v_{1}, v_{2}, \cdots, v_{k})$.

5. solve the linear system to compute $(w_{1}, w_{2}, \cdots, w_{k})$.


correctness: 

$$A_{x} = UDV^{T}, A_{y} = UEV^{T}$$

$$A_{x}A^{-1}_{y} = UDE^{-1}U^{-1}$$

$$A_{x}^{-1}A_{y} = V^{T^{-1}}D^{-1}EV^{T}$$

if $x, y$ pick randomly, it's likely that $A_{x}A_{y}^{-1}$ and $A^{-1}_{x}A_{y}$'s eigenvalues are distinct, so we can distinguish different eigenvectors.

And because of the $S, T$ should be the reciprocative, so we can group correct eigenvectors.

## Spectral Graph Theory

The magic about representing the graph as matrix.

Denote rank matrix as $D$ and adjacent matrix as $A$.

Define Laplacian matrix as $L = D - A$.

Note $L$ is a symmetric matrix.

now consider

$$
Lv_{i} = deg(i)v_{i} - \sum_{j\sim i} v_{j} = \sum_{j \sim i} (v_{i} - v_{j})
$$

$$
\begin{align}
v^{T}Lv &= \sum_{i=1}^{n} v_{i} \sum_{j \sim i} (v_{i} - v_{j}) \\
&= \sum_{i<j: j \sim i}(v_{i} - v_{j})^{2}
\end{align}
$$

So if we put all the vertices on the real numberline. 
$v^{T}Lv$ is the square sum of all the path.

### Eigenvalues and Eigenvectors
$L$ has $n$ non-negative real eigenvalues because $L$ is a symmetric matrix and $v^{T}Lv \geq 0$. 

The fact is that the minimum eigenvalue is $0$. Let $v = (\frac{1}{\sqrt{n}}, \cdots, \frac{1}{\sqrt{n}})$.

$$Lv_{i} = \sum_{j \sim i} (v_{i} - v_{j}) = 0$$

Theorem: The number of zero eigenvalues of the Laplacian matrix equals the number connected components of the graph.

proof

we first show that \# connected components < \# zero eigenvalues

Let $S_{i}$ be a maximal connected components, construct a vector $v$, $v_{i} = \frac{1}{\sqrt{|S_{i}|}}  \mathbb{I}[x \in S_{i}]$

So it can form \# connected component orthonormal vectors.

Then about the other side, recall $v^{T}Lv$, if $v_{k+1}$ is orthogonal to $v_{1}, \cdots, v_{k}$, assume $v_{k+1, j} \neq 0$, then for positions of the same maximal connected component must $\neq 0$, so it must not orthogonal to all vectors.

$\blacksquare$
