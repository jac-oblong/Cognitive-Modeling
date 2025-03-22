# Homework Assignment 3

## Problem 1 - True-False

### 1. The solution of the stochastic integral $\int_0^T \mu dW_t$ is $\mu(W_T - W_0)$ and is a random variable itself.

### 2. The variance of a Wiener process with scale coefficient $\alpha = 1$ at time $t$ is $t^2$.

### 3. The standard Drift-Diffusion Model (DDM) assumes that evidence about a dominant alternative accumulates in discrete chunks over time.

### 4. The first passage time distribution has a closed-form probability density function, but its density can still be evaluated only numerically.

### 5. The Euler-Maruyama method can only be used to simulate linear stochastic systems.

### 6. For any Bayesian analysis, the prior will always have a smaller variance than the posterior.

### 7. In addition to good statistical practice, experimental validation of cognitive models is crucial for ensuring construct validity.

### 8. Markov chain Monte Carlo (MCMC) methods approximate a complex posterior distribution through a simpler, yet analytically tractable, distribution.

### 9. For most Bayesian problems, the more data we collect, the less influence does the prior exert on the resulting inferences.

### 10. The effective sample size (ESS) estimated from MCMC samplers differs from the total number of samples because the samples are not independent (i.e., exhibit non-zero autocorrelation).

## Problem 2 - Diffusion Model Explorations

## Problem 3 - Prior and Posterior Variance

$$Var[\theta] = E[Var[\theta | y]] + Var[E[\theta | y]]$$

First, we know that 

$$Var[X] = E[X^2] - E[X]^2$$
$$Var[X|Y] = E[X^2 | Y] - E[X | Y]^2$$
$$E[X + Y] = E[X] + E[Y]$$
$$E[X] = E[E[X | Y]]$$

If we expand the right-hand side

$$Var[\theta] = E[Var[\theta | y]] + Var[E[\theta | y]]$$
$$Var[\theta] = E[E[\theta^2 | y] - E[\theta | y]^2] + Var[E[\theta | y]]$$
$$Var[\theta] = E[E[\theta^2 | y]] - E[E[\theta | y]^2] + Var[E[\theta | y]]$$
$$Var[\theta] = E[\theta^2] - E[E[\theta | y]^2] + Var[E[\theta | y]]$$

Focusing on $E[\theta^2]$, if we rearrange the equation for $Var[X]$ we have that
$E[X^2] = Var[X] + E[X]^2$, so

$$Var[\theta] = Var[\theta] + E[\theta]^2 - E[E[\theta | y]^2] + Var[E[\theta | y]]$$

Now focusing on $E[E[\theta | y]^2]$, if we rearrange the equation for $Var[X|Y]$ we have that
$E[E[X | Y]^2] = E[E[X^2 | Y] - Var[X | Y]]$, so

$$Var[\theta] = Var[\theta] + E[\theta]^2 - E[E[\theta^2 | y] - Var[\theta | y]] + Var[E[\theta | y]]$$
$$Var[\theta] = Var[\theta] + E[\theta]^2 - E[E[\theta^2 | y]] - E[Var[\theta | y]] + Var[E[\theta | y]]$$
$$Var[\theta] = Var[\theta] + E[\theta]^2 - E[\theta^2] - E[Var[\theta | y]] + Var[E[\theta | y]]$$
$$Var[\theta] = Var[\theta] - E[Var[\theta | y]] + Var[E[\theta | y]]$$

## Problem 4 - Normal-Normal Model

## Problem 5 - Simple Bayesian Regression with Stan

## Problem 6 - Estimating the Drift-Diffusion Model
