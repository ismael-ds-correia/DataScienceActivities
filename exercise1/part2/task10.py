import matplotlib
matplotlib.use('Agg')  # Backend não-interativo
import matplotlib.pyplot as plt
import numpy as np
from scipy import special

def main():
    # Criar um intervalo de valores x no domínio dos polinômios de Legendre [-1, 1]
    x = np.linspace(-1, 1, 1000)
    
    plt.figure(figsize=(10, 6))
    
    # Gerar e plotar os primeiros 5 polinômios de Legendre
    for n in range(5):
        # Calcular o polinômio de Legendre de ordem n
        legendre_poly = special.legendre(n)
        y = legendre_poly(x)
        plt.plot(x, y, label=f'P_{n}(x)')
    
    # Adicionar detalhes ao gráfico
    plt.title('Polinômios de Legendre')
    plt.xlabel('x')
    plt.ylabel('P_n(x)')
    plt.grid(True)
    plt.legend()
    
    # Adicionar linha horizontal em y=0 para melhor visualização
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('legendre_polynomials.png')
    print("Gráfico dos polinômios de Legendre salvo em 'legendre_polynomials.png'")

if __name__ == "__main__":
    main()