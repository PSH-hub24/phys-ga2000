import numpy as np
import scipy.special as special

# Define the parameters
n = 5  # Change this for different n values

# Define the function to integrate
def integrand(x):
    Hn = special.hermite(n)  # Get the nth Hermite polynomial
    return x**2 * (Hn(x))**2

# Get the Gauss-Hermite quadrature points and weights
points, weights = special.roots_hermite(50)  # Use 50 quadrature points for good accuracy

# Perform the integration using Gauss-Hermite quadrature
integral = np.sum(weights * integrand(points))

# Calculate the normalization factor
normalization = 1 / (2**n * special.factorial(n) * np.sqrt(np.pi))

# Final result
result = normalization * integral

# Print the result
print(f"The result of the integral for n={n} is:", np.sqrt(result))