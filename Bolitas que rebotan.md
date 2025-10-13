import cv2 as cv
import numpy as np
import random
import math

# Crear ventana
width, height = 500, 500
img = np.ones((height, width, 3), dtype=np.uint8) * 255

class Pelota:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.colores = [
            (0, 0, 255),    # Rojo
            (255, 0, 0),    # Azul
            (0, 255, 0),    # Verde
            (0, 255, 255),  # Amarillo
            (255, 0, 255),  # Magenta
            (255, 255, 0),  # Cian
            (0, 0, 0),      # Negro
            (128, 0, 128)   # Morado
        ]
    
    def mover(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Rebotar en los bordes y cambiar color
        if self.x <= self.radius or self.x >= width - self.radius:
            self.speed_x *= -1
            self.x = max(self.radius, min(self.x, width - self.radius))
            self.cambiar_color()
        
        if self.y <= self.radius or self.y >= height - self.radius:
            self.speed_y *= -1
            self.y = max(self.radius, min(self.y, height - self.radius))
            self.cambiar_color()
    
    def cambiar_color(self):
        # Cambiar a un color aleatorio diferente al actual
        nuevo_color = self.color
        while nuevo_color == self.color:
            nuevo_color = random.choice(self.colores)
        self.color = nuevo_color
    
    def dibujar(self, frame):
        cv.circle(frame, (int(self.x), int(self.y)), self.radius, self.color, -1)
        # Efecto 3D
        cv.circle(frame, (int(self.x - self.radius/3), int(self.y - self.radius/3)), 
                 int(self.radius/3), (255, 255, 255), -1)
    
    def check_colision(self, otra_pelota):
        distance = math.sqrt((self.x - otra_pelota.x)**2 + (self.y - otra_pelota.y)**2)
        return distance <= (self.radius + otra_pelota.radius)

# Crear dos pelotas del mismo tamaño
pelota1 = Pelota(100, 100, 25, (0, 0, 255), 3, 2)
pelota2 = Pelota(400, 400, 25, (255, 0, 0), -2, -3)

while True:
    # Crear fondo blanco
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    # Mover pelotas
    pelota1.mover()
    pelota2.mover()
    
    # Verificar colisión entre pelotas
    if pelota1.check_colision(pelota2):
        # Intercambiar velocidades (rebote elástico)
        pelota1.speed_x, pelota2.speed_x = pelota2.speed_x, pelota1.speed_x
        pelota1.speed_y, pelota2.speed_y = pelota2.speed_y, pelota1.speed_y
        
        # Cambiar colores de ambas pelotas
        pelota1.cambiar_color()
        pelota2.cambiar_color()
        
        # Separar las pelotas para evitar que se queden pegadas
        overlap = (pelota1.radius + pelota2.radius) - math.sqrt(
            (pelota1.x - pelota2.x)**2 + (pelota1.y - pelota2.y)**2)
        
        if overlap > 0:
            angle = math.atan2(pelota2.y - pelota1.y, pelota2.x - pelota1.x)
            pelota1.x -= overlap * math.cos(angle) / 2
            pelota1.y -= overlap * math.sin(angle) / 2
            pelota2.x += overlap * math.cos(angle) / 2
            pelota2.y += overlap * math.sin(angle) / 2
    
    # Dibujar pelotas
    pelota1.dibujar(img)
    pelota2.dibujar(img)
    
    # Mostrar frame
    cv.imshow('Dos Pelotas Rebotando', img)
    
    # Solo esperar un poco para la animación
    cv.waitKey(30)

cv.destroyAllWindows()
