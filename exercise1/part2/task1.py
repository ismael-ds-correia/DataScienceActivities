import matplotlib
matplotlib.use('Agg')         # <-- escolhe um backend “headless”
import matplotlib.pyplot as plt
from scipy import datasets

img = datasets.face()

def main():
    plt.imshow(img)
    plt.axis('off')
    plt.savefig('face.png')  # salva em arquivo em vez de plt.show()

if __name__ == '__main__':
    main()