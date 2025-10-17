import cv2
import numpy as np

# Inicializa una lista para almacenar los puntos de la trayectoria
puntos_trayectoria = []

# Abre la cámara.
cap = cv2.VideoCapture(0)

# El bucle principal para capturar fotogramas
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Voltea el fotograma horizontalmente
    frame = cv2.flip(frame, 1)

    # Crea una copia del fotograma para aplicar la transformación de color y dibujar
    frame_display = frame.copy() 

    # Convierte el fotograma de BGR a HSV para la detección de color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- DEFINICIÓN DE RANGOS DE COLOR ROJO ---
    # Rango 1 (Tono bajo de Rojo)
    rango_rojo_bajo1 = np.array([0, 120, 70])
    rango_rojo_alto1 = np.array([10, 255, 255])
    # Rango 2 (Tono alto de Rojo)
    rango_rojo_bajo2 = np.array([170, 120, 70])
    rango_rojo_alto2 = np.array([180, 255, 255])

    # Crea y combina las máscaras de color rojo
    mascara1 = cv2.inRange(hsv, rango_rojo_bajo1, rango_rojo_alto1)
    mascara2 = cv2.inRange(hsv, rango_rojo_bajo2, rango_rojo_alto2)
    mascara_final = cv2.bitwise_or(mascara1, mascara2)

    # --- ENCONTRAR CONTORNOS Y SEGUIMIENTO DE TRAYECTORIA ---
    
    # Encuentra los contornos en la máscara
    contornos, _ = cv2.findContours(mascara_final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Si se encuentran contornos, procesa el más grande
    if contornos:
        contorno_mas_grande = max(contornos, key=cv2.contourArea)

        # Solo si el área del contorno es lo suficientemente grande, se activa el seguimiento
        if cv2.contourArea(contorno_mas_grande) > 500:
            
            # --- CÁLCULO DEL CENTRO PARA LA TRAYECTORIA ---
            M = cv2.moments(contorno_mas_grande)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Agrega las coordenadas del centro a nuestra lista de trayectoria
                puntos_trayectoria.append((cx, cy))

                # Dibuja un círculo en el centro del objeto detectado (color verde para la trayectoria)
                cv2.circle(frame_display, (cx, cy), 5, (0, 255, 0), -1) 
            
            # --- PINTAR EL OBJETO DE MORADO ---
            
            # 1. Crea una imagen Morada del mismo tamaño que el frame. BGR para Morado es (255, 0, 255)
            # El morado es B=255, G=0, R=255.
            color_morado = np.full_like(frame, (255, 0, 255), dtype=np.uint8)
            
            # 2. Solo aplica la imagen Morada en el área donde se detectó el Rojo
            area_morada = cv2.bitwise_and(color_morado, color_morado, mask=mascara_final)
            
            # 3. Deja el resto de la imagen sin cambios (lo que NO es rojo)
            mascara_inv = cv2.bitwise_not(mascara_final)
            frame_sin_rojo = cv2.bitwise_and(frame_display, frame_display, mask=mascara_inv)
            
            # 4. Combina el frame_sin_rojo con el area_morada
            frame_display = cv2.add(frame_sin_rojo, area_morada)
            
            # Actualiza el frame de visualización
            frame = frame_display
    
    # --- DIBUJAR LA LÍNEA DE LA TRAYECTORIA EN LA PANTALLA ---
    # La trayectoria se dibuja con los puntos previamente guardados
    for i in range(1, len(puntos_trayectoria)):
        if puntos_trayectoria[i-1] is None or puntos_trayectoria[i] is None:
            continue

        # Dibuja la línea verde de la trayectoria sobre el frame modificado
        grosor = int(np.sqrt(len(puntos_trayectoria) / float(i + 1)) * 2.5)
        cv2.line(frame, puntos_trayectoria[i-1], puntos_trayectoria[i], (0, 255, 0), grosor)

    # Muestra el fotograma con los dibujos
    cv2.imshow('Seguimiento Morado y Trayectoria', frame)

    # Si se presiona la tecla 'q', salimos del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()
