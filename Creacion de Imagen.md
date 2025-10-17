import numpy as np
import cv2 as cv

# Crea una imagen de 500x500 píxeles
img = np.ones((500, 500), dtype=np.uint8) * 240

# "HOLA" en la parte superior
# H
for i in range(50, 151):
    img[i, 50] = 0
    img[i, 100] = 0
img[100, 50:101] = 0

# O
for i in range(50, 151):
    img[i, 120] = 0
    img[i, 170] = 0
img[50, 120:171] = 0
img[150, 120:171] = 0

# L
for i in range(50, 151):
    img[i, 190] = 0
img[150, 190:221] = 0

# A
for i in range(50, 151):
    img[i, 240] = 0
    img[i, 290] = 0
img[50, 240:291] = 0
img[100, 240:291] = 0

# "MUNDO" en la parte inferior
# M
for i in range(250, 351):
    img[i, 50] = 0
    img[i, 100] = 0
for i in range(50):
    img[250 + i, 50 + i] = 0
    img[250 + i, 100 - i] = 0

# U
for i in range(250, 351):
    img[i, 120] = 0
    img[i, 170] = 0
img[350, 120:171] = 0

# N
for i in range(250, 351):
    img[i, 190] = 0
    img[i, 240] = 0
    img[250 + i - 250, 190 + (i - 250)] = 0

# D
for i in range(250, 351):
    img[i, 260] = 0
img[250, 260:291] = 0
img[350, 260:291] = 0
for i in range(25):
    img[275 + i, 290] = 0

# O
for i in range(250, 351):
    img[i, 310] = 0
    img[i, 360] = 0
img[250, 310:361] = 0
img[350, 310:361] = 0

cv.imshow('HOLA MUNDO', img)
cv.waitKey(0)
cv.destroyAllWindows()
