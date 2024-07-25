import numpy as np

def gradient_descent(grad_f, initial_guess, learning_rate, num_iterations):
    x, y = initial_guess
    for _ in range(num_iterations):
        grad_x, grad_y = grad_f(x, y)
        x -= learning_rate * grad_x
        y -= learning_rate * grad_y
    return x, y

def grad_f(x, y):
    df_dx = 2*x - y + 1
    df_dy = 2*y - x - 1
    return np.array([df_dx, df_dy])

# Initial guess
initial_guess = (0, 0)
# Learning rate
learning_rate = 0.1
# Number of iterations
num_iterations = 100

# Perform gradient descent
min_x, min_y = gradient_descent(grad_f, initial_guess, learning_rate, num_iterations)
print(f"Minimum value found at x = {min_x}, y = {min_y}")
