import numpy as np
import cv2 as cv
import math
import time

rostro = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
if rostro.empty():
    print(" No se pudo cargar el clasificador de rostro.")
    exit()
else:
    print(" Clasificador cargado correctamente.")

# Inicializar cámara
cap = cv.VideoCapture(0)
x = y = w = h = 0
count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    t = time.time() - start_time  # tiempo para animaciones

    for (x, y, w, h) in rostros:
        m1 = int(h / 2)
        n1 = int(w / 2)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame, (x + n1, y + m1), int(w / 2), (255, 0, 0), 2)

        # ---------- SOMBRERO NEGRO ELEGANTE ----------
        sombrero_top_y1 = y - int(h * 0.70)
        sombrero_top_y2 = y - int(h * 0.25)
        sombrero_x1 = x - int(w * 0.3)
        sombrero_x2 = x + int(w * 1.2)

        # Parte principal del sombrero
        cv.rectangle(frame, (sombrero_x1, sombrero_top_y1),
                     (sombrero_x2, sombrero_top_y2), (10, 20, 20), -1)
        # Banda gris
        banda_y1 = y - int(h * 0.48)
        banda_y2 = y - int(h * 0.44)
        cv.rectangle(frame, (sombrero_x1, banda_y1),
                     (sombrero_x2, banda_y2), (100, 100, 100), -1)
        # Ala del sombrero
        cv.rectangle(frame, (x - int(w * 0.6), y - int(h * 0.25)),
                     (x + int(w * 1.6), y - int(h * 0.18)), (10, 10, 10), -1)

        # ---------- OJOS (parpadeO) ----------
        radio_base = int(w / 10)
        parpadeo = abs(math.sin(t * 3))
        alto_ojo = max(2, int(radio_base * parpadeo))

        ojo_izq = (x + int(w * 0.33), y + int(h * 0.35))
        ojo_der = (x + int(w * 0.66), y + int(h * 0.35))
        #NEGROS
        cv.ellipse(frame, ojo_izq, (radio_base, alto_ojo), 0, 0, 360, (255, 255, 255), -1)
        cv.ellipse(frame, ojo_der, (radio_base, alto_ojo), 0, 0, 360, (255, 255, 255), -1)
        #BLANCOS
        cv.circle(frame, (ojo_izq[0], ojo_izq[1]), max(2, alto_ojo // 2), (0, 0, 0), -1)
        cv.circle(frame, (ojo_der[0], ojo_der[1]), max(2, alto_ojo // 2), (0, 0, 0), -1)

        # ---------- LENGUA (animada y más grande) ----------
        lengua_tamaño = abs(math.sin(t * 2))
        lengua_altura = int((h // 7) + (lengua_tamaño * h // 5))
        lengua_ancho = int(w // 5)

        boca_x = x + w // 2
        boca_y = y + int(0.78 * h)

        cv.ellipse(frame, (boca_x, boca_y),
                   (lengua_ancho, lengua_altura), 0, 0, 180, (0, 0, 255), -1)
        cv.ellipse(frame, (boca_x, boca_y - 8),
                   (lengua_ancho, lengua_altura // 2), 0, 0, 180, (255, 100, 200), -1)

    cv.imshow('Filtro Animado', frame)

    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
