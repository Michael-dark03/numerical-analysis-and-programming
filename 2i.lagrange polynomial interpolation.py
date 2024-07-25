import numpy as np
import matplotlib.pyplot as plt

# Define the data points
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

def lagrange_interpolation(x_points, y_points, x):
    """
    Perform Lagrange interpolation for the given data points.
    
    Parameters:
    x_points : array-like
        The x coordinates of the data points.
    y_points : array-like
        The y coordinates of the data points.
    x : float
        The x value at which to evaluate the interpolating polynomial.
    
    Returns:
    float
        The interpolated value at x.
    """
    n = len(x_points)
    total = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        total += term
    return total

# Define the x values for plotting the polynomial
x_values = np.linspace(1, 4, 100)
y_values = [lagrange_interpolation(x_points, y_points, x) for x in x_values]

# Plot the data points and the interpolating polynomial
plt.plot(x_points, y_points, 'o', label='Data points')
plt.plot(x_values, y_values, label='Lagrange polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial Interpolation')
plt.legend()
plt.grid(True)
plt.show()
