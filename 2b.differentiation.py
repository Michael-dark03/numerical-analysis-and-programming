import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function
f = x**2 - x - 2

# Differentiate the function
f_prime = sp.diff(f, x)

print(f"The derivative of {f} is {f_prime}")
