import numpy as np

array = np.arange(21).reshape(3, 7) 

array[0, 0] = 51

array[1, :3] = 0
array[2, :3] = 0

print(array)