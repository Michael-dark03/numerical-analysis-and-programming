import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function and its derivative
f_expr = x**3 - 0.165*x**2 + 3.993e-4
f_prime_expr = sp.diff(f_expr, x)

# Convert sympy expressions to numerical functions
f = sp.lambdify(x, f_expr, 'numpy')
f_prime = sp.lambdify(x, f_prime_expr, 'numpy')

# Newton's method function
def newtons_method(f, f_prime, x0, iterations):
    results = []
    for i in range(iterations):
        x1 = x0 - f(x0) / f_prime(x0)
        error = abs((x1 - x0) / x1) * 100 if x1 != 0 else 0
        results.append((i+1, x1, error))
        x0 = x1
    return results

# Initial guess
x0 = 0.05  # Initial guess should be reasonably close to the actual root

# Conduct three iterations
iterations = 3
results = newtons_method(f, f_prime, x0, iterations)

# Print results
print(f"{'Iteration':<10} {'x':<20} {'Absolute Relative Approximate Error (%)':<40}")
for i, x1, error in results:
    print(f"{i:<10} {x1:<20} {error:<40}")

# Plotting the function and the iterations for visualization
import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(0, 0.1, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
for i, x1, error in results:
    plt.plot(x1, f(x1), 'ro')
    plt.text(x1, f(x1), f'  Iter {i}', verticalalignment='bottom')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title("Newton's Method Iterations")
plt.show()
