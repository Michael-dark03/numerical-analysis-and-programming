import math

# Define the function for which we want to find the root
def func(x):
    return x * x - x - 2

def regula(a, b, iterations, tol):
    fa = func(a)
    fb = func(b)
    
    if fa * fb >= 0:
        print("The function must have different signs at the endpoints a and b.")
        return -1

    for i in range(iterations):
        x = (a * fb - b * fa) / (fb - fa)
        fx = func(x)
        print(f"Iteration {i + 1}: x = {x}, f(x) = {fx}")
        if math.fabs(fx) < tol:
            return x
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    return -1  # Return -1 if no root is found within the specified number of iterations

def main():
    a = 1  # Start of the interval
    b = 3  # End of the interval
    iterations = 3  # Number of iterations
    tol = 1e-6  # Tolerance for the root

    root = regula(a, b, iterations, tol)
    if root != -1:
        print(f"Root found: {root}")
    else:
        print("No root found within the specified number of iterations.")

if __name__ == "__main__":
    main()

