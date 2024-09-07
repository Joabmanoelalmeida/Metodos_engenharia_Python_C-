import numpy as np

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

# Método de Newton-Raphson
def newton_raphson(initial_guess, tol=1e-8, max_iter=100):
    x = np.array(initial_guess, dtype=float)
    
    for i in range(max_iter):
        fx = F(x)
        Jx = J(x)
        
        # Verificar se a função está próxima de zero
        if np.linalg.norm(fx, ord=2) < tol:
            return x, i
        
        # Resolver o sistema linear J(x) * delta = -F(x)
        delta = np.linalg.solve(Jx, -fx)
        
        # Atualizar a solução
        x = x + delta
        
        # Verificar a convergência
        if np.linalg.norm(delta, ord=2) < tol:
            return x, i
    
    raise Exception("Método de Newton-Raphson não convergiu após o número máximo de iterações")

# Definir a estimativa inicial
initial_guess = [0.5, 0.5, 0.5]

# Resolver o sistema
solution, num_iterations = newton_raphson(initial_guess)

# Exibir resultados
print(f'Solução encontrada: x1 = {solution[0]:.6f}, x2 = {solution[1]:.6f}, x3 = {solution[2]:.6f}')
print(f'Número de iterações: {num_iterations}')