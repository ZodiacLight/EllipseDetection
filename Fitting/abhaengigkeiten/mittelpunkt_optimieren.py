'''
Bei der optimierung des Mittelpunktes wird der Median aller Abweichungen
als optimierterer Mittelpunkt angenommen.
'''
import sys
sys.path.append("./")
#
from koordianten_transformationen.pol_zu_kart import pol_zu_kart
import numpy as np
def mittelpunkt_optimieren(arr_abweichungskurve,phi_arr):
    # array aufsteigend sortieren
    abweichungskurve_sortiert = np.sort(arr_abweichungskurve)
    phi_sortiert = np.sort(phi_arr)
    # median berechen
    abweichungskurve_median = np.median(abweichungskurve_sortiert)
    phi_median = np.median(phi_sortiert)
    #
    optimierter_mittelpunkt = phi_median,abweichungskurve_median
    return np.array(optimierter_mittelpunkt).reshape(1,2)