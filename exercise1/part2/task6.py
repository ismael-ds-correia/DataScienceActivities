import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import datasets
from skimage.transform import resize

def main():
    # Carregar a imagem original
    img = datasets.face()
    gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    
    # Obter dimensões originais
    original_height, original_width = gray.shape
    
    # Redimensionar para 50%
    half_size = resize(gray, (original_height // 2, original_width // 2), 
                      anti_aliasing=True)
    
    # Voltar ao tamanho original usando interpolação bilinear
    restored = resize(half_size, (original_height, original_width), 
                     order=1, anti_aliasing=False)
    
    # Plotar as imagens para comparação
    plt.figure(figsize=(15, 5))
    
    # Imagem original
    plt.subplot(1, 3, 1)
    plt.imshow(gray, cmap='gray')
    plt.title('Original')
    plt.axis('off')
    
    # Imagem reduzida a 50%
    plt.subplot(1, 3, 2)
    plt.imshow(half_size, cmap='gray')
    plt.title('Reduzida (50%)')
    plt.axis('off')
    
    # Imagem restaurada ao tamanho original
    plt.subplot(1, 3, 3)
    plt.imshow(restored, cmap='gray')
    plt.title('Restaurada (interpolação bilinear)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('interpolation_comparison.png')
    
    diff = np.abs(gray - restored)
    print(f"Erro médio de reconstrução: {np.mean(diff):.4f}")
    print(f"Erro máximo de reconstrução: {np.max(diff):.4f}")

if __name__ == "__main__":
    main()