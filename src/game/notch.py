from game.marble import Marble
from utils import MoveError


class Notch:
    SYMBOLS = '○●◍'

    def __init__(self, marble: Marble = None):
        self.__marble = marble

    def play(self, marble) -> 'Notch':
        if isinstance(marble, Marble):
            if self.is_empty():
                return Notch(marble)
            else:
                raise MoveError('this spot is not empty')
        else:
            raise MoveError('only a marble can be played')

    def is_empty(self):
        return self.__marble is None

    def get_colour(self):
        if self.is_empty():
            return None
        else:
            return self.__marble.get_colour()

    def get_symbol(self):
        if self.is_empty():
            return '·'
        else:
            return self.SYMBOLS[self.get_colour()]

    def __eq__(self, other):
        return self.get_colour() == other.get_colour()
