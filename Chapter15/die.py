from random import randint


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回一个结果"""
        return randint(1, self.num_sides)
