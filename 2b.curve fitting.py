import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the model function
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Sample data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1, 4, 9, 16, 25])

# Fit the model to the data
params, covariance = curve_fit(model, x_data, y_data)

# Plot the data and the fit
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *params), label='Fitted curve', color='red')
plt.legend()
plt.show()

print(f"Fitted parameters: {params}")
