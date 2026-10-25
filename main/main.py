import sys
sys.path.append("./")
# Bildaufbereitung
from Bildaufbereitung.graustufenumwandlung import graustufenumwandlung
from Bildaufbereitung.canny_edge import canny_edge
from Konturen_bilden.konturen_finden import konturen_finden
from Fitting.fitschleife import fitschleife
from main.abhaengigkeiten import konturen_in_liste

def main():
    # Fitting
    from Fitting.fitschleife import fitschleife
    # Bildpfad
    pfad = "/home/robin/SFN/Ellipsenerkennung/Daten/Bilder/Mare_Humorum.jpg"
    # canny bild
    canny_bild = canny_edge(graustufenumwandlung(pfad))
    # Konturen finden
    konturen_array = konturen_finden(canny_bild)
    # Konturen in eine Liste schreiben und an die Fitschleife übergeben
    fitting = fitschleife(konturen_in_liste(konturen_array))

main()