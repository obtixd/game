import pygame
pygame.init()

import random
import shelve

from constants import *
from objects import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


#ячейки экрана
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, SNAKE_COLOR, (self.x, self.y, CELL_SIZE, CELL_SIZE), 0, 5)

class Apple:
    def __init__(self):
        self.x = random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE)*CELL_SIZE
        self.y = random.randint(1, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE)*CELL_SIZE

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, CELL_SIZE, CELL_SIZE), 0, 5)

class Snake:
    def __init__(self):
        self.cells = [Cell(300, 300), Cell(400, 400)]
        self.direction = "RIGHT"
        self.go_to = self.direction

    def move(self):
        if any((self.go_to == "RIGHT" and not self.direction == "LEFT",
                self.go_to == "LEFT" and not self.direction == "RIGHT",
                self.go_to == "UP" and not self.direction == "DOWN",
                self.go_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.go_to

    def new_head(self, ate_food):
        head = self.cells[0]
        if self.direction == "RIGHT":
            new_head = Cell(head.x + CELL_SIZE, head.y)
        elif self.direction == "LEFT":
            new_head = Cell(head.x - CELL_SIZE, head.y)
        elif self.direction == "UP":
            new_head = Cell(head.x, head.y - CELL_SIZE)
        elif self.direction == "DOWN":
            new_head = Cell(head.x, head.y + CELL_SIZE)

        self.cells.insert(0, new_head)

        if not ate_food:  # удаляем последний элемент если ничег не съел
            self.cells.pop()

    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)

    def check_crash(self):
        head = self.cells[0]
        # столкновение с границами
        if head.x < 0 or head.x >= SCREEN_WIDTH or head.y < 0 or head.y >= SCREEN_HEIGHT:
            return True

        # столкновение ссамой собой
        for i in range(1, len(self.cells)):
            segment = self.cells[i]
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

def run_easy():
    ate_food = False  # съела ли змейка еду

    snake = Snake()
    apple = Apple()
    global point, clock
    point = 0


    running = True
    while running:
        screen.fill(BACK_COLOR)
        points(60, 30, 35, 20, 15, 80, 60)
        print("легкий")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.go_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    snake.go_to = "LEFT"
                elif event.key == pygame.K_UP:
                    snake.go_to = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.go_to = "DOWN"

        head = snake.cells[0]

        if head.x == apple.x and head.y == apple.y:  # проверка на еду
            apple = Apple()
            ate_food = True
            point += 1
        else:
            ate_food = False

        snake.move()
        snake.new_head(ate_food)

        if snake.check_crash():
            running = False
            #pygame.quit()
            #quit()

        snake.draw(screen)
        apple.draw(screen, APPLE_COLOR)
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    return game_over()

def run_classic():
    ate_food = False  # съела ли змейка еду

    snake = Snake()
    apple = Apple()
    global point, clock
    SNAKE_SPEED = 2
    point = 0


    running = True
    while running:
        screen.fill(BACK_COLOR)
        points(40, 30, 35, 3, 20, 80, 60)
        print("обычный")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.go_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    snake.go_to = "LEFT"
                elif event.key == pygame.K_UP:
                    snake.go_to = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.go_to = "DOWN"

        head = snake.cells[0]

        if head.x == apple.x and head.y == apple.y:  # проверка на еду
            apple = Apple()
            ate_food = True
            point += 1
            SNAKE_SPEED += 1
        else:
            ate_food = False

        snake.move()
        snake.new_head(ate_food)

        if snake.check_crash():
            running = False
            # pygame.quit()
            # quit()

        snake.draw(screen)
        apple.draw(screen, APPLE_COLOR)
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    return game_over()

def run_hard():
    ate_food = False  # съела ли змейка еду

    snake = Snake()
    apple = Apple()
    apple_bad1 = Apple()
    apple_bad2 = Apple()
    global point, clock
    point = 0

    running = True
    while running:
        screen.fill(BACK_COLOR)
        points(40, 30, 35, 3, 20, 80, 60)
        print("сложный")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.go_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    snake.go_to = "LEFT"
                elif event.key == pygame.K_UP:
                    snake.go_to = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.go_to = "DOWN"

        head = snake.cells[0]

        if head.x == apple.x and head.y == apple.y:  # проверка на еду
            apple = Apple()
            apple_bad1 = Apple()
            apple_bad2 = Apple()
            ate_food = True
            point += 1
        else:
            ate_food = False

        if (head.x == apple_bad1.x and head.y == apple_bad1.y) or\
                (head.x == apple_bad2.x and head.y == apple_bad2.y):  # проверка на еду
            apple_bad = Apple()
            ate_food = True
            running = False
        else:
            ate_food = False

        snake.move()
        snake.new_head(ate_food)

        if snake.check_crash():
            running = False
            # pygame.quit()
            # quit()

        snake.draw(screen)
        apple.draw(screen, APPLE_COLOR)
        apple_bad1.draw(screen, APPLE_COLOR_BAD)
        apple_bad2.draw(screen, APPLE_COLOR_BAD)
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    return game_over()


def run():
    ITEMS = ['Легкий', 'Классический', 'Сложный']
    ITEMS2 = ['змейка двигается с одной скоростью', 'змейка съедает яблоко и становится быстрее',\
              'съедая темное яблоко змейка умирает']
    fontItem = pygame.font.Font(None, 50)
    fontItemSelect = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 35)
    select = 0
    selectAdd = 0

    global clock

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # play = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selectAdd = -1
                elif event.key == pygame.K_DOWN:
                    selectAdd = 1
                elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if ITEMS[select] == 'Легкий':
                        run_easy()
                    elif ITEMS[select] == 'Классический':
                        run_classic()
                    elif ITEMS[select] == 'Сложный':
                        run_hard()

                select = (select + selectAdd) % len((ITEMS))

                selectAdd = 0

        screen.fill('darkseagreen')

        for i in range(len(ITEMS)):
            if i == select:
                text = fontItemSelect.render(ITEMS[i], 1, (43,27,249))

                text2 = font.render(ITEMS2[i], 1, 'blueviolet')
                rect2 = text2.get_rect(center=(400, 240 + 100 * i))
                screen.blit(text2, rect2)
            else:
                text = fontItem.render(ITEMS[i], 1, 'darkslategray')

            rect = text.get_rect(center=(400, 200 + 100 * i))
            screen.blit(text, rect)

        pygame.display.update()

