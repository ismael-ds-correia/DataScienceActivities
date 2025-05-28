import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import datasets
from skimage.transform import resize

def main():
    img = datasets.face()
    
    gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    
    height, width = gray.shape
    resized = resize(gray, (height // 2, width // 2), anti_aliasing=True)
    
    plt.figure()
    plt.imshow(resized, cmap='gray')
    plt.axis('off')
    plt.savefig('face_resized_50percent.png')

if __name__ == "__main__":
    main()