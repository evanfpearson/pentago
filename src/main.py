from utils import read_config
from game.board import Board


def main():
    config = read_config('config.yaml')
    game_config = config['game']
    board = Board.blank(game_config['board_size'], game_config['block_size'])


if __name__ == "__main__":
    main()
