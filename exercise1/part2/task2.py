import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import datasets

img = datasets.face()

gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

def main():
    plt.imshow(gray, cmap='gray')
    plt.axis('off')
    plt.savefig('face_gray.png') 

if __name__ == '__main__':
    main()