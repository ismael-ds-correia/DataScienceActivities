import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 

multi_B = np.array(a)

print("multi_B:")
print(multi_B)

print("Numero de linhas da lista A: ", len(a))
print("Numero de colunas da lista A: ", len(a[0]))

print("Shape do multi_B (dimensoes): ", multi_B.shape)