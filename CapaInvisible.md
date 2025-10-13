import cv2
import numpy as np

# Captura de video desde la cámara
cap = cv2.VideoCapture(0)
# Permitir que la cámara se estabilice
cv2.waitKey(2000)
# Capturar el fondo durante unos segundos
ret, background = cap.read()
if not ret:
    print("Error al capturar el fondo.")
    cap.release()
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convertir el cuadro a espacio de color HSV para ambos procesos
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # ======================================================
    #   VENTANA 1: INVISIBILIDAD VERDE
    # ======================================================
    
    # Rango de color VERDE en HSV
    lower_green = np.array([80, 40, 40])
    upper_green = np.array([145, 255, 255])
    
    # Crear máscara VERDE y su inversa (lo que NO es verde)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv_green = cv2.bitwise_not(mask_green)
    
    # Aplicar máscaras para el croma key verde
    res1_green = cv2.bitwise_and(frame, frame, mask=mask_inv_green)
    res2_green = cv2.bitwise_and(background, background, mask=mask_green)
    
    # Output final 1 (Verde invisible)
    final_output_green = cv2.addWeighted(res1_green, 1, res2_green, 1, 0)
    
    
    # ======================================================
    #   VENTANA 2: INVISIBILIDAD ROJA
    # ======================================================
    
    # El rojo está en ambos extremos del espectro HSV, por lo que se necesitan dos rangos:
    # Rango 1 (Rojo oscuro)
    lower_red_1 = np.array([0, 120, 70])
    upper_red_1 = np.array([10, 255, 255])
    # Rango 2 (Rojo brillante)
    lower_red_2 = np.array([170, 120, 70])
    upper_red_2 = np.array([180, 255, 255])
    
    # Crear dos máscaras y combinarlas con un OR bitwise
    mask_red_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask_red_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)
    
    # Crear la máscara inversa (lo que NO es rojo, que se mantiene visible)
    mask_inv_red = cv2.bitwise_not(mask_red)

    # Aplicar máscaras para el croma key rojo
    # res1_red: Solo la persona (lo NO rojo)
    res1_red = cv2.bitwise_and(frame, frame, mask=mask_inv_red)
    # res2_red: Solo el fondo (lo rojo se reemplaza por el fondo)
    res2_red = cv2.bitwise_and(background, background, mask=mask_red)
    
    # Output final 2 (Rojo invisible)
    final_output_red = cv2.addWeighted(res1_red, 1, res2_red, 1, 0)
    
    # --- MOSTRAR AMBAS VENTANAS ---
    
    # Ventana 1: Croma key verde (original)
    cv2.imshow("1. Capa de Invisibilidad (Verde Invisible)", final_output_green)
    
    # Ventana 2: Croma key rojo (nueva)
    cv2.imshow("2. Croma Key Rojo (Rojo Invisible)", final_output_red)
    # cv2.imshow('Mascara Roja (debug)', mask_red) # Opcional para ver la detección del rojo

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
