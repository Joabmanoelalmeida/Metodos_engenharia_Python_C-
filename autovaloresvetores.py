import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir a matriz 3x3
A = np.array([[4, 1, 2],
              [1, 3, 0],
              [2, 0, 5]])

# Calcular autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

# Criar a figura e os eixos
fig = plt.figure(figsize=(16, 8))

# Visualização da matriz
ax1 = fig.add_subplot(121)
cax = ax1.matshow(A, cmap='coolwarm', interpolation='none')
fig.colorbar(cax)

ax1.set_title('Matriz A', fontsize=16)
ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['0', '1', '2'])
ax1.set_yticks([0, 1, 2])
ax1.set_yticklabels(['0', '1', '2'])
for (i, j), val in np.ndenumerate(A):
    ax1.text(j, i, f'{val:.2f}', ha='center', va='center', color='black', fontsize=14)

# Visualização dos autovetores
ax2 = fig.add_subplot(122, projection='3d')

# Plotar autovetores
colors = ['blue', 'red', 'green']
for i in range(autovetores.shape[1]):
    ax2.quiver(0, 0, 0, autovetores[0, i], autovetores[1, i], autovetores[2, i], 
               color=colors[i], 
               label=f'Autovetor {i+1} (λ{i+1} = {autovalores[i]:.2f})')

ax2.set_xlim([-2, 2])
ax2.set_ylim([-2, 2])
ax2.set_zlim([-2, 2])
ax2.set_xlabel('X', fontsize=14)
ax2.set_ylabel('Y', fontsize=14)
ax2.set_zlabel('Z', fontsize=14)
ax2.set_title('Autovetores de A', fontsize=16)
ax2.legend()

plt.tight_layout()
plt.show()