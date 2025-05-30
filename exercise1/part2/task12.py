import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

x = np.arange(0, 20)

pmf = binom.pmf(x, n=20, p=0.5)

plt.figure(figsize=(14, 5))
plt.vlines(x, 0, pmf, colors='b', lw=5, label='PMF')
plt.plot(x, pmf, 'bo', ms=8)
plt.title('Distribuição Binomial PMF')
plt.xlabel('Número de Sucessos')
plt.ylabel('Probabilidade')
plt.grid()
plt.legend()

plt.show()
