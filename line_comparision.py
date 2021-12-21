import math


class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate_length(self):
        length = math.sqrt((self.x2 - self.x1) ^ 2 + (self.y2 - self.y1) ^ 2)
        print(length)


if __name__ == "__main__":
    line = Line(2,4,2,4)
    line.calculate_length()

