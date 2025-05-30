import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def main():
    np.random.seed(42)
    
    # Gerar duas amostras aleatórias
    amostra1 = np.random.normal(loc=5, scale=2, size=100)
    amostra2 = np.random.normal(loc=6, scale=2, size=100)
    
    # Realizar teste t para amostras independentes
    t_stat, p_valor = stats.ttest_ind(amostra1, amostra2)
    
    # Criar histogramas para visualizar as amostras
    plt.figure(figsize=(10, 6))
    
    plt.hist(amostra1, bins=15, alpha=0.5, label='Amostra 1')
    plt.hist(amostra2, bins=15, alpha=0.5, label='Amostra 2')
    
    plt.axvline(np.mean(amostra1), color='blue', linestyle='dashed', linewidth=1)
    plt.axvline(np.mean(amostra2), color='orange', linestyle='dashed', linewidth=1)
    
    plt.title(f'Comparação de Amostras\nEstatística t={t_stat:.4f}, p-valor={p_valor:.4f}')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('t_test_samples.png')
    
    # Task 14
    
    # Exemplo: concatenar as duas amostras e pegar os primeiros 12 elementos
    lista = np.concatenate((amostra1, amostra2))[:12]
    
    # Transformar a lista em array com shape (2, 2, 3)
    array_reshaped = lista.reshape(2, 2, 3)
    
    print("Array reshaped (2, 2, 3):")
    print(array_reshaped)

if __name__ == "__main__":
    main()