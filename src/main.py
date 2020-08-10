import os
from utils import read_config
from game.board import Board
from game.game import Game
from game.player import Player


def main():
    wd, _ = os.path.split(__file__)
    os.chdir(wd)
    config = read_config('config.yaml')
    win_length, block_size, board_size = \
        config['game']['win_length'], \
        config['game']['block_size'], \
        config['game']['board_size']
    board = Board.blank(board_size, block_size)
    players = [Player(0), Player(1)]
    game = Game(board, players, win_length)
    game.play()


if __name__ == "__main__":
    main()
