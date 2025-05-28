import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import datasets as misc

img = misc.face()

def main():
    plt.imshow(img)
    plt.axis('off')
    plt.savefig('face.png')

if __name__ == '__main__':
    main()