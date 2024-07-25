import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Plot the data and the fit
plt.scatter(x, y, label='Data')
plt.plot(x, slope * x + intercept, label='Fitted line', color='red')
plt.legend()
plt.show()

print(f"Slope: {slope}, Intercept: {intercept}")
