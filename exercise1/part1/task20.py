import numpy as np

array = np.arange(24).reshape(4, 6)

print("array:\n", array)

print("maior valor: ", array.max())

print("menor valor: ", array.min())

print("soma dos valores: ", array.sum())

print("media dos valores: ", array.mean())

print("soma de cada linha: ", array.sum(axis = 1))

print("soma de cada coluna: ", array.sum(axis = 0))