from copy import deepcopy
from game.block import Block
from game.position import Position
from game.marble import Marble
from typing import List


class Board:
    def __init__(self, blocks: List[List[Block]]):
        self.__blocks = blocks

    def get_block_size(self) -> int:
        return self.__blocks[0][0].get_size()

    def get_size(self) -> int:
        return len(self.__blocks[0])

    def get_blocks(self):
        return self.__blocks

    def play_marble(self, pos: Position, colour: int) -> 'Board':
        block_size = self.get_block_size()
        block_pos = Position(pos.get_row() // block_size, pos.get_column() // block_size)
        marble_pos = Position(pos.get_row() % block_size, pos.get_column() % block_size)
        return self.update_block(block_pos, self.get_block(block_pos).play(Marble(colour), marble_pos))

    def get_block(self, block_pos: Position) -> Block:
        return self.__blocks[block_pos.get_row()][block_pos.get_column()]

    @staticmethod
    def blank(board_size, block_size) -> 'Board':
        return Board([[Block.blank(block_size) for _ in range(board_size)] for _ in range(board_size)])

    def update_block(self, block_pos: Position, new_block: Block) -> 'Board':
        new_blocks = deepcopy(self.__blocks)
        new_blocks[block_pos.get_row()][block_pos.get_column()] = new_block
        return Board(new_blocks)
