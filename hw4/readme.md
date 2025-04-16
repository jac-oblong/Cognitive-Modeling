# Homework Assignment 4

## Problem 1 - True-False

### Direct $K$-fold cross-validation requires $K$ model re-fits, which may be computationally demanding, especially when inverse inference is costly

TRUE. This is still less demanding, however, than something like Leave-one-out cross-validation.

### Bayes factors (BFs) are *relative measures*, that is, they cannot differentiate between "equally good" and "equally bad" models.

TRUE. Bayes factors simply compare the marginal likelihoods of models, they don't offer any further insight to general model performance.

### Marginal likelihoods and, by extension, Bayes factors (BFs) cannot be used to compare models with different likelihoods.

FALSE. Marginal likelihoods just look at the probability of obtaining the data given the model, and so they, and by extension, Bayes factors, can be used to compare all sorts of models with regard to how accurately they represent the data.

### Both the Binomial and the Dirichlet distribution can be formulated as special cases of the Multinomial distribution.

FALSE. The Binomial is a special case of the Multinomial distribution, but the Dirichlet distribution is instead the multivariate extension of the Beta distribution.

### Bayesian leave-one-out cross-validation (LOO-CV) relies on the posterior predictive distribution of left-out data points.

TRUE. For each left out data point, the posterior predictive distribution is used.

### The Akaike Information Criterion (AIC) penalizes model complexity indirectly through the variance of a model's marginal likelihood.

FALSE. Bayes factors do this in order to measure generative performance. AIC penalizes model complexity directly by applying a penalty for the number of parameters in the model (with more parameters giving a higher penalty and more paramters being one simple way to measure model complexity).

### The log-predictive density (LPD) is a relative metric of model complexity.

FALSE. LPD is a reletive metric of predictive performance. It doesn't depend on complexity directly, rather, it depends on the model's predictive performance.

### The LPD can be approximated by evaluating the likelihood of each posterior draw (e.g., as provided by an MCMC sampler) and taking the average of all resulting likelihood values.

TRUE. A Monte Carlo estimate can be used to approximate the LPD as described in the statement.

### Bayes factors do not depend on the prior odds, that is, the ratio of prior model probabilities $p(M_1)/p(M_2)$.

TRUE. Bayes factors compare the marginal likelihoods of the models. They are, however, proportional to the posterior odds with the scale factor being the prior odds:

$\frac{p(y|M_1)}{p(y|M_2)} * \frac{p(M_1)}{p(M_2)} = \frac{p(M_1|y)}{p(M_2|y)}$

### You should always prefer information criteria to cross-validation in terms of estimating predictive performance.

FALSE. Both information criteria and cross-validation methods are approximations used to estimate predictive performance. Therefore, each method may be a better or worse approximation given specific circumstances.

## Problem 2 - Simple Multinomial Processing Trees (MPTs)

The answer to this problem can be found in [problem2.ipynb](./problem2.ipynb).

## Problem 3 - Multiple Regression

The answer to this problem can be found in [problem3.ipynb](./problem3.ipynb).

## Problem 4 - Predictive Distribution

The answer to this problem can be found in [problem4.ipynb](./problem4.ipynb).

## Problem 5 - Reflection

One take-away is how important statistics is in the modern age. So many different
disciplines utilize predictive models whether they realize it or not. Some examples
include medicine, weather, stock markets, and even traffic patterns. Not all of
them utilize Bayesian models, but they do utilize previous observations to predict
new data, which is fundamentally a statistical problem.

Another take-away is the importance of validating the results of models. This is
especially important because of how many different ways there are to validate them
and also because of how complex they are.

Continuing off of that, another key takeaway is the difference between generative and
predictive performance. Models are often very specialized (or, at least, it is much harder
to make a high-performing general model), and so when comparing models for selection,
it's important to know what type of behavior you are looking to get from it.
Thus, when evaluating model performance, first decide whether it is more useful to test
generative performance, predictive performance, or both. Do you want the model to reproduce
the data or predict new data? From there, you can further decide how best to evaluate that type of performance.

Finally, going back to something from the start of the semester that would be useful even
if we never touch statistical modeling again is the idea of the replication crisis in psychology
and the related fields. Especially given the state of the news today 
(at least in America, not sure what is it like elsewhere) where getting clicks and making money
is much more important than providing informative, non-biased news,
it is very common to see all sorts of headlines that are either an exaggeration of the truth or not even slightly true.
This would be especially present if there is some sort of "scientific/research study"
that they are getting their source from, but made no effort to check the validity of the study.
Add into this AI-generated information and the replication crisis and it can be very difficult to tell what is true,
solid information or not. Therefore, we must be cognizant of this issue when gathering and spreading information on and from the internet.

## Problem 6 - Project Pre-Study

We are planning on modeling the reaction of cone cells in the eye to light stimuli. When hit by a light wave within their range, cone cells will activate, and the brain interprets these signals as sight. Certain cells respond to certain ranges in frequency, with three main types - S (short wavelengths - "blue"), M (medium wavelengths - "green"), and L (long wavelengths - "red"). In order to perceive color, the brain compares the activation levels of the cell types and perceives the multitude of responses as the color. A great example to visualize this is purple. There is no such thing as "purple" light. Instead, enough cone cells receive a blue frequency and enough receive a red frequency, with a lack of green frequencies, and together, this is perceived as purple. We intend to model this cognitive process, where, given activation levels of cone cells, the model will predict which light frequency was present. 

For this problem, the data will be the activation levels of cone cells, and the parameters will be the frequency. We will be utilizing a neural network to do the modeling. The input to the network (i.e. the data representation) will be a vector with the dimensionality of the number of cone cells, with each value being a 0 (for inactive) or a 1 (for activated cell). For the parameter we will do a classification problem. A selection of frequency ranges (or colors) will be chosen as the categories. We will treat this very similarly to the clothing type classification example from class.

For the sake of the project, we will be generating the data using a simulator. We will research the average responses for each cell type and use these values to generate random activations for various frequencies. All together, we will pick a random frequency. This frequency will be given a color label based on which range it is in. The frequency will be passed to the simulator to determine a valid cone cell response. This will be done for many data points. Training, testing, and validation sets will be generated.

There is a lot of scientific research into the activation of cone cells. The results of these studies vary greatly person to person, with some people having lower count of cone cells and cone cell types (leading to colorblindness) and others even having a fourth type of cone cell, giving them a condition called tetrachromacy where they can perceive a richer range of colors. This reseach often involves analyzing the data in the other dimension: supplying a specific frequency to the eyes and measuring cone cell activations to find their activation functions. Instead, we are finding these activation functions implicitly through training the network, then using the network to determine the input color given the cone cells activations. 

We will ensure computational faithfulness and criticize the model through the analysis of its training. Due to the data being simulated, we can create as much as we need to get reasonable results. This, however, does mean that we need to ensure the proper behavior of the simulator. This will be done by comparing the generated activation response data to the expected cone cell activations to ensure it is generating valid data. Additionally, we may investigate the performance of the model given different configurations, similarly to adding noise to the clothing type detection network in class. However, noise doesn't make as much sense in this case. Instead, we can look into adding more/less cone cell types to see if we can simulate colorblindness/tetrachromacy, or other, similar modifications to the model.
