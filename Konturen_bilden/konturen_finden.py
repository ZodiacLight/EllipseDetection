import sys
sys.path.append("./")
import numpy as np
from Bildaufbereitung.canny_edge import canny_edge
from Bildaufbereitung.graustufenumwandlung import graustufenumwandlung
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import time

'''
Zum Bilden von unabhängigen Bildkonturen wird als Eingabe ein schwarz-weiß Kantenbild erwartet (wie Canny Edge).
Der Code ist am connected component labeling orientiert. Allerdings werden auch die Diagonalen Nachbarnpixel mit einbezogen
und nicht nur die horizontalen und die vertikalen.
'''

def konturen_finden(kanten_array):
    # label array erstellen
    label_array = np.zeros(kanten_array.shape)
    # pixel label
    pixel_label = 1
    # zähler der nachbarn mit helligkeit = null
    null_counter = 0
    # pass counter
    pass_counter = 0
    # wie oft das label geändert wurde
    label_switch_counter = 0
    #
    bild_hoehe, bild_breite = kanten_array.shape
    # pixel range die überprüft wird
    pixel_range = [[0,-1],[-1,-1],[-1,0],[-1,+1]]
    # zeit stoppen
    zeit_start = time.time()
    # for schleife
    for y in range(bild_hoehe):
        for x in range(bild_breite):
            pass_counter = 0
            null_counter = 0
            naechsten_pixel_testen = False
            label_switch_counter = 0
            # jede zeile die komplett schwarz ist überspringen
            if np.all(kanten_array[y,:] == 0):
                continue
            # nur wenn der pixel weiß ist
            if kanten_array[y,x] != 0:
                for idx in pixel_range:
                    # wenn der pixel weiß ist
                    try:
                        if label_array[y+idx[0],x+idx[1]] != 0:
                            print('übernommenes label: ',label_array[y+idx[0],x+idx[1]])
                            #label_array[y,x] = label_array[y+idx[0],x+idx[1]]
                            if label_switch_counter >= 1 and label_array[y+idx[0],x+idx[1]] != label_array[y,x]:
                                print('label werden zu einem ergänzt: ',label_array[y+idx[0],x+idx[1]],'-->', label_array[y,x])
                                # alle pixel mit dem label des zweiten pixels filtern
                                pixel_label_zu_aendern = np.where(label_array == label_array[y+idx[0],x+idx[1]])
                                anzahl_fundstellen = len(pixel_label_zu_aendern[0])
                                # alle pixel mit dem label des zweiten weißen nachbarn (zweites neues label) auf das des ersten weißen nachbarns setzen
                                label_array[pixel_label_zu_aendern] = label_array[y,x]
                                #for pixel in range(anzahl_fundstellen):
                                #    label_array[pixel_label_zu_aendern[0][pixel],pixel_label_zu_aendern[1][pixel]] = label_array[y,x]
                                #pass_counter = 0
                                #null_counter = 0
                                naechsten_pixel_testen = True
                                continue
                            label_array[y,x] = label_array[y+idx[0],x+idx[1]]
                            label_switch_counter += 1
                    except IndexError as e:
                        pass_counter += 1
                        continue
                    #else:
                    if label_array[y+idx[0],x+idx[1]] == 0:
                        null_counter += 1
                        continue
                    elif naechsten_pixel_testen == True:
                        continue
                if pass_counter + null_counter == 4:
                    # neues label einrichten
                    label_array[y,x] = pixel_label
                    pixel_label += 1
                    continue
    zeit_ende = time.time() - zeit_start
    print('dauer:', zeit_ende)
    # color mapping
    #num_labels = (len(np.unique(label_array[label_array != 0])))
    label_array_temp = label_array.copy()
    unique_values = np.unique(label_array)
    unique_values = unique_values[unique_values > 0]
    for u_new, u_old in enumerate(unique_values,start=1):
        label_array_temp[label_array == u_old] = u_new
    unique_values = np.unique(label_array)
    unique_values = unique_values[unique_values > 0]
    label_array = label_array_temp
    #ergebnis = np.any(label_array[:,] > 0)
    # zufallsordnung der farben
    for u_new, u_old in enumerate(np.random.permutation(unique_values),start=1):
        label_array_temp[label_array == u_old] = u_new
    num_labels = int(np.max(label_array))
    ergebnis = np.any(label_array[:,] > 0)
    label_array = label_array_temp
    unique_values1 = len(np.unique(label_array > 0))
    print(unique_values1)
    print(ergebnis)
    # Min-Max scaling
    #min_val = np.min(label_array)
    #print('min val: ',min_val)
    #max_val = np.max(label_array)
    scaled_data = label_array#(label_array - min_val) / (max_val - min_val)*20
    # 1. Wähle eine farbenfrohe Map (gist_ncar hat ein breites Spektrum)
    base_cmap = plt.get_cmap('prism',num_labels)
    # 2. Extrahiere Farben in gleichmäßigen Abständen
    color_list = base_cmap(np.linspace(0,1,num_labels))
    color_list[0] = [0.13, 0.13, 0.13, 1]
    # 3. Erstelle daraus eine neue diskrete Map
    custom_cmap = ListedColormap(color_list)
    #
    plt.xlabel('Pixel',fontsize=15)
    plt.ylabel('Pixel',fontsize=15)
    plt.title('Canny-Bild gelabelt',fontsize=20)
    plt.imshow(scaled_data,cmap=custom_cmap,vmin=0,vmax=num_labels)
    plt.show()
    # neuer plot: histogramm
    # 2. Histogramm erstellen
    plt.figure()
    plt.title("Grauwert-Histogramm")
    plt.xlabel("Intensitätswert")
    plt.ylabel("Anzahl Pixel")
    # 3. Nullen herausfiltern (Boolesche Maske)
    filtered_pixels = scaled_data[scaled_data > 0]
    plt.hist(filtered_pixels.ravel(), bins=256, range=(0, np.max(scaled_data)), color='gray', alpha=0.7)
    plt.show()
    #
    gefilterd_label_array = label_array[label_array != 0]
    rows = np.nonzero(label_array)[0]
    plt.plot(gefilterd_label_array,rows,'o')
    plt.show()
    return scaled_data
#
#pfad = r'/home/robin/SFN/Mondkraterdatierung für sterbliche/Daten/Bilder/png/Mare_Humorum.png'
#konturen_finden(canny_edge(graustufenumwandlung(pfad)))