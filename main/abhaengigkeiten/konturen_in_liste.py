'''
Speichert die gelabelten Konturen von konturen_finden.py als voneinander unabhängige Arrays
in eine Liste. Diese kann dann als eingabe für die fitschleife verwendet werden.
'''
import numpy as np
def konturen_in_liste(gelabeltes_bild):
    # liste zum speichern der Arrays
    label_liste = []
    for i in range(1,int(np.max(gelabeltes_bild))+1):
        indizes = np.argwhere(np.isin(gelabeltes_bild, i))
        if indizes.size == 0:
            continue
        label_liste.append(np.array(indizes))
    return label_liste