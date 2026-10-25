import sys
sys.path.append("./")
#
import numpy as np
def daten_zentrieren(daten,mittelpunkt):
    print('der input mittelpunkt fürs zentrieren hat eine shape von:',mittelpunkt.shape)
    print('die input daten fürs zentrieren haben eine shape von:',daten.shape)
    verschobene_datenpunkte_arr = np.ones_like(daten)
    verschobene_datenpunkte_arr[:,0] = daten[:,0] - mittelpunkt[0,0] # x
    verschobene_datenpunkte_arr[:,1] = daten[:,1] - mittelpunkt[0,1] # y
    print('zetrierung abgschlossen')
    return verschobene_datenpunkte_arr