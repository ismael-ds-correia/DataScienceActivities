import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def main():
    np.random.seed(42)
    
    # Gerar duas amostras aleatórias
    # Grupo 1: Distribuição normal com média 5 e desvio padrão 2
    # Grupo 2: Distribuição normal com média 6 e desvio padrão 2
    amostra1 = np.random.normal(loc=5, scale=2, size=100)
    amostra2 = np.random.normal(loc=6, scale=2, size=100)
    
    # Realizar teste t para amostras independentes
    t_stat, p_valor = stats.ttest_ind(amostra1, amostra2)
    
    # Criar histogramas para visualizar as amostras
    plt.figure(figsize=(10, 6))
    
    # Histograma da amostra 1
    plt.hist(amostra1, bins=15, alpha=0.5, label='Amostra 1')
    
    # Histograma da amostra 2
    plt.hist(amostra2, bins=15, alpha=0.5, label='Amostra 2')
    
    # Adicionar detalhes ao gráfico
    plt.axvline(np.mean(amostra1), color='blue', linestyle='dashed', linewidth=1)
    plt.axvline(np.mean(amostra2), color='orange', linestyle='dashed', linewidth=1)
    
    plt.title(f'Comparação de Amostras\nEstatística t={t_stat:.4f}, p-valor={p_valor:.4f}')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('t_test_samples.png')

if __name__ == "__main__":
    main()