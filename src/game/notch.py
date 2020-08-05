from game.marble import Marble
from utils import MoveError


class Notch:
    def __init__(self, marble: Marble):
        self.__marble = marble

    def play(self, marble):
        if isinstance(marble, Marble) and self.is_empty():
            return Notch(marble)
        else:
            raise MoveError('only a marble can be played')

    def is_empty(self):
        return self.__marble is None

    def colour(self):
        if self.is_empty():
            return None
        else:
            return self.__marble.get_colour()