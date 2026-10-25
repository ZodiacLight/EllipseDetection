'''
Beim Fit wird die scipy.optimize.curve_fit verwendet
um die besten Ellipsenparameter die zu den Daten passen zu
bestimmen
'''
# Externe abhängigkeiten
import sys
sys.path.append("./")
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from Fitting.abhaengigkeiten.ellipsengleichung import ellipsengleichung
def fit(array_polar, initial_guess):
    # Fit
    params,covariance = curve_fit(ellipsengleichung, array_polar[:,0], array_polar[:,1], p0=initial_guess) # phi,r
    # datenpunkte des Fittes speichern (nur fürs plotten wichtig)
    fit_datenpunkte = ellipsengleichung(array_polar[:,0],*params)
    # exzentrizitaet für den print
    exzentrizitaet = np.sqrt(params[1]**2-params[2]**2)/ params[1]
    # Abweichungskurve zur optimierung des Mittelpunktes
    arr_abweichungskurve = np.ones_like(array_polar[:,0])
    for k in range(arr_abweichungskurve.size):
        arr_abweichungskurve[k] = ellipsengleichung(array_polar[:,0][k],*params) - array_polar[:,1][k]
    # Plotten
    plt.scatter(array_polar[:,0],array_polar[:,1]) # Datenpunkte
    plt.scatter(array_polar[:,0],fit_datenpunkte,label='Fit-Kurve',colorizer='g') # Fit-Kurve
    plt.scatter(array_polar[:,0],ellipsengleichung(array_polar[:,0],*initial_guess),color='g',label='Initial Guess') # Initial Guess
    plt.xlabel('phi (Winkel)')
    plt.ylabel('r (Abstand)')
    plt.show()
    #
    return params, covariance, arr_abweichungskurve, exzentrizitaet # die params werden für den zweiten fit übernommen und kommen in den initial guess