import numpy as np



# np.lispace(0, 22, 5) cria uma lista de 5 números igualmente espaçados entre 0 e 22.
# O espaçamento entre os números é calculado usando a fórmula:
# (stop - start) / (num - 1), onde start é 0, stop é 22 e num é 5.

linspace = np.linspace(0, 22, 5)

for a in linspace:
    print(a)