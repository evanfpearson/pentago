from game.notch import Notch
from game.marble import Marble
from game.position import Position
from copy import deepcopy
from typing import List


class Block:
    def __init__(self, notches: List[List[Notch]], size: int):
        self.__notches = notches
        self.__size = size

    def get_size(self) -> int:
        return self.__size

    def get_row(self, row_num: int) -> List[Notch]:
        return self.__notches[row_num]

    def rotate_clockwise(self):
        n = self.get_size()
        return Block([[self.__notches[row][col] for row in range(n, -1, -1)] for col in range(n)], n)

    def rotate_anticlockwise(self):
        n = self.get_size()
        return Block([[self.__notches[row][col] for col in range(n, -1, -1)] for row in range(3)], n)

    def play(self, marble: Marble, pos: Position):
        new_notches = deepcopy(self.__notches)
        new_notches[pos.get_row()][pos.get_column()] = new_notches[pos.get_row()][pos.get_column()].play(marble)
        return Block(new_notches, self.__size)

    @staticmethod
    def blank(size):
        return Block([[Notch(None) for _ in range(size)] for _ in range(size)], size)
