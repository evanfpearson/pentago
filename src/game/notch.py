from game.marble import Marble
from utils import MoveError


class Notch:
    def __init__(self, marble):
        self.__marble = marble

    def play(self, marble):
        if isinstance(marble, Marble) and self.is_empty():
            return Notch(marble)
        else:
            raise MoveError('only a marble can be played')

    def is_empty(self):
        return self.__marble is None
