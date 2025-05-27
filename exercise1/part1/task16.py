import numpy as np

array = np.arange(21).reshape(3, 7)

print("elemento 2 (linha 2): ", array[2])

print("elemento 3 da linha 2: ", array[2, 3])

print("linhas 0 e 1: ", array[0:2])

print("coluna 3: ", array[:, 3])

print("ultimos 3 elementos da linha 1: ", array[0, -3:])
print("ultimos 3 elementos da linha 2: ", array[1:, -3])

print("ultimos 5 elementos de cada linha: ", array[:, -5:])

