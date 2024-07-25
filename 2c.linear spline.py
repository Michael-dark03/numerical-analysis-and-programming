import numpy as np
import matplotlib.pyplot as plt

# Given data points
x_points = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_points = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Linear interpolation function
def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

# Target x value for interpolation
x_target = 4.0

# Find the interval [x0, x1] that contains x_target
for i in range(len(x_points) - 1):
    if x_points[i] <= x_target <= x_points[i+1]:
        x0, y0 = x_points[i], y_points[i]
        x1, y1 = x_points[i+1], y_points[i+1]
        break

# Perform linear interpolation
y_target = linear_interpolate(x0, y0, x1, y1, x_target)

print(f"The value of y at x = {x_target} is {y_target}")

# Plotting the data points and the interpolation result
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.plot(x_points, y_points, label='Spline Path', color='blue')
plt.scatter([x_target], [y_target], color='green', label=f'Interpolated y at x={x_target}')
plt.xlabel('X (in)')
plt.ylabel('Y (in)')
plt.legend()
plt.title('Linear Spline Interpolation')
plt.show()
