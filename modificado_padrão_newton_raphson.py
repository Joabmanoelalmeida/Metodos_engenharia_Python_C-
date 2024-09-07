import numpy as np
import matplotlib.pyplot as plt

# Definir a função F(x) para o sistema de equações não lineares
def F(x):
    return np.array([
        x[0]**2 + x[1]**2 + x[2]**2 - 1,
        x[0]**2 - x[1] - x[2] + 0.5,
        x[1]**2 + x[2] - 1
    ])

# Definir a Jacobiana J(x)
def J(x):
    return np.array([
        [2*x[0], 2*x[1], 2*x[2]],
        [2*x[0], -1, -1],
        [0, 2*x[1], 1]
    ])

# Método de Newton-Raphson padrão com verificação de singularidade
def newton_raphson_standard(initial_guess, tol=1e-8, max_iter=100):
    x = np.array(initial_guess, dtype=float)
    history = [x.copy()]
    
    for i in range(max_iter):
        fx = F(x)
        Jx = J(x)
        
        # Tentar resolver o sistema linear J(x) * delta = -F(x)
        try:
            delta = np.linalg.solve(Jx, -fx)
        except np.linalg.LinAlgError:
            print("Matriz Jacobiana singular. Tentando regularização.")
            # Regularização: Adiciona um pequeno valor à diagonal
            Jx += np.eye(Jx.shape[0]) * 1e-6
            delta = np.linalg.solve(Jx, -fx)
        
        # Atualizar a solução
        x = x + delta
        history.append(x.copy())
        
        # Verificar a convergência
        if np.linalg.norm(fx, ord=2) < tol:
            return x, history, i
    
    raise Exception("Método de Newton-Raphson não convergiu após o número máximo de iterações")

# Método de Newton-Raphson modificado (com fator de escala)
def newton_raphson_modified(initial_guess, tol=1e-8, max_iter=100, scale_factor=0.5):
    x = np.array(initial_guess, dtype=float)
    history = [x.copy()]
    
    for i in range(max_iter):
        fx = F(x)
        Jx = J(x)
        
        # Tentar resolver o sistema linear J(x) * delta = -F(x)
        try:
            delta = np.linalg.solve(Jx, -fx)
        except np.linalg.LinAlgError:
            print("Matriz Jacobiana singular. Tentando regularização.")
            # Regularização: Adiciona um pequeno valor à diagonal
            Jx += np.eye(Jx.shape[0]) * 1e-6
            delta = np.linalg.solve(Jx, -fx)
        
        # Atualizar a solução com fator de escala
        x = x + scale_factor * delta
        history.append(x.copy())
        
        # Verificar a convergência
        if np.linalg.norm(fx, ord=2) < tol:
            return x, history, i
    
    raise Exception("Método de Newton-Raphson não convergiu após o número máximo de iterações")

# Definir a estimativa inicial
initial_guess = [0.5, 0.5, 0.5]

# Resolver o sistema com o método padrão
solution_standard, history_standard, num_iterations_standard = newton_raphson_standard(initial_guess)

# Resolver o sistema com o método modificado
solution_modified, history_modified, num_iterations_modified = newton_raphson_modified(initial_guess)

# Plotar a convergência dos métodos
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Método padrão
history_standard = np.array(history_standard)
axs[0].plot(np.linalg.norm(F(history_standard), axis=1), marker='o')
axs[0].set_title('Método de Newton-Raphson Padrão')
axs[0].set_xlabel('Iteração')
axs[0].set_ylabel('Norma de F(x)')
axs[0].set_yscale('log')

# Método modificado
history_modified = np.array(history_modified)
axs[1].plot(np.linalg.norm(F(history_modified), axis=1), marker='o')
axs[1].set_title('Método de Newton-Raphson Modificado')
axs[1].set_xlabel('Iteração')
axs[1].set_ylabel('Norma de F(x)')
axs[1].set_yscale('log')

plt.tight_layout()
plt.show()

# Exibir resultados
print(f'Solução padrão encontrada: x1 = {solution_standard[0]:.6f}, x2 = {solution_standard[1]:.6f}, x3 = {solution_standard[2]:.6f}')
print(f'Número de iterações (padrão): {num_iterations_standard}')
print(f'Solução modificada encontrada: x1 = {solution_modified[0]:.6f}, x2 = {solution_modified[1]:.6f}, x3 = {solution_modified[2]:.6f}')
print(f'Número de iterações (modificado): {num_iterations_modified}')