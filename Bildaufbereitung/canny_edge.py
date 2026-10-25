import sys
sys.path.append("./")
#
import numpy as np
import scipy
import cv2
import matplotlib.pyplot as plt
#
def canny_edge(bild_array): # eingabe ist ein graues Bild (array)
    image_grey_array = np.array(bild_array)
    # canny filter anwenden
    filter_size = 5
    image_median_array = scipy.ndimage.median_filter(image_grey_array, size=filter_size)
    canny_Edge = cv2.Canny(image_median_array,threshold1=20, threshold2=80) # 15,20
    plt.imshow(canny_Edge, cmap='gray')
    plt.xlabel('X Achse [px]')
    plt.ylabel('Y Achse [px]')
    plt.show()
    return canny_Edge