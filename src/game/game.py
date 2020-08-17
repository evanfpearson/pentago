from game.player import Player
from utils import read_config
from game.board import Board
from typing import List
from game.move import Rotation, Placement
from game.position import Position
from game.analyser import BoardAnalyser


class Game:
    def __init__(self, board: Board, players: List[Player], win_length: int):
        self.__board = board
        self.__players = players
        self.__win_length = win_length
        self.__player_num = 0
        self.__stage = 0

    def next_player(self):
        self.__player_num = (self.__player_num + 1) % len(self.__players)
        self.__stage = 0

    def next_stage(self):
        self.__stage = self.__stage + 1

    def marble_move(self, player: int, row, col):
        n = self.__board.get_block_size()
        marble_placement = Placement(Position(row // n, col // n), Position(row % n, col % n))
        self.__update_board(self.__board.play_marble(marble_placement, player))

    def rotation(self, rotation: Rotation):
        self.__update_board(self.__board.rotate_block(rotation))

    def draw(self, stdscr, top_left_from_top, top_left_from_left, cursor):
        self.__board.draw(stdscr, top_left_from_top, top_left_from_left, cursor)

    def draw_width(self):
        return self.__board.draw_width()

    @staticmethod
    def from_config(config_path: str):
        config = read_config(config_path)
        win_length, block_size, board_size = \
            config['game']['win_length'], \
            config['game']['block_size'], \
            config['game']['board_size']
        board = Board.blank(board_size, block_size)
        players = [Player(0), Player(1)]
        return Game(board, players, win_length)

    def __update_board(self, board: Board):
        self.__board = board

