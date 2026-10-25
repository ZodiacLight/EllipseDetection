import cv2
from modified.abhaengigkeiten.gauss_filter import gauss_filter
from Bildaufbereitung.PhaseStretchTansform.modified.abhaengigkeiten.FFT_Kernel import FFT
def run_PST(pfad):
    # bild laden
    bild = cv2.imread(pfad)
    # gaussian filter anwenden
    blurred_bild = gauss_filter(bild,2) # bild, sigma
    # fast fourier transformation anwenden
    fourier_image = FFT()
    # PST Kernen anwenden
    # rücktransformation
