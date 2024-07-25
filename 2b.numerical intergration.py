import scipy.integrate as spi
import numpy as np

# Define the function
def f(x):
    return x**2 - x - 2

# Integrate the function from 1 to 3
integral, error = spi.quad(f, 1, 3)

print(f"The integral of the function from 1 to 3 is {integral} with an error of {error}")
