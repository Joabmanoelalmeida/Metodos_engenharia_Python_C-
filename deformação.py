import numpy as np

# Definir o campo de deslocamento
def displacement_field(x, y, z):
    u_x = x**2 + y**2 - z**2
    u_y = 2 * x * y
    u_z = -x * z + y * z
    return np.array([u_x, u_y, u_z])

# Função para calcular o gradiente do campo de deslocamento
def gradient_displacement_field(x, y, z):
    u_x, u_y, u_z = displacement_field(x, y, z)
    
    # Gradientes parciais
    du_dx = 2 * x
    du_dy = 2 * y
    du_dz = -2 * z
    
    dv_dx = 2 * y
    dv_dy = 2 * x
    dv_dz = 0
    
    dw_dx = -z
    dw_dy = z
    dw_dz = -x + y
    
    # Gradiente (jacobiana) do campo de deslocamento
    grad_u = np.array([
        [du_dx, du_dy, du_dz],
        [dv_dx, dv_dy, dv_dz],
        [dw_dx, dw_dy, dw_dz]
    ])
    
    return grad_u

# Função para calcular o tensor de deformação
def strain_tensor(x, y, z):
    grad_u = gradient_displacement_field(x, y, z)
    # Tensor de deformação
    E = 0.5 * (grad_u + grad_u.T)
    return E

# Definir um ponto para cálculo
x, y, z = 1.0, 1.0, 1.0
E = strain_tensor(x, y, z)

# Exibir o tensor de deformação de forma legível
print(f'Tensor de Deformação no ponto ({x}, {y}, {z}):')
print(f'[{E[0, 0]:.4f} {E[0, 1]:.4f} {E[0, 2]:.4f}]')
print(f'[{E[1, 0]:.4f} {E[1, 1]:.4f} {E[1, 2]:.4f}]')
print(f'[{E[2, 0]:.4f} {E[2, 1]:.4f} {E[2, 2]:.4f}]')