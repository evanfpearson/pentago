class Marble:
    def __init__(self, colour: int):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def __eq__(self, other):
        return self.get_colour() == other.get_colour()
