from game.player import Player
from utils import read_config
from game.board import Board
from typing import List
from game.move import Rotation, Placement
from game.position import Position
from game.analyser import BoardAnalyser


class Game:
    def __init__(self, board: Board, win_length: int, p_num: int, stage: int, num_players: int, chosen_tile: Position):
        self.__board = board
        self.__win_length = win_length
        self.__player_num = p_num
        self.__stage = stage
        self.__num_players = num_players
        self.__chosen_tile = chosen_tile

    def next_stage(self) -> 'Game':
        next_stage = (self.__stage + 1) % 2  # (0, Marble) (1, Rotate)
        next_player = (self.__player_num + (1 - next_stage)) % self.__num_players
        return Game(self.__board, self.__win_length, next_player, next_stage, self.__num_players, self.__chosen_tile)

    def marble_move(self, row, col) -> 'Game':
        n = self.__board.get_block_size()
        marble_placement = Placement(Position(row // n, col // n), Position(row % n, col % n))
        new_board = self.__board.play_marble(marble_placement, self.__player_num)
        return Game(new_board, self.__win_length, self.__player_num, self.__stage, self.__num_players, self.__chosen_tile).next_stage()

    def rotate(self, clockwise: bool) -> 'Game':
        new_board = self.__board.rotate_block(Rotation(self.__chosen_tile, clockwise))
        return Game(new_board, self.__win_length, self.__player_num, self.__stage, self.__num_players, self.__chosen_tile).next_stage()

    def choose_block(self, block_pos: Position):
        return Game(self.__board, self.__win_length, self.__player_num, self.__stage, self.__num_players, block_pos)

    def is_over(self):
        return BoardAnalyser(self.__board).is_over(list(range(self.__num_players)), self.__win_length)

    def winner(self):
        return BoardAnalyser(self.__board).get_winner(list(range(self.__num_players)), self.__win_length)

    def draw(self, stdscr, top_left_from_top, top_left_from_left, cursor):
        self.__board.draw(stdscr, top_left_from_top, top_left_from_left, cursor, self.__stage)

    def draw_width(self):
        return self.__board.draw_width()

    def draw_height(self):
        return self.__board.draw_height()

    @staticmethod
    def from_config(config_path: str) -> 'Game':
        config = read_config(config_path)
        win_length, block_size, board_size, num_players = \
            config['game']['win_length'], \
            config['game']['block_size'], \
            config['game']['board_size'], \
            config['game']['players']
        board = Board.blank(board_size, block_size)
        return Game(board, win_length, 0, 0, num_players, Position(0, 0))

    def board_size(self):
        return self.__board.get_size()

    def notch_width(self):
        return self.__board.get_size() * self.__board.get_block_size()

    def block_size(self):
        return self.__board.get_block_size()

    def get_stage(self):
        return self.__stage
