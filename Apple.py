import random


class Apple:
    def __init__(self):
        self.cords = None

    def is_exists(self):
        return False if self.cords is None else True

    def spawn(self, width, height):
        self.cords = (random.randrange(width), random.randrange(height))
