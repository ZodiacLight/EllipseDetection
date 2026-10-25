from scipy.ndimage import gaussian_filter
def gauss_filter(bild, sigma):
    # gauss filter anwenden
    blurred_image = gaussian_filter(bild,sigma)
    return blurred_image