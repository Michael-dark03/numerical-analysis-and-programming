# Full script to run both methods and compare the results

import numpy as np

def power_iteration(A, num_simulations: int):
    b_k = np.random.rand(A.shape[1])
    for _ in range(num_simulations):
        b_k1 = np.dot(A, b_k)
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
    
    eigenvalue = np.dot(A @ b_k, b_k) / np.dot(b_k, b_k)
    eigenvector = b_k
    return eigenvalue, eigenvector

def qr_algorithm(A, num_simulations: int):
    A_k = A.copy()
    n = A.shape[0]
    Q_total = np.eye(n)
    for _ in range(num_simulations):
        Q, R = np.linalg.qr(A_k)
        A_k = R @ Q
        Q_total = Q_total @ Q
    
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_total
    return eigenvalues, eigenvectors

# Define the matrix A
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

# Number of iterations
num_simulations = 1000

# Power Iteration Method
eigenvalue, eigenvector = power_iteration(A, num_simulations)
print("Power Iteration Method:")
print("Eigenvalue:", eigenvalue)
print("Eigenvector:", eigenvector)

# QR Algorithm
eigenvalues, eigenvectors = qr_algorithm(A, num_simulations)
print("QR Algorithm:")
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
