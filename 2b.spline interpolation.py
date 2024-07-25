import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Perform spline interpolation
spline = splrep(x, y)
x_new = np.linspace(1, 5, 100)
y_new = splev(x_new, spline)

# Plot the data and the spline interpolation
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, label='Spline interpolation', color='red')
plt.legend()
plt.show()
