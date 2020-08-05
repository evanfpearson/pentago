from typing import List, Any, Union

from utils import read_config
from game.board import Board
from game.analyser import BoardAnalyser


def main():
    config = read_config('config.yaml')
    game_config = config['game']
    board = Board.blank(game_config['board_size'], game_config['block_size'])
    analyser = BoardAnalyser(board, game_config['win_length'])
    analyser.check_win(1)


if __name__ == "__main__":
    main()
