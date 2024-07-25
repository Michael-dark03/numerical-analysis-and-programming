import numpy as np
import matplotlib.pyplot as plt

# Define the function to be integrated
def f(x):
    return x**2

# Implement the trapezoidal rule
def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the trapezoidal rule with n intervals.
    
    Parameters:
    f : function
        The function to integrate.
    a : float
        The start of the interval.
    b : float
        The end of the interval.
    n : int
        The number of intervals.
    
    Returns:
    float
        The approximate integral of f from a to b.
    """
    x = np.linspace(a, b, n+1)  # n+1 points make n intervals
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# Define the interval and number of intervals
a = 0
b = 1
n = 10  # Number of intervals

# Calculate the approximate integral
approx_integral = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral of f(x) from {a} to {b} using the trapezoidal rule with {n} intervals is: {approx_integral}")

# Plot the function and the trapezoids
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, label='f(x) = x^2')
plt.fill_between(x, y, alpha=0.2)

x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)

for i in range(n):
    plt.plot([x_trap[i], x_trap[i]], [0, y_trap[i]], 'r--')
    plt.plot([x_trap[i+1], x_trap[i+1]], [0, y_trap[i+1]], 'r--')
    plt.plot([x_trap[i], x_trap[i+1]], [y_trap[i], y_trap[i+1]], 'r--')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Trapezoidal Rule for Numerical Integration')
plt.show()
