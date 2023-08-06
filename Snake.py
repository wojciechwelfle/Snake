class Snake:
    def __init__(self):
        self.head = [0, 0]
        self.parts: list = []
        self.direction = "RIGHT"

    def remove_last_part(self):
        self.parts.remove(self.parts[0])

    def add_new_part(self):
        self.parts.append(self.head)

    def update(self, is_on_apple: bool):
        self.parts.append([self.head[0], self.head[1]])
        if self.direction == "LEFT":
            self.head[0] -= 1
        elif self.direction == "RIGHT":
            self.head[0] += 1
        elif self.direction == "UP":
            self.head[1] -= 1
        elif self.direction == "DOWN":
            self.head[1] += 1
        else:
            self.direction = "RIGHT"
            self.head[0] += 1
        if not is_on_apple:
            self.remove_last_part()
