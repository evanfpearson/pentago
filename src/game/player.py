from game.analyser import BoardAnalyser
from game.move import Placement, Rotation
from game.position import Position


def get_string_of_length(n: int, prompt: str):
    move_string = input(prompt)
    while len(move_string) != n:
        print(f'string must be length {n}')
        move_string = input(prompt)
    return move_string


class Player:
    def __init__(self, colour):
        self.__colour = colour

    def get_marble_placement(self, analyser: BoardAnalyser) -> Placement:
        move_instruction = f"""Player {self.__colour}:
        Enter a string of length 4 - For example '0112' - 'rowcolrowcol'
        First couple of characters: The block on which to place the marble
        Second couple of characters: The position to place the marble
        """
        move_string = get_string_of_length(4, move_instruction)

        return Placement(
            block_pos=Position(int(move_string[0]), int(move_string[1])),
            marble_pos=Position(int(move_string[2]), int(move_string[3]))
        )

    def get_rotation(self, analyser: BoardAnalyser) -> Rotation:
        rotation_instruction = """
        Enter a string of length 3 - For example '001' - rotates top left block anticlockwise
        First couple of characters: The block to rotate
        Final character: 0 - anticlockwise, 1 clockwise
        """
        move_string = get_string_of_length(3, rotation_instruction)

        return Rotation(
            block_pos=Position(int(move_string[0]), int(move_string[1])),
            clockwise=bool(int(move_string[2]))
        )

    def get_colour(self):
        return self.__colour
