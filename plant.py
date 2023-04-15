import random


class Plant():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.size = random.uniform(1, 6)

    def __str__(self) -> str:
        return f"x:{self.x}    y:{self.y}    size:{self.size}"