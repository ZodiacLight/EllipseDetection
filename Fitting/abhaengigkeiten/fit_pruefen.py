import sys
sys.path.append("./")
#
import numpy as np
def fit_pruefen(fehler): # die konvarianzmatrix
    # wenn die Abweichungen nicht zu groß sind wird Ellipsenwert auf eins gesetzt (True)
    ellipsen_wert = 0
    # Standartabweichung berechnen
    abweichung = np.sqrt(np.diag(fehler))
    # schwellwert definieren
    schwellwert = np.array([12,12,12]) # exzentrizität,kleine Halbachse,Rotation
    k = 0
    grosse_abweichung = False
    for i in abweichung:
        if k > abweichung.size:
            break
        if i > schwellwert[k]:
            print('die gesammte abweichung beträgt:',abweichung)
            grosse_abweichung = True
            #break
        k += 1
    if grosse_abweichung == False:
        print('die abweichung beträgt: ',abweichung)
        ellipsen_wert += 1
    #
    return ellipsen_wert