from game.position import Position


class Placement:
    def __init__(self, block_pos: Position, marble_pos: Position):
        self.__block_pos = block_pos
        self.__marble_pos = marble_pos

    def get_block_pos(self) -> Position:
        return self.__block_pos

    def get_marble_pos(self) -> Position:
        return self.__marble_pos


class Rotation:
    def __init__(self, block_pos: Position, clockwise: bool):
        self.__block_pos = block_pos
        self.__clockwise = clockwise

    def get_block_pos(self):
        return self.__block_pos

    def clockwise(self):
        return self.__clockwise
