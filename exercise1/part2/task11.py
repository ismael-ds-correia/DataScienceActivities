import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def main():
    x = np.linspace(-4, 4, 1000)
    
    # Criar figura com quatro subplots (2x2)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Distribuição Normal (Gaussiana)
    mu, sigma = 0, 1
    norm_dist = stats.norm(mu, sigma)
    
    # PDF da Normal
    axes[0, 0].plot(x, norm_dist.pdf(x), 'b-', linewidth=2)
    axes[0, 0].set_title('PDF - Distribuição Normal')
    axes[0, 0].grid(True)
    
    # CDF da Normal
    axes[0, 1].plot(x, norm_dist.cdf(x), 'b-', linewidth=2)
    axes[0, 1].set_title('CDF - Distribuição Normal')
    axes[0, 1].grid(True)
    
    # 2. Distribuição t de Student
    df = 3
    t_dist = stats.t(df)
    
    # PDF da t-Student
    axes[1, 0].plot(x, t_dist.pdf(x), 'r-', linewidth=2)
    axes[1, 0].set_title('PDF - Distribuição t-Student (df=3)')
    axes[1, 0].grid(True)
    
    # CDF da t-Student
    axes[1, 1].plot(x, t_dist.cdf(x), 'r-', linewidth=2)
    axes[1, 1].set_title('CDF - Distribuição t-Student (df=3)')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig('probability_distributions.png')
    print("Gráficos das distribuições de probabilidade salvos em 'probability_distributions.png'")

if __name__ == "__main__":
    main()