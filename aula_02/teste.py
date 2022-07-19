import numpy as np

altura = np.round(np.random.normal(1.75, 0.2, 10), 2)
peso = np.round(np.random.normal(60, 10, 10), 2)

print(altura)
print(peso)

dados = np.column_stack((altura, peso))

print(dados)