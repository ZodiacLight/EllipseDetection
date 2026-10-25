import sys
sys.path.append("./")
#
import numpy as np
import math
def pol_zu_kart(phi_koordinaten, r_koordinaten):
    # array zum speichern der Koordinaten erstellen [x,y]
    kart_koordinaten_arr = np.ones_like(phi_koordinaten)
    kart_koordinaten_arr_dublikat = kart_koordinaten_arr[:]
    # zu einem 2d array zusammenfügen
    kart_koordinaten_arr_2d = np.column_stack((kart_koordinaten_arr,kart_koordinaten_arr_dublikat))
    # umrechnung in kart und in array schreiben
    for i in range(len(kart_koordinaten_arr_2d[:,0])):
        kart_koordinaten_arr_2d[i,0] = r_koordinaten[i]*math.cos(phi_koordinaten[i]) # x
        kart_koordinaten_arr_2d[i,1] = r_koordinaten[i]*math.sin(phi_koordinaten[i]) # y
    return kart_koordinaten_arr_2d