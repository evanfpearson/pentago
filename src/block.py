class Block:
    def __init__(self, notches):
        self.__notches = notches

    def rotate_anticlockwise(self):
        return Block([self.__notches[(2 - j) + (3 * i)] for j in range(3) for i in range(3)])

    def rotate_clockwise(self):
        return Block([self.__notches[3 * (2 - j) + i] for i in range(3) for j in range(3)])

    def play(self, marble, pos):
        new_notches = [notch for notch in self.__notches]
        new_notches[pos] = new_notches[pos].play(marble)
