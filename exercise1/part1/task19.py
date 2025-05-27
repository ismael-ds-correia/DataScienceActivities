import numpy as np

list1 = np.array([1, 2, 3])
list2 = np.array([4, 5, 6])

sum = list1 + list2
multiplication = list1 * list2
division = list1 / list2

results = np.array([sum, multiplication, division])
print("Results:")
print(results)