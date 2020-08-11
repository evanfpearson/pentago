from copy import deepcopy
from utils import MoveError
from game.block import Block
from game.position import Position
from game.marble import Marble
from game.move import Placement, Rotation
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

    def play_marble(self, pos: Placement, colour: int) -> 'Board':
        block_pos, notch_pos = pos.get_block_pos(), pos.get_marble_pos()
        return self.__update_block(block_pos, self.get_block(block_pos).play(Marble(colour), notch_pos))

    def get_block(self, block_pos: Position) -> Block:
        if block_pos.get_row() < 0 or block_pos.get_column() < 0:
            raise MoveError('use positive notch numbers please')
        try:
            return self.__blocks[block_pos.get_row()][block_pos.get_column()]
        except IndexError:
            raise MoveError('block does not exist')

    @staticmethod
    def blank(board_size, block_size) -> 'Board':
        return Board([[Block.blank(block_size) for _ in range(board_size)] for _ in range(board_size)])

    def rotate_block(self, rotation: Rotation) -> 'Board':
        block_pos = rotation.get_block_pos()
        return self.__update_block(block_pos, self.get_block(block_pos).rotate(rotation.is_clockwise()))

    def __update_block(self, block_pos: Position, new_block: Block) -> 'Board':
        new_blocks = deepcopy(self.__blocks)
        new_blocks[block_pos.get_row()][block_pos.get_column()] = new_block
        return Board(new_blocks)

    # +---+---+---+---+---+---+
    # | O   O   O | O   O   O |
    # | O   O   O | O   O   O |
    # | O   O   O | O   O   O |
    # +---+---+---+---+---+---+
    # | O   O   O | O   O   O |
    # | O   O   O | O   O   O |
    # | O   O   O | O   O   O |
    # +---+---+---+---+---+---+
    def __str__(self):
        h = '+---' * self.get_size() * self.get_block_size() + '+\n'

        def row_string(block_row: int, marble_row: int):
            return '|'.join([block.row_string(marble_row) for block in self.__blocks[block_row]]).join(['|', '|'])

        def block_row_string(block_row: int):
            return '\n'.join([row_string(block_row, marble_row) for marble_row in range(self.get_block_size())]) + '\n'

        return h.join([block_row_string(b) for b in range(self.get_size())]).join([h, h])
