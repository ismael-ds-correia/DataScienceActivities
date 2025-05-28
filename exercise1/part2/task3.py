import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

def main():
    img = datasets.face()
    
    gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    
    print("Array da imagem em escala de cinza:")
    print(gray)

if __name__ == "__main__":
    main()