import numpy as np


a = np.poly1d([3, 4])
print("Polinômio a:")
print(a)

b = np.poly1d([4, 3, 2, 1])
print("Polinômio b:")
print(b)

c = np.poly1d([2, 0, 0, 3])
print("Polinômio c:")
print(c)

d = np.poly1d([1, 2, 3])
print("Polinômio d:")
print(d)

productCxD = c * d
print("Produto de c e d:")
print(productCxD)

d_prime = d.deriv()
print("Derivada de d:")
print(d_prime)

d_integral = d.integ()
print("Integral de d:")
print(d_integral)