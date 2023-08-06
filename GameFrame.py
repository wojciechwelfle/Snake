import pygame
from Colors import Colors
from Snake import Snake
from Apple import Apple
import time
from Screen import *


class GameFrame:
    width, height = Screen.get_screen_resolution()
    FRAME_WIDTH = width
    FRAME_HEIGHT = height
    OBJECT_SIZE = 80
    ELEMENTS_IN_HEIGHT = (FRAME_HEIGHT // OBJECT_SIZE)
    ELEMENTS_IN_WIDTH = (FRAME_WIDTH // OBJECT_SIZE)
    FRAME_TITLE = "Snake Game"
    PADDING = 3
    COLORS = Colors
    DELAY = 0.15

    score = 0
    is_running = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(self.FRAME_TITLE)
        self.game_window = pygame.display.set_mode(
            (self.FRAME_WIDTH + self.PADDING, self.FRAME_HEIGHT + self.PADDING))
        self.game()
        self.snake = None
        self.apple = None

    def game(self):
        self.is_running = True
        self.snake = Snake()
        self.apple = Apple()
        self.spawn_new_apple()

        while self.is_running:
            self.check_direction_pressed()
            self.apple_logic()
            self.paint_game()
            self.check_collision()
            time.sleep(self.DELAY)

        pygame.quit()

    def paint_board(self):
        self.game_window.fill(Colors.BLACK)
        for x in range(0, self.FRAME_WIDTH + self.OBJECT_SIZE, self.OBJECT_SIZE):
            length = self.ELEMENTS_IN_HEIGHT * self.OBJECT_SIZE
            pygame.draw.line(self.game_window, Colors.WHITE, (x, 0), (x, length))
        for y in range(0, self.FRAME_HEIGHT + self.OBJECT_SIZE, self.OBJECT_SIZE):
            length = self.ELEMENTS_IN_WIDTH * self.OBJECT_SIZE
            pygame.draw.line(self.game_window, Colors.WHITE, (0, y), (length, y))

    def paint_snake(self, paint_parts: bool):
        size = self.OBJECT_SIZE
        rect = (self.snake.head[0] * size + 1, self.snake.head[1] * size + 1, size - 1, size - 1)
        pygame.draw.rect(self.game_window, Colors.DARK_GREEN, rect)
        if paint_parts:
            for part in self.snake.parts:
                rect = (part[0] * size + 1, part[1] * size + 1, size - 1, size - 1)
                pygame.draw.rect(self.game_window, Colors.GREEN, rect)
                pygame.draw.rect(self.game_window, Colors.random_color(), rect)  # random color body parts

    def paint_apple(self):
        rect = (self.apple.cords[0] * self.OBJECT_SIZE + 1, self.apple.cords[1] * self.OBJECT_SIZE + 1,
                self.OBJECT_SIZE - 1, self.OBJECT_SIZE - 1)
        pygame.draw.rect(self.game_window, Colors.RED, rect)

    def is_on_apple(self):
        return self.apple.cords[0] == self.snake.head[0] and self.apple.cords[1] == self.snake.head[1]

    def is_apple_in_parts(self):
        return self.apple.cords in self.snake.parts

    def check_collision(self):
        if self.snake.head[0] < 0 or self.snake.head[1] < 0:
            self.is_running = False
        if self.snake.head[0] >= self.ELEMENTS_IN_WIDTH:
            self.is_running = False
        if self.snake.head[1] >= self.ELEMENTS_IN_HEIGHT:
            self.is_running = False
        if self.snake.head in self.snake.parts:
            self.is_running = False

    def spawn_new_apple(self):
        while True:
            self.apple.spawn(self.ELEMENTS_IN_WIDTH, self.ELEMENTS_IN_HEIGHT)
            if not self.is_on_apple() and not self.is_apple_in_parts():
                break

    def paint_score(self):
        score_string = f"Score: {self.score}"
        font = pygame.font.Font(None, 50)
        score_text = font.render(score_string, True, Colors.WHITE)
        self.game_window.blit(score_text, (10, 10))

    def paint_game(self):
        self.paint_board()
        self.paint_apple()
        self.paint_snake(True)
        self.paint_score()
        pygame.display.update()

    def check_direction_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.snake.direction = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.snake.direction = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.snake.direction = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.snake.direction = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def apple_logic(self):
        apple = self.is_on_apple()
        self.snake.update(apple)
        if apple:
            self.score += 1
            self.spawn_new_apple()
