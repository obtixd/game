import pygame
pygame.init()

from constants import *
from objects import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pacman")
#screen.fill(BACK_COLOR)
#pygame.display.flip()
clock = pygame.time.Clock()

def playing():
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                pygame.quit()
                quit()

        screen.fill((255, 105, 180))

        b_play = Button(150, 50, (135, 206, 250), (30, 144, 255), 50)
        b_exit = Button(150, 50, (135, 206, 250), (30, 144, 255), 50)

        b_play.draw(330, 200, "Играть")
        b_play.draw(330, 300, "Выход")
        print_text('PACMAN', 400, 100, 50, "forestgreen")

        pygame.display.update()

def world():

    global pacman_pos

    world = True
    while world:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        old_pos = pacman_pos

        if keys[pygame.K_LEFT]:
            pacman_pos[0] -= pacman_speed
        if keys[pygame.K_RIGHT]:
            pacman_pos[0] += pacman_speed
        if keys[pygame.K_UP]:
            pacman_pos[1] -= pacman_speed
        if keys[pygame.K_DOWN]:
            pacman_pos[1] += pacman_speed

        #for line in range(len(map)):
            #for element in range(len(map[line])):
        if map[old_pos[0]// 25][old_pos[1] // 25] == 1:
            pacman_pos = old_pos

        screen.fill((255, 105, 180))

        for line in range(len(map)):
            for element in range(len(map[line])):
                x = element * CELL_SIZE
                y = line * CELL_SIZE

                if map[line][element] == 1:
                    pygame.draw.rect(screen, "red", (x, y, CELL_SIZE, CELL_SIZE))

        pygame.draw.circle(screen, "YELLOW", (pacman_pos[0], pacman_pos[1]), pacman_size)

        pygame.display.update()
        clock.tick(60)
