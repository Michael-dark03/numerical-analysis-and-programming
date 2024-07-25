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

def lagrange_interpolation(x_points, y_points):
    """
    Perform Lagrange interpolation for the given data points.
    
    Parameters:
    x_points : array-like
        The x coordinates of the data points.
    y_points : array-like
        The y coordinates of the data points.
    
    Returns:
    function
        A function that evaluates the Lagrange polynomial at a given x value.
    """
    def polynomial(x):
        total = 0
        n = len(x_points)
        for i in range(n):
            term = y_points[i]
            for j in range(n):
                if i != j:
                    term *= (x - x_points[j]) / (x_points[i] - x_points[j])
            total += term
        return total
    
    return polynomial

# Define the x_points and y_points here
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

# Compute the Newton polynomial
newton_poly = newton_divided_difference(x_points, y_points)

# Compute the Lagrange polynomial
lagrange_poly = lagrange_interpolation(x_points, y_points)

# Define the x values for plotting the polynomials
x_values = np.linspace(min(x_points), max(x_points), 100)

# Compute the y values for the Lagrange polynomial
y_lagrange_values = [lagrange_poly(x) for x in x_values]

# Compute the y values for the Newton polynomial
y_newton_values = [newton_poly(x) for x in x_values]

# Plot both Lagrange and Newton polynomials
plt.plot(x_points, y_points, 'o', label='Data points')
plt.plot(x_values, y_lagrange_values, label='Lagrange polynomial')
plt.plot(x_values, y_newton_values, label='Newton polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange vs Newton Polynomial Interpolation')
plt.legend()
plt.grid(True)
plt.show()
