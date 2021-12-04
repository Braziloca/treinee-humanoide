#o código muda um objeto de cor VERDE para AZUL
import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

while True:
    conectado, frame = webcam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([36, 25, 25])
    upper_green = np.array([70, 255,255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green) 
    result = cv2.bitwise_and(frame, frame, mask=mask)
    result[mask>0] = (255,0,0)

    cv2.imshow('Video original', frame)
    cv2.imshow('Video resultado', result)

    key = cv2.waitKey(5)

    if key == 27: #tecla ESC fecha as janelas
        break

webcam.release()
cv2.destroyAllWindows()