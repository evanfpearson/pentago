from game.board import Board
from typing import List
from game.notch import Notch


class BoardAnalyser:
    def __init__(self, board: Board, win_length: int):
        self.__board = board
        self.__win_length = win_length

    def get_full_size(self):
        return self.__board.get_size() * self.__board.get_block_size()

    def get_notch_array(self) -> List[List[Notch]]:
        n = self.__board.get_block_size() * self.__board.get_size()
        return [self.get_notch_row(row_num) for row_num in range(n)]

    def get_notch_row(self, row_num) -> List[Notch]:
        block_size = self.__board.get_block_size()
        block_row = row_num // block_size
        marble_row_on_block = row_num % block_size
        return [notch for block in self.__board.get_blocks()[block_row] for notch in block.get_row(marble_row_on_block)]

    def check_win(self, colour: int):
        return any([
            self.__check_vertical_win(colour),
            self.__check_diagonal_win(colour),
            self.__check_horizontal_win(colour)
        ])

    def __check_vertical_win(self, colour: int):
        for col in range(self.get_full_size()):
            for i in range(self.get_full_size() - self.__win_length):
                if all([self.get_notch_array()[row+i][col].colour() == colour for row in range(self.__win_length)]):
                    return True
        return False

    def __check_horizontal_win(self, colour):
        for row in range(self.get_full_size()):
            for i in range(self.get_full_size() - self.__win_length):
                if all([self.get_notch_array()[row][col+i].colour() == colour for col in range(self.__win_length)]):
                    return True
        return False

    def __check_diagonal_win(self, colour):
        n = self.get_full_size()
        w = self.__win_length
        for r_shift in range(n - w):
            for c_shift in range(n - w):
                if any([
                    all([self.get_notch_array()[r_shift+i][c_shift+i].colour() == colour for i in range(w)]),
                    all([self.get_notch_array()[n-r_shift-i-1][n-c_shift-i-1].colour() == colour for i in range(w)])
                ]):
                    return True
        return False
