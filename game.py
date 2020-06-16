#!/usr/bin/env python3

import random
import pygame
pygame.init()

max_x = 500
max_y = 500
window = pygame.display.set_mode((max_x, max_y))

pygame.display.set_caption("first game")

x = 50
y = 50
width = 40
height = 60
vel = 2

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - vel

    if keys[pygame.K_RIGHT]:
        x = x + vel

    if keys[pygame.K_UP]:
        y = y - vel

    if keys[pygame.K_DOWN]:
        y = y + vel

    if keys[pygame.K_SPACE]:
        x = random.randint(0, max_x - 200)
        y = random.randint(0, max_y - 200)

    window.fill((0, 0, 0))  # fill with black color
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(window, (0, 255, 0), (100+x, 100+y, width, height))
    pygame.draw.rect(window, (0, 0, 255), (200+x, 200+y, width, height))
    pygame.display.update()

pygame.quit()
