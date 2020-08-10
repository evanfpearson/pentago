from game.player import Player
from game.board import Board
from typing import List
from game.analyser import BoardAnalyser
from utils import MoveError


class Game:
    def __init__(self, board: Board, players: List[Player], win_length: int):
        self.__board = board
        self.__players = players
        self.__win_length = win_length

    def play(self):
        player_num = 0
        print(self.__board)
        while True:
            analysis = BoardAnalyser(self.__board)
            while True:
                try:
                    analysis = self.marble_move(player_num, analysis)
                    break
                except MoveError as e:
                    print(e.message)
                    pass
            if analysis.is_over([player_num], self.__win_length):
                print(f"player {analysis.get_winner()} wins")
                return
            while True:
                try:
                    analysis = self.rotation(player_num, analysis)
                    break
                except MoveError as e:
                    print(e.message)
                    pass
            if analysis.is_over([player.get_colour() for player in self.__players], self.__win_length):
                print(f"player {analysis.get_winner()} wins")
                return
            player_num = (player_num + 1) % len(self.__players)

    def marble_move(self, player: int, analysis: BoardAnalyser) -> BoardAnalyser:
        marble_placement = self.__players[player].get_marble_placement(analysis)
        self.update_board(self.__board.play_marble(marble_placement, player))
        print(self.__board)
        return BoardAnalyser(self.__board)

    def rotation(self, player: int, analysis: BoardAnalyser) -> BoardAnalyser:
        rotation = self.__players[player].get_rotation(analysis)
        self.update_board(self.__board.rotate_block(rotation))
        print(self.__board)
        return BoardAnalyser(self.__board)

    def update_board(self, board: Board):
        self.__board = board

