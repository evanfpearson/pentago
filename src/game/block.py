from game.notch import Notch
from game.marble import Marble
from game.position import Position
from copy import deepcopy
from typing import List


class Block:
    def __init__(self, notches: List[List[Notch]], size: int):
        self.__notches = notches
        self.__size = size

    def get_empty_positions(self) -> List[Position]:
        return [Position(i, j) for i in range(self.get_size()) for j in range(self.get_size()) if self.__notches[i][j].is_empty()]

    def get_size(self) -> int:
        return self.__size

    def get_row(self, row_num: int) -> List[Notch]:
        return self.__notches[row_num]

    def get_notch(self, pos: Position):
        return self.__notches[pos.get_row()][pos.get_column()]

    def row_string(self, row_num):
        return '   '.join([notch.get_symbol() for notch in self.get_row(row_num)]).join([' ', ' '])

    def rotate(self, clockwise: bool) -> 'Block':
        if clockwise:
            return self.rotate_clockwise()
        else:
            return self.rotate_anticlockwise()

    def rotate_clockwise(self) -> 'Block':
        n = self.get_size()
        return Block([[self.__notches[row][col] for row in range(n-1, -1, -1)] for col in range(n)], n)

    def rotate_anticlockwise(self) -> 'Block':
        n = self.get_size()
        return Block([[self.__notches[row][col] for row in range(n)] for col in range(n-1, -1, -1)], n)

    def play(self, marble: Marble, pos: Position):
        new_notches = deepcopy(self.__notches)
        new_notches[pos.get_row()][pos.get_column()] = new_notches[pos.get_row()][pos.get_column()].play(marble)
        return Block(new_notches, self.__size)

    @staticmethod
    def blank(size):
        return Block([[Notch(None) for _ in range(size)] for _ in range(size)], size)
