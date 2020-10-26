import pygame, random
from rain import *

## diplay settings
largura, altura = 450, 300
screen = pygame.display.set_mode((largura, altura))
title = pygame.display.set_caption("purple rain from the coding train - IN PYTHON!")

## variables
drops = []
drop_number = 100

for x in range(drop_number):
    random_pos_x = random.randint(0, largura)
    random_pos_y = random.randint(0, altura)
    drops.append(Rain(screen, random_pos_x, random_pos_y))

clock = pygame.time.Clock()
## game loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                
    screen.fill((239, 228, 245))

    # drawinings

    for x in range(drop_number):
        drops[x].draw_rain()
        drops[x].fall()

        
    # display update
    pygame.display.update()