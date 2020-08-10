from game.notch import Notch
from game.marble import Marble
from game.position import Position
from utils import MoveError
from copy import deepcopy
from typing import List


class Block:
    def __init__(self, notches: List[List[Notch]]):
        self.__notches = notches

    def get_empty_positions(self) -> List[Position]:
        return [Position(i, j) for i in range(self.get_size()) for j in range(self.get_size()) if self.__notches[i][j].is_empty()]

    def get_size(self) -> int:
        return len(self.__notches[0])

    def get_row(self, row_num: int) -> List[Notch]:
        return self.__notches[row_num]

    def get_notch(self, pos: Position):
        return self.get_row(pos.get_row())[pos.get_column()]

    def row_string(self, row_num):
        return '   '.join([notch.get_symbol() for notch in self.get_row(row_num)]).join([' ', ' '])

    def rotate(self, clockwise: bool) -> 'Block':
        if clockwise:
            return self.rotate_clockwise()
        else:
            return self.rotate_anticlockwise()

    def rotate_clockwise(self) -> 'Block':
        n = self.get_size()
        return Block([[self.__notches[row][col] for row in range(n-1, -1, -1)] for col in range(n)])

    def rotate_anticlockwise(self) -> 'Block':
        n = self.get_size()
        return Block([[self.__notches[row][col] for row in range(n)] for col in range(n-1, -1, -1)])

    def play(self, marble: Marble, pos: Position):
        new_notches = deepcopy(self.__notches)
        if pos.get_row() < 0 or pos.get_column() < 0:
            raise MoveError('use positive notch numbers please')
        try:
            new_notches[pos.get_row()][pos.get_column()] = new_notches[pos.get_row()][pos.get_column()].play(marble)
        except IndexError:
            raise MoveError('notch does not exist')
        return Block(new_notches)

    @staticmethod
    def blank(size) -> 'Block':
        return Block([[Notch(None) for _ in range(size)] for _ in range(size)])

    @staticmethod
    def from_int_array(int_array: List[List[int]]) -> 'Block':
        return Block([[Notch() if i is None else Notch(Marble(i)) for i in row] for row in int_array])

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.get_size() != other.get_size():
            return False
        for row in range(self.get_size()):
            for col in range(self.get_size()):
                pos = Position(row, col)
                if self.get_notch(pos).get_colour() != other.get_notch(pos).get_colour():
                    return False
        return True

