#!/usr/bin/env python3

import pygame, time, random
pygame.init()

window = pygame.display.set_mode((500,500))
xr = random.random() * 12
yr = random.random() * 12
x,y = 250,250
cr = 1

while True:
    # time.sleep(0.01)
    pygame.draw.rect(window, (255 - int(cr),x//2,y//2.2), (x,y,10,10))
    pygame.display.update()
    x += xr
    y += yr
    if x < 5 or x > 495:
        xr *= (-1)
    if y < 5 or y > 495:
        yr *= (-1)
        cr += random.random() * 5


