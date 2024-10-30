import pygame
pygame.init()

from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.flip()
clock = pygame.time.Clock()

def print_text(message, x, y, font_size, font_color = (0, 0, 0), font_name = None):
    font = pygame.font.Font(font_name, font_size)
    text = font.render(message, True, font_color)
    rect = text.get_rect(center = (x, y))
    screen.blit(text, rect)

class Button:
    def __init__(self, wight, height, inactive_color, active_color, font_size, r = 0):
        self.wight = wight
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font_size = font_size
        self.r = r

    def draw(self, x, y, message, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.wight and y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_color, (x, y, self.wight, self.height), 0, self.r)

                if click[0] == 1:
                    action()

        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.wight, self.height), 0, self.r)

        print_text(message, x + self.wight//2, y + self.height//2, self.font_size)

def points(x, y, font_size, cell_x, sell_y, wight, height):
    pygame.draw.rect(screen, (102, 205, 170), (cell_x, sell_y, wight, height))
    print_text("очки:", x, y, 35, "black")
    print_text(str(point), x, y * 2, 35, "black")
