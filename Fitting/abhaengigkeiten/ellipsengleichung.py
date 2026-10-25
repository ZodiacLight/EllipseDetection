'''
Ellipsengleichung zur Berechnung der Ellipsen-Parameter
in Polarkoordinaten.
'''
import sys
sys.path.append("./")
#
import numpy as np
def ellipsengleichung(phi,e,b,c):
    return b/np.sqrt(1-e**2*np.cos(phi+c)**2)