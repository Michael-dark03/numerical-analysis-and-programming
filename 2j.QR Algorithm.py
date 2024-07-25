import numpy as np

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

# Calculate eigenvalues and eigenvectors using QR algorithm
eigenvalues, eigenvectors = qr_algorithm(A, num_simulations)
print("QR Algorithm:")
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
