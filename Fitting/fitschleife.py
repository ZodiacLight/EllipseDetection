import sys
sys.path.append("./")
import numpy as np
from Fitting.abhaengigkeiten.fit import fit
from Fitting.abhaengigkeiten.punkte_mitteln import punkte_mitteln
from Fitting.abhaengigkeiten.daten_zentrieren import daten_zentrieren
from koordianten_transformationen.kart_zu_pol import kart_zu_pol
from koordianten_transformationen.pol_zu_kart import pol_zu_kart
from Fitting.abhaengigkeiten.fit_pruefen import fit_pruefen
from Fitting.abhaengigkeiten.mittelpunkt_optimieren import mittelpunkt_optimieren
#
def fitschleife(array_liste):
    # counter für gefundene Ellipsen
    gefundene_ellipsen = 0
    for array in array_liste:
        # grober Mittelpunkt zur Umrechnung in Polar
        gemittelter_startpunkt = punkte_mitteln()
        # Daten zentrieren
        zentriert = daten_zentrieren(array,gemittelter_startpunkt)
        # Koordinaten Transformation
        polar = (zentriert)
        # initial guess als anfangsschätzung für die Fit-Parameter berechnen
        initial_guess = []
        # erster Fit
        fit1 = fit(polar,initial_guess)
        # rück transfomration 
        kart = pol_zu_kart()
        # optimierung des Mittelpunktes
        optimierter_mittelpunkt = mittelpunkt_optimieren()
        # zentrieren
        zentriert1 = daten_zentrieren(array,optimierter_mittelpunkt)
        # kartesisch in Polar
        polar1 = kart_zu_pol(zentriert1)
        # zweiter Fit mit übernommenen parametern des ersten Fits
        fit2 = fit(polar1,fit1[0])
        # fit mit schwellenwerten überprüfen
        fit_abweichungen = fit_pruefen(fit2[1])
        if fit_abweichungen == True:
            gefundene_ellipsen += 1
        else:
            continue
    print('gefundene Ellipsen:',gefundene_ellipsen)
    return gefundene_ellipsen
