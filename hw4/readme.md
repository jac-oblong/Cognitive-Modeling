# Homework Assignment 4

## Problem 1 - True-False

### Direct $K$-fold cross-validation requires $K$ model re-fits, which may be computationally demanding, especially when inverse inference is costly

TRUE

### Bayes factors (BFs) are *relative measures*, that is, they cannot differentiate between "equally good" and "equally bad" models.

TRUE

### Marginal likelihoods and, by extension, Bayes factors (BFs) cannot be used to compare models with different likelihoods.

FALSE.

### Both the Binomial and the Dirichlet distribution can be formulated as special cases of the Multinomial distribution.

FALSE. The Binomial is a special case of the Multinomial distribution, but the Dirichlet distribution is instead the multivariate extension of the Beta distribution.

### Bayesian leave-one-out cross-validation (LOO-CV) relies on the posterior predictive distribution of left-out data points.

### The Akaike Information Criterion (AIC) penalizes model complexity indirectly through the variance of a model's marginal likelihood.

### The log-predictive density (LPD) is a relative metric of model complexity.

### The LPD can be approximated by evaluating the likelihood of each posterior draw (e.g., as provided by an MCMC sampler) and taking the average of all resulting likelihood values.

### Bayes factors do not depend on the prior odds, that is, the ratio of prior model probabilities $p(M_1)/p(M_2)$.

## Problem 2 - Simple Multinomial Processing Trees (MPTs)

## Problem 3 - Multiple Regression

## Problem 4 - Predictive Distribution

## Problem 5 - Reflection

## Problem 6 - Project Pre-Study

We are planning on modeling the reaction of cone cells in the eye to light stimuli. When hit by a light wave within their range, cone cells will activate, and the brain interprets these signals as sight. Certain cells respond to certain ranges in frequency, with three main types - S (short wavelengths - "blue"), M (medium wavelengths - "green"), and L (long wavelengths - "red"). In order to perceive color, the brain compares the activation levels of the cell types and perceives the multitude of responses as the color. A great example to visualize this is purple. There is no such thing as "purple" light. Instead, enough cone cells receive a blue frequency and enough receive a red frequency, with a lack of green frequencies, and together, this is perceived as purple. We intend to model this cognitive process, where, given activation levels of cone cells, the model will predict which light frequency was present. 

For this problem, the data will be the activation levels of cone cells, and the parameters will be the frequency. We will be utilizing a neural network to do the modeling. The input to the network (i.e. the data representation) will be a vector with the dimensionality of the number of cone cells, with each value being a 0 (for inactive) or a 1 (for activated cell). For the parameter we will do a classification problem. A selection of frequency ranges (or colors) will be chosen as the categories. We will treat this very similarly to the clothing type classification example from class.

For the sake of the project, we will be generating the data using a simulator. We will research the average responses for each cell type and use these values to generate random activations for various frequencies. All together, we will pick a random frequency. This frequency will be given a color label based on which range it is in. The frequency will be passed to the simulator to determine a valid cone cell response. This will be done for many data points. Training, testing, and validation sets will be generated.

There is a lot of scientific research into the activation of cone cells. The results of these studies vary greatly person to person, with some people having lower count of cone cells and cone cell types (leading to colorblindness) and others even having a fourth type of cone cell, giving them a condition called tetrachromacy where they can perceive a richer range of colors. This reseach often involves analyzing the data in the other dimension: supplying a specific frequency to the eyes and measuring cone cell activations to find their activation functions. Instead, we are finding these activation functions implicitly through training the network, then using the network to determine the input color given the cone cells activations. 

We will ensure computational faithfulness and criticize the model through the analysis of its training. Due to the data being simulated, we can create as much as we need to get reasonable results. This, however, does mean that we need to ensure the proper behavior of the simulator. This will be done by comparing the generated activation response data to the expected cone cell activations to ensure it is generating valid data. Additionally, we may investigate the performance of the model given different configurations, similarly to adding noise to the clothing type detection network in class. However, noise doesn't make as much sense in this case. Instead, we can look into adding more/less cone cell types to see if we can simulate colorblindness/tetrachromacy, or other, similar modifications to the model.
