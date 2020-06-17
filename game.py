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
vel = 5

run = True
isJump = False
jump_count = 10

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x = x - vel

    if keys[pygame.K_RIGHT] and x < max_x - width - vel:
        x = x + vel

    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y = y - vel

        if keys[pygame.K_DOWN] and y < max_y - height - vel:
            y = y + vel

        if keys[pygame.K_RETURN]:  # move to random location when RETURN key pressed 
            x = random.randint(0, max_x - width)
            y = random.randint(0, max_y - height)

        if keys[pygame.K_SPACE]:   # rectangle "jumps"
            isJump = True

    else:
        if jump_count >= -10:
            jump_size = jump_count ** 2 / 2
            if jump_count >= 0:
                y = y - jump_size
            else:
                y = y + jump_size
            jump_count = jump_count - 1
        else:
            isJump=False
            jump_count = 10

    window.fill((0, 0, 0))  # fill with black color
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
#    pygame.draw.rect(window, (0, 255, 0), (100+x, 100+y, width, height))
#    pygame.draw.rect(window, (0, 0, 255), (200+x, 200+y, width, height))
    pygame.display.update()

pygame.quit()
