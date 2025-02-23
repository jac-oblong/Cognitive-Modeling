# Homework Assignment 2

## Problem 1 - True-False

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
