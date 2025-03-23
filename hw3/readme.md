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

$$
\begin{align}
    \nonumber Var[X] &= E[X^2] - E[X]^2 \\
    \nonumber Var[X|Y] &= E[X^2 | Y] - E[X | Y]^2 \\
    \nonumber E[X + Y] &= E[X] + E[Y] \\
    \nonumber E[X] &= E[E[X | Y]] \\
\end{align}
$$

Let us start with the definition of $Var[X]$

$$Var[\theta] = E[\theta^2] - E[\theta]^2$$

We know that $E[X^2] = E[E[X^2 | Y]]$, so

$$Var[\theta] = E[E[\theta^2 | y]] - E[\theta]^2$$

From the equation for $Var[X | Y]$, we have that $E[X^2 | Y] = Var[X | Y] + E[X | Y]^2$, so

$$Var[\theta] = E[Var[\theta | y] + E[\theta | y]^2] - E[\theta]^2$$

From the equation for $E[X + Y]$, we have

$$Var[\theta] = E[Var[\theta | y]] + E[E[\theta | y]^2]] - E[\theta]^2$$

Again, $E[X^2] = E[E[X^2 | Y]]$, so

$$Var[\theta] = E[Var[\theta | y]] + E[E[\theta | y]^2]] - E[E[\theta | y]]^2$$

Finally, using the equation for $Var[X]$, we have

$$Var[\theta] = E[Var[\theta | y]] + Var[E[\theta | y]]$$

## Problem 4 - Normal-Normal Model

## Problem 5 - Simple Bayesian Regression with Stan

## Problem 6 - Estimating the Drift-Diffusion Model
