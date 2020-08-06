from utils import read_config
from game.board import Board
from game.game import Game
from game.player import Player


def main():
    config = read_config('config.yaml')
    game_config = config['game']
    board = Board.blank(game_config['board_size'], game_config['block_size'])
    players = [Player(0), Player(1)]
    game = Game(board, players, game_config['win_length'])
    print(board)
    game.play()


if __name__ == "__main__":
    main()
