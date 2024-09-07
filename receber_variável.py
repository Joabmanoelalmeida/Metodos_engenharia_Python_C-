import numpy as np
import matplotlib.pyplot as plt

# Define o intervalo de valores para o eixo x
x = np.linspace(0, 2 * np.pi, 1000)

# Calcula os valores de seno e cosseno
seno = np.sin(x)
cosseno = np.cos(x)

# Cria uma nova figura e eixos
plt.figure(figsize=(12, 8))

# Plota a função seno com estilo de linha e marcador
plt.plot(x, seno, label='Seno', color='blue', linestyle='-', marker='', linewidth=2)

# Plota a função cosseno com estilo de linha e marcador
plt.plot(x, cosseno, label='Cosseno', color='red', linestyle='--', marker='', linewidth=2)

# Adiciona título e rótulos aos eixos
plt.title('Gráficos das Funções Seno e Cosseno', fontsize=16)
plt.xlabel('Ângulo (radianos)', fontsize=14)
plt.ylabel('Valor', fontsize=14)

# Adiciona uma legenda
plt.legend()

# Adiciona uma grade para facilitar a leitura
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adiciona linhas horizontais e verticais em y=0
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

# Adiciona anotações para pontos específicos
plt.annotate('π', xy=(np.pi, 0), xytext=(np.pi, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='blue')
plt.annotate('2π', xy=(2 * np.pi, 0), xytext=(2 * np.pi, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='red')

# Ajusta os limites dos eixos
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.5, 1.5)

# Adiciona marcas e rótulos aos eixos
plt.xticks(np.linspace(0, 2 * np.pi, 5), ['0', 'π/2', 'π', '3π/2', '2π'])
plt.yticks(np.linspace(-1, 1, 5))

# Exibe o gráfico
plt.show()

# Adiciona uma grade para facilitar a leitura
plt.grid(True)

# Exibe o gráfico
plt.show()