def menu():
    global clock

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #play = False
                pygame.quit()
                quit()

        screen.fill('darkseagreen')

        b_play = Button(150, 50, (135, 206, 250), (30, 144, 255), 50)
        b_exit = Button(150, 50, (135, 206, 250), (30, 144, 255), 50, pygame.quit())

        b_play.draw(330, 200, "Играть")
        b_play.draw(330, 300, "Выход")
        print_text('SNAKE GAME', 400, 100, 50, "forestgreen")

        pygame.display.update()
        clock.tick(60)

def game_over():
    fontItem = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 35)


    g_m = True
    while g_m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        game_over_text = fontItem.render("GAME OVER", 0, "maroon")
        rect1 = game_over_text.get_rect(center=(400, 200))

        point_text = fontItem.render(str(point), 0, (43,27,249))
        rect2 = point_text.get_rect(center=(540, 250))

        text = fontItem.render("съедено яблок:", 0, (43,27,249))
        rect3 = text.get_rect(center=(380, 250))

        text2 = font.render("чтобы вернуться в меню нажмите Enter", 0, (43,27,249))
        rect4 = text2.get_rect(center=(400, 550))

        screen.fill('darkseagreen')

        screen.blit(game_over_text, rect1)
        screen.blit(point_text, rect2)
        screen.blit(text, rect3)
        screen.blit(text2, rect4)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            menu()

        pygame.display.update()
        clock.tick(70)

while menu():
    pass

pygame.quit()
quit()


