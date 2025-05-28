import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

x = np.linspace(1, 5, 100)
y = gamma(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Gamma', color='blue')
plt.title('Função Gamma')
plt.xlabel('x')
plt.ylabel('Gamma(x)')
plt.grid(True)
plt.legend()
plt.show()
