# Homework Assignment 2

## Problem 1 - True-False

### 1. A random variable is discrete if its support is countable and there exists an associated probability density function (pdf)

**FALSE**. A random variable is discrete if its support is countable and there exists an associated probability mass function (pmf) ($p: R\rightarrow[0,1]$).

### 2. Probability mass functions have a lower bound of 0 and an upper bound of 1

**TRUE**.

### 3. The set of all possible realizations of a random variable is called its probability density

**FALSE**. The set of all possible realizations of a random variable is called its support.

### 4. The expected value of a discrete random variable is always part of its support, that is, $E[X] \in R_X$

**FALSE**. This is not always the case. Take a coin flip where heads is 0 and tails is 1. The expected value is 0.5, which is not part of the support (${0, 1}$).

### 5. Continuous random variables are functions which map points from the sample space to the real numbers

**TRUE**.

### 6. We can formulate most parametric Bayesian models as a generative process, by which we first sample from the likelihood and then use the synthetic data point to sample from the prior

**TRUE**.

### 7. The Bayesian posterior $p(\theta | y)$ for continuous parameter vectors $\theta\in R^D$ is just another density function. That means, its integral $\int p(\theta | Y=y)d\theta \ne 1$ for some y

**FALSE**. In order for $p$ to be a pdf, integrating the support must yield 1.

### 8. Each realization of a continuous random variable has a probability of zero

**TRUE**.

## Problem 2 - Expectations I

## Problem 3 - Expectations II

### 1. $Var[X] = E[X^2] - E[X]^2$

We know that the variance of a random variable, $X$, is

$$Var[X] = E[(X - E[X])^2]$$

This can be expanded to be

$$Var[X] = E[(X - E[X]) \cdot (X - E[X])]$$
$$Var[X] = E[X^2 - 2XE[X] + E[X]^2]$$

Since, $E[X + Y] \equiv E[X] + E[Y]$, we have

$$Var[X] = E[X^2] - E[2XE[X]] + E[X]^2$$

Since $E[X]$ is a constant, and $E[c\cdot X] \equiv c\cdot E[X]$, where $c$ is a constant, we have

$$Var[X] = E[X^2] - 2E[X]E[X] + E[X]^2$$
$$Var[X] = E[X^2] - 2E[X]^2 + E[X]^2$$
$$Var[X] = E[X^2] - E[X]^2$$

### 2. $Var[\alpha X + \beta] = \alpha^2 Var[X]$

We know that the variance of a random variable, $X$, is

$$Var[X] = E[(X - E[X])^2]$$

If we replace $X$ with $\alpha X + \beta$, we have

$$Var[X] = E[((\alpha X + \beta) - E[\alpha X + \beta])^2]$$

We know that $E[\alpha X + \beta] \equiv \alpha E[X] + \beta$, so

$$Var[X] = E[((\alpha X + \beta) - (\alpha E[X] + \beta))^2]$$
$$Var[X] = E[(\alpha X + \beta - \alpha E[X] - \beta)^2]$$
$$Var[X] = E[(\alpha X - \alpha E[X])^2]$$

The $\alpha$ can be factored out

$$Var[X] = E[(\alpha\cdot(X - E[X]))^2]$$
$$Var[X] = E[\alpha^2\cdot(X - E[X])^2]$$

Since $\alpha$ is a constant, and $E[c\cdot X] \equiv c\cdot E[X]$, where $c$ is a constant, we have

$$Var[X] = \alpha^2\cdot E[(X - E[X])^2]$$
$$Var[X] = \alpha^2\cdot Var[X]$$

### 3. $X\sim Normal(\mu=0,\sigma=1) \rightarrow \overline{X}\sim Normal(\mu=3,\sigma=5)$

Say that $\overline{X} = \alpha X + \beta$, then 

$$E[\overline{X}] = \alpha E[X] + \beta$$
$$\sqrt{Var[\overline{X}]} = \alpha^2\sqrt{Var[X]}$$

From this we have that

$$\alpha = \sqrt{5}$$
$$\beta = 3$$

So the transformation that needs to be applied is $\sqrt{5}\cdot X + 3$

## Problem 4 - Simple Bayes' Rule

## Problem 5 - Murder Mystery Revised

A teacher is picking students' names from a hat. There are five students: Bob, Brandon, Billy,
Bart, and Ben. There are two hats to choose from. The first hat (hat A) has the names Bob, 
Brandon, Billy, and Billy. The second hat (hat B) has the names Bob, Brandon, Bart, Bart, and Ben.
The teacher will choose the hat to pull from at random, so the probability of either hat being 
selected is 0.5. The probabilities are shown in the tables below.

### Probability of choosing each student for Hat A -- $p(Student | A)$

| Student | Probability |
| :------ | ----------: |
| Bob     |        0.25 |
| Brandon |        0.25 |
| Billy   |        0.50 |
| Bart    |           0 |
| Ben     |           0 |

### Probability of choosing each student for Hat B -- $p(Student | B)$

| Student | Probability |
| :------ | ----------: |
| Bob     |         0.2 |
| Brandon |         0.2 |
| Billy   |           0 |
| Bart    |         0.4 |
| Ben     |         0.2 |

### Probability of choosing each student -- $p(Student)$

This is calculated as $p(A)\cdot p(Student | A) + p(B)\cdot p(Student | B)$

| Student | Probability |
| :------ | ----------: |
| Bob     |       0.225 |
| Brandon |       0.225 |
| Billy   |       0.250 |
| Bart    |       0.200 |
| Ben     |       0.100 |

### Probability of each event -- $p(Hat, Student)$

This is calculated as $p(Hat)\cdot p(Student)$

|         | Hat A | Hat B |
| Bob     | 0.125 |   0.1 |
| Brandon | 0.125 |   0.1 |
| Billy   | 0.250 |     0 |
| Bart    |     0 |   0.2 |
| Ben     |     0 |   0.1 |

The `murder_myster_revised.py` script contains the code for simulating this story. The results
have been copied below.

|         |  Hat A |  Hat B |
| Bob     | 0.1224 | 0.0998 |
| Brandon | 0.1270 | 0.0941 |
| Billy   | 0.2535 | 0.0000 |
| Bart    | 0.0000 | 0.2004 |
| Ben     | 0.0000 | 0.1028 |

As can be seen in the table, the simulated probabilities largely match the calculated ones.
Running only 1000 simulation produces results that are not too terrible, but running with
10,000 simulation (as was done for the table above) or more will produce much better results.

## Problem 6 - Priors, Posteriors, Sensitivity, Specificity

## Problem 7 - AI-Assisted Programming
