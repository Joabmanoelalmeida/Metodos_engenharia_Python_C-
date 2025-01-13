import numpy as np

# Definir a matriz A
A = np.array([[5, 1, np.sqrt(2)],
              [1, 5, np.sqrt(2)],
              [np.sqrt(2), np.sqrt(2), 6]])

# autovalores e autovetores
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Autovalores:")
print(eigenvalues)
print("Autovetores (colunas correspondem aos autovalores):")
print(eigenvectors)

# Verificar se os autovetores são ortonormais, matriz identidade esperada
identity_check = np.dot(eigenvectors.T, eigenvectors)
print("Verificação de ortogonalidade (Matriz identidade esperada):")
print(identity_check)

# Confirmar ortogonalidade com tolerância
tolerance = 0.5
identity_matrix = np.eye(len(A))  # Matriz identidade do mesmo tamanho
if np.allclose(identity_check, identity_matrix, atol=tolerance):
    print("Sim, os autovetores são ortogonais e ortonormais.")
else:
    print("Não, os autovetores não são ortogonais ou ortonormais.")