import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time

# Les caractères ASCII du plus sombre au plus clair
ASCII_CHARS = "@%#*+=-:. "

def map_pixels_to_ascii(image, range_width=25):
    """Convertit une image en caractères ASCII"""
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value//range_width]
    return ascii_str

def main():
    # Capture vidéo
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Redimensionner l'image
        width = 120  # Largeur de sortie ASCII
        height = 60  # Hauteur de sortie ASCII
        frame = cv2.resize(frame, (width, height))
        
        # Convertir en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Convertir en ASCII
        im = Image.fromarray(gray)
        ascii_str = map_pixels_to_ascii(im)
        
        # Afficher le résultat
        ascii_str_len = len(ascii_str)
        ascii_img=""
        for i in range(0, ascii_str_len, width):
            ascii_img += ascii_str[i:i+width] + '\n'
        print(ascii_img)
        
        # Effacer l'écran (Windows)
        time.sleep(0.05)
        print('\033[H\033[J')
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()