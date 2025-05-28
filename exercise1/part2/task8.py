import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import special

def main():
    # Definir intervalo de valores x
    x = np.linspace(-5, 5, 1000)
    
    # Criar figura com dois subplots
    plt.figure(figsize=(12, 5))
    
    # 1. Funções de Bessel
    plt.subplot(1, 2, 1)
    for n in range(4):
        plt.plot(x, special.jv(n, x), label=f'J{n}(x)')
    
    plt.title('Funções de Bessel de Primeiro Tipo')
    plt.xlabel('x')
    plt.ylabel('J_n(x)')
    plt.grid(True)
    plt.legend()
    
    # 2. Função de erro Gaussiana
    plt.subplot(1, 2, 2)
    plt.plot(x, special.erf(x), 'r-', linewidth=2)
    
    plt.title('Função de Erro Gaussiana')
    plt.xlabel('x')
    plt.ylabel('erf(x)')
    plt.grid(True)
    
    # Salvar figura
    plt.tight_layout()
    plt.savefig('special_functions.png')
    print("Gráficos salvos em 'special_functions.png'")

if __name__ == "__main__":
    main()