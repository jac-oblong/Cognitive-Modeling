# Homework Assignment 2

## Problem 1 - True-False

### 1. A random variable is discrete if its support is countable and there exists an associated probability density function (pdf)

**FALSE**. A random variable is discrete if its support is countable and there exists an associated probability mass function (pmf) ($p: R\rightarrow[0,1]).

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

## Problem 4 - Simple Bayes' Rule


## Problem 5 - Murder Mystery Revised

## Problem 6 - Priors, Posteriors, Sensitivity, Specificity

## Problem 7 - AI-Assisted Programming
