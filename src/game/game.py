from game.player import Player
from game.board import Board
from typing import List
from game.analyser import BoardAnalyser


class Game:
    def __init__(self, board: Board, players: List[Player], win_length: int):
        self.__board = board
        self.__players = players
        self.__win_length = win_length

    def play(self):
        player = 0
        print(self.__board)
        while True:
            analysis = BoardAnalyser(self.__board)
            analysis = self.marble_move(player, analysis)
            if analysis.check_win([player], self.__win_length):
                print(f"player {analysis.get_winner()} wins")
                return
            analysis = self.rotation(player, analysis)
            analysis.check_win([player.get_colour() for player in self.__players], self.__win_length)
            if analysis.check_win([player], self.__win_length):
                print(f"player {analysis.get_winner()} wins")
                return
            player = (player + 1) % len(self.__players)

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

