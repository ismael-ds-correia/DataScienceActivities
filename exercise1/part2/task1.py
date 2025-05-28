from scipy import datasets
import matplotlib.pyplot as plt

img = datasets.face()

def main():
    plt.imshow(img)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()