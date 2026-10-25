import sys
sys.path.append("./")
import numpy as np
def kart_zu_pol(x_arr,y_arr):
    polar_koordinaten = np.ones((len(x_arr),2))
    for i in range(len(x_arr)):
        r = np.sqrt(x_arr[i]**2+y_arr[i]**2)
        phi = np.arctan2(x_arr[i],y_arr[i])
        polar_koordinaten[i] = np.array([phi,r])
    print('kart zu pol abgeschossen')
    return polar_koordinaten