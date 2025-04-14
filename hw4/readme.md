# Homework Assignment 4

## Problem 1 - True-False

### Direct $K$-fold cross-validation requires $K$ model re-fits, which may be computationally demanding, especially when inverse inference is costly

### Bayes factors (BFs) are *relative measures*, that is, they cannot differentiate between "equally good" and "equally bad" models.

### Marginal likelihoods and, by extension, Bayes factors (BFs) cannot be used to compare models with different likelihoods.

### Both the Binomial and the Dirichlet distribution can be formulated as special cases of the Multinomial distribution.

### Bayesian leav-one-out cross-validation (LOO-CV) relies on the posterior predictive distribution of left-out data points.

### The Akaike Information Criterion (AIC) penalizes model complexity indirectly through the variance of a model's marginal likelihood.

### The log-predictive density (LPD) is a relative metric of model complexity.

### The LPD can be approximated by evaluating the likelihood of each posterior draw (e.g., as provided by an MCMC sampler) and taking the average of all resulting likelihood values.

### Bayes factors do not depend on the prior odds, that is, the ratio of prior model probabilities $p(M_1)/p(M_2)$.

## Problem 2 - Simple Multinomial Processing Trees (MPTs)

## Problem 3 - Multiple Regression

## Problem 4 - Predictive Distribution

## Problem 5 - Reflection

## Problem 6 - Project Pre-Study

We are planning on modeling the reaction of cone cells in the eye to light stimuli. When hit by a light wave within their range, cone cells will activate, and the brain interprets these signals as sight. Certain cells respond to certain ranges in frequency, and so in order to perceive the "true color" (as much as is possible, as color is just an abstract thing), the brain compares the levels of the cell types and perceives a multitude of responses as a color. A great example to visualize this is purple. There is no such thing as "purple" light. Instead, enough cone cells receive a blue frequency and enough receive a red frequency, with a lack of green frequencies, and together, this is perceived as purple. We intend to model this cognitive process, where, given activation levels of cone cells, the model will predict which light frequency was present. 

We have light frequency, cone activations, and perceived colors to work with. 
