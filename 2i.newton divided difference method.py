import numpy as np
import matplotlib.pyplot as plt

def newton_divided_difference(x_points, y_points):
    """
    Perform Newton's Divided Difference interpolation for the given data points.
    
    Parameters:
    x_points : array-like
        The x coordinates of the data points.
    y_points : array-like
        The y coordinates of the data points.
    
    Returns:
    function
        A function that evaluates the interpolating polynomial at a given x value.
    """
    n = len(x_points)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y_points
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (x_points[i+j] - x_points[i])
    
    def polynomial(x):
        total = divided_diff[0, 0]
        term = 1.0
        for i in range(1, n):
            term *= (x - x_points[i-1])
            total += divided_diff[0, i] * term
        return total
    
    return polynomial

# Define the x_points and y_points here
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

# Compute the Newton polynomial
newton_poly = newton_divided_difference(x_points, y_points)

# Define the y values for plotting the polynomial
x_values = np.linspace(min(x_points), max(x_points), 100)
y_newton_values = [newton_poly(x) for x in x_values]

# Plot the data points and the interpolating polynomial
plt.plot(x_points, y_points, 'o', label='Data points')
plt.plot(x_values, y_newton_values, label='Newton polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Polynomial Interpolation')
plt.legend()
plt.grid(True)
plt.show()
