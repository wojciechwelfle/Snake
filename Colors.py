import pygame
from random import randint

from pygame import Color


class Colors:
    # Colors (R, G, B, A)
    BLACK: Color = pygame.Color(0, 0, 0)
    WHITE: Color = pygame.Color(255, 255, 255)
    GREEN: Color = pygame.Color(0, 255, 0)
    DARK_GREEN: Color = pygame.Color(0, 128, 0)
    RED: Color = pygame.Color(255, 0, 0)

    @staticmethod
    def random_color() -> Color:
        return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
