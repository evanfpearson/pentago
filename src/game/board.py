from copy import deepcopy
from utils import MoveError
from game.block import Block
from game.position import Position
from game.marble import Marble
from game.move import Placement, Rotation
from game.cursor import Cursor
from typing import List
import curses


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

    # Curses Draw Methods
    def draw(self, stdscr, top_left_from_top: int, top_left_from_left: int, cursor: Cursor, stage: int):
        block_width, block_height = 4 * self.get_block_size(), 2 * self.get_block_size()
        for row_num, row in enumerate(self.get_blocks()):
            for col_num, block in enumerate(row):
                block_cursor = self.get_block_cursor(row_num, col_num, cursor)
                if stage == 1 and cursor.get_y() == row_num and cursor.get_x() == col_num:
                    stdscr.attron(curses.color_pair(2))
                block.draw(stdscr, top_left_from_top + block_height * row_num, top_left_from_left + block_width * col_num, block_cursor, stage)
                if stage == 1 and cursor.get_y() == row_num and cursor.get_x() == col_num:
                    stdscr.attroff(curses.color_pair(2))

    def get_block_cursor(self, block_row, block_col, cursor):
        if (cursor.get_y() // self.get_block_size(), cursor.get_x() // self.get_block_size()) == (block_row, block_col):
            return Cursor(cursor.get_y() % self.get_block_size(), cursor.get_x() % self.get_block_size())
        else:
            return Cursor(-1, -1)

    def draw_width(self):
        return 4 * self.get_block_size() * self.get_size()

    def draw_height(self):
        return 2 * self.get_block_size() * self.get_size()

    # Private Methods
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
        h = ''.join(['+', '--', '---' * self.get_block_size()]) * self.get_size() + '+\n'

        def row_string(block_row: int, marble_row: int):
            return '|'.join([block.row_string(marble_row) for block in self.__blocks[block_row]]).join(['|', '|'])

        def block_row_string(block_row: int):
            blank = '\n'+''.join(['|', '  ', '   ' * self.get_block_size()]) * self.get_size() + '|\n'
            return blank.join([row_string(block_row, marble_row) for marble_row in range(self.get_block_size())]) + '\n'

        return h.join([block_row_string(b) for b in range(self.get_size())]).join([h, h])
