def newton_raphson(f, f_prime, x0, tol=1e-7, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raízes de funções.
    
    :param f: Função para a qual se deseja encontrar a raiz.
    :param f_prime: Derivada da função f.
    :param x0: Estimativa inicial da raiz.
    :param tol: Tolerância para a precisão da raiz encontrada.
    :param max_iter: Número máximo de iterações.
    :return: Estimativa da raiz da função.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
        # Imprime o erro atual e a derivada
        print(f"Iteração {i + 1}:")
        print(f"  x = {x}")
        print(f"  f(x) = {fx}")
        print(f"  f'(x) = {fpx}")
        print(f"  Erro = {abs(fx)}")
        
        if fpx == 0:
            raise ZeroDivisionError("Derivada zero. O método falhou.")
        
        x_new = x - fx / fpx
        
        if abs(x_new - x) < tol:
            print(f"Convergência alcançada após {i + 1} iterações.")
            return x_new
        
        x = x_new
    
    raise ValueError("Número máximo de iterações atingido sem convergência.")

# Função f(x) = 5*x^3 + x^2 - 12*x + 4
def f(x):
    return 5*x**3 + x**2 - 12*x + 4

# Derivada de f(x): f'(x) = 15*x^2 + 2*x - 12
def f_prime(x):
    return 15*x**2 + 2*x - 12

# Estimativa inicial
x0 = 1.0

# Encontrar a raiz
raiz = newton_raphson(f, f_prime, x0)

print(f"A raiz encontrada é: {raiz}")