import numpy as np
import scipy


# ChatGPT response
def multivariate_normal_density(x, mu, Sigma):
    """
    Calculate the multivariate normal density.

    Parameters:
    x (numpy.ndarray): A vector of observed values (d,).
    mu (numpy.ndarray): The mean vector (d,).
    Sigma (numpy.ndarray): The covariance matrix (d, d).

    Returns:
    float: The multivariate normal density evaluated at x.
    """
    # Ensure that x, mu, and Sigma are numpy arrays
    x = np.asarray(x)
    mu = np.asarray(mu)
    Sigma = np.asarray(Sigma)

    # Dimensionality
    d = len(mu)

    # Compute the normalization factor
    norm_factor = (2 * np.pi) ** (-d / 2)
    norm_factor *= np.linalg.det(Sigma) ** (-0.5)

    # Compute the quadratic form (x - mu)^T Sigma^-1 (x - mu)
    diff = x - mu
    inv_Sigma = np.linalg.inv(Sigma)
    quadratic_form = np.dot(diff.T, np.dot(inv_Sigma, diff))

    # Compute the density value
    density = norm_factor * np.exp(-0.5 * quadratic_form)

    return density


# data vector
x = np.array([1, 1])
# mean vector
mu = np.array([0, 0])

# covariance matrix
cov = np.array([[1, 0], [0, 1]])
print("Spherical Gaussian:")
print(f"ChatGPT: {multivariate_normal_density(x, mu, cov)}")
print(f"SciPy:   {scipy.stats.multivariate_normal.pdf(x, mean=mu, cov=cov)}")
print()

cov = np.array([[1, 0], [0, 2]])
print("Diagonal Gaussian:")
print(f"ChatGPT: {multivariate_normal_density(x, mu, cov)}")
print(f"SciPy:   {scipy.stats.multivariate_normal.pdf(x, mean=mu, cov=cov)}")
print()

cov = np.array([[1, 1.25], [1.25, 2]])
print("Full-Covariance Gaussian:")
print(f"ChatGPT: {multivariate_normal_density(x, mu, cov)}")
print(f"SciPy:   {scipy.stats.multivariate_normal.pdf(x, mean=mu, cov=cov)}")
print()
