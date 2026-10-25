import sys
sys.path.append("./")
#
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#
def graustufenumwandlung(pfad):
    image_path = Image.open(pfad)
    image_gray = image_path.convert('L')
    image_array = np.array(image_gray)
    plt.imshow(image_array, cmap='grey')
    plt.title('Mondkrater in Graustufen',fontsize=14)
    plt.xlabel('Pixel',fontsize=11)
    plt.ylabel('Pixel',fontsize=11)
    plt.show()
    return image_array