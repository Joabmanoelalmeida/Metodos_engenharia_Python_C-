import numpy as np
import matplotlib.pyplot as plt

# Define o intervalo de valores para o eixo x
x = np.linspace(0, 2 * np.pi, 1000)

# Calcula os valores de seno e cosseno
seno = np.sin(x)
cosseno = np.cos(x)

# Cria uma nova figura e eixos
plt.figure(figsize=(10, 6))

# Plota a função seno
plt.plot(x, seno, label='Seno', color='blue')

# Plota a função cosseno
plt.plot(x, cosseno, label='Cosseno', color='red')

# Adiciona título e rótulos aos eixos
plt.title('Gráficos das Funções Seno e Cosseno')
plt.xlabel('Ângulo (radianos)')
plt.ylabel('Valor')

# Adiciona uma legenda
plt.legend()

# Adiciona uma grade para facilitar a leitura
plt.grid(True)

# Exibe o gráfico
plt.show()