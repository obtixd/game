import pygame
pygame.init()

from constants import *
from objects import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")
#screen.fill(BACK_COLOR)
#pygame.display.flip()
clock = pygame.time.Clock()

def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                pygame.quit()
                quit()

        screen.blit(BACK_IMAGE, (0, 0))

        button = Button(80, 80, BUTTUN_INACTIVE, BUTTUN_ACTIVE, 40, 40)
        button.draw(40, 396, "pacman")

        pygame.display.update()

def menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                quit()

        screen.fill("pink")


run()