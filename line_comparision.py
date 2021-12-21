import logging
import math

"""
Author:- Sunanda Shil
Date:- 21-12-21
"""
logging.basicConfig(filename="line_comparision.log", filemode="w")


class Line:
    """
    Class line created for finding the length
    """

    def __init__(self, x1, x2, y1, y2):
        """
        Initialize the attribute
        :param x1:
        :param x2:
        :param y1:
        :param y2:
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate_length(self):
        """
        calculation for finding the length
        :return:
        """
        try:
            length = math.sqrt((self.x2 - self.x1) ^ 2 + (self.y2 - self.y1) ^ 2)
            print(length)
        except Exception:
            logging.exception("Calculation error!!!")


if __name__ == "__main__":

    """
    Creating object for Line class and calling calculation
    """
    try:
        line = Line(2, 4, 2, 4)
        line.calculate_length()
    except Exception:
        logging.exception("Pass the integer value")
