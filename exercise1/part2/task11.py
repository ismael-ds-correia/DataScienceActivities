import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#parâmetros da distribuição Normal
mu = 0      # média
sigma = 1   # desvio padrão


x = np.linspace(- 4, 4, 100)

# PDF e CDF
pdf = norm.pdf(x)
cdf = norm.cdf(x)

# Plotando
plt.figure(figsize=(12, 5))

plt.plot(x, pdf, label='PDF')
plt.plot(x, cdf, label='CDF')
plt.title('Funções PDF e CDF da Distribuição Normal')
plt.xlabel('x')
plt.ylabel('Probabilidade')
plt.grid()
plt.legend()
plt.show()