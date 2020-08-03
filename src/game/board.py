from typing import List
from game.block import Block
from game.notch import Notch


class Board:
    def __init__(self, blocks: List[List[Block]], size):
        self.__blocks = blocks
        self.__size = size

    def get_block_size(self):
        return self.__blocks[0][0].get_size()

    def get_size(self):
        return self.__size

    def get_notch_array(self) -> List[Notch]:
        n = self.get_block_size() * self.get_size()
        return [self.get_notch_row(row_num) for row_num in range(n)]

    def get_notch_row(self, row_num) -> List[Notch]:
        block_size = self.get_block_size()
        block_row = row_num // block_size
        marble_row_on_block = row_num % block_size
        return [marble for block in self.__blocks[block_row] for marble in block.get_row(marble_row_on_block)]

    @staticmethod
    def blank(board_size, block_size):
        return Board([[Block.blank(block_size) for _ in range(board_size)] for _ in range(board_size)], board_size)
