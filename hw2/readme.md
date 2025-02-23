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

Let's have X denote whether the market goes up with X=x meaning the market goes up and X=!x (or x bar) meaning the market went down. Given this, we have:

$$p(X=x) = 0.8$$
$$p(X=\bar{x}) = 0.2$$

When X=x, the market increases to 1.01 times its value.
When X=!x (or x bar), the market decreases to 0.9 times its value.

This gives us a g(X):

$$g(X=x) = 1.01$$
$$g(X=\bar{x}) = 0.9$$

Therefore, we can calculate the expected value of X as
$$E(X) = \sum_{n=1}^{N}p(x_{n})g(x_{n}) = (0.8 * 1.01) + (0.2*0.9) = 0.988$$

This is less than 1, meaning the market loses money, and so we wouldn't want to invest in it. 

We can calculate the lowest required probability that the market goes up in order to make money, given the increase and decrease amounts are fixed, by finding what value gives us an expected value of one and set that as our threshold the probability must be above (as there is essentially no point in investing even if your money stays the same):

$$E(X) = 1 = (y * 1.01) + ((1-y) * 0.9)$$

Solving this for y gives:

$$y = \frac{0.10}{0.11} = \frac{10}{11} = 0.\bar{90}$$

Therefore, for us to invest, we require the probability the market goes up to be greater than 10/11.

Of course this is only the expected trend as the number of market fluctuations (and so, time) goes to infinity. With a finite number of fluctuations, we can only use this as an approximation, and the market could temporarily trend in our favor or exactly the opposite.

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

=======
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
Let's have X denote whether a statement was true. 

Let's have X denote whether a statement was true with X=x meaning the statement was true and X=!x (or x bar) meaning the statement was false. Given this, we have:

$$p(X=x) = \frac{1}{3}$$
$$p(X=\bar{x}) = \frac{2}{3}$$

We can determine the situation has two possible cases:
1. The second statement is true, which means the first statement also was true
2. The second statement is false, meaning the first statement also was false

Therefore, we know that the status of the second statement is the same as the status of the first. 

We can expand our variables to let f denote the first statement was true and s denote the second statement was true.

Therefore, we want to find:

$$p(f | f == s)$$

where

$$p(f) = \frac{1}{3},$$

$$p(f == s) = p(f, s) + p(\bar{f}, \bar{s}) = (\frac{1}{3} * \frac{1}{3}) + (\frac{2}{3} * \frac{2}{3}) = \frac{5}{9}$$

We can then use Bayes' Rule:

$$p(f | f == s) = \frac{p(f==s | f) * p(f)}{p(f==s)}$$

We know that p(f == s | f) means that the first statement was true, so it is equivalent to p(s) which is 1/3.

So, 

$$p(f | f == s) = \frac{(\frac{1}{3}) * (\frac{1}{3})}{(\frac{5}{9})} = \frac{1}{5}$$

Therefore, the probability that the first statement was true in this particular situation is 1/5, or 0.2.

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

Let's have X denote whether someone has disease X, with X=x meaning they have the disease and X=!x (or x bar) meaning they don't have disease X. Additionally, let T denote if a test comes back positive, P denote if a test was a true positive and N denote whether a test was a true negative. Given this, we have:

$$p(X=x) = 0.01$$

$$p(P=p) = 0.95$$

$$p(N=n) = 0.90$$

We know that the result of the test was positive. This means we have two possible cases:

1. The person has disease X and the test is a true positive
2. The person does not have disease X and the test is a false positive

Therefore:

$$p(T=t) = p(X=x, P=p) + p(X=\bar{x}, N=\bar{n})$$

$$p(T=t) = (0.01 * 0.95) + (0.99 * 0.10) =  0.1085$$

This can then be combined with Bayes' theorum, giving us:

$$p(X=x | T=t) = \frac{p(T=t | X=x) * p(X=x)}{p(T=t)} = \frac{0.95 * 0.01}{0.1085} = 0.0876$$

where the decimal value has been rounded to the nearest ten-thousandth. This is the posterior probability of the test.

The Python program that produces the graphs can be found in problem6.py, with it displayed as a notebook in problem6.ipynb to showcase the flow of the code and easily have all plots up at once.

As seen in the graphs, 

1. As the prior increases, the posterior increases following $$1-e^{-x}$$
up to a final value of 1.0 when the prior is 1.0, as that means everyone has the disease.

2. As the sensitivity increases, the posterior increases linearly up to a maximum value of 0.1 when the sensitivity is 1.0. In this case, all people with the disease get positive tests, but there are still many false positives.

3. As the specificity increases, the posterior increases following an exponential growth, with a maximum value of 0.9 when specificity is 1.0. In this case, all people without the disease get negative tests, but there are still some false negatives.

## Problem 7 - AI-Assisted Programming

The `ai_assisted_programming.py` file contains the code for this problem.

An interesting note to make about the ChatGPT version of the function is that, despite
specifying that the third parameter should be `Sigma`, it still interpreted it as the
covariance matrix, `Cov`.

ChatGPT's implementation of the multivariate normal density function closely matches
the output of SciPy's version. The only difference between the two is for a full
covariance Gaussian, and even that is a slight difference after 15 decimal places.
