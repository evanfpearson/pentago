import curses

class Cursor:
    def __init__(self, y, x):
        self.__y = y
        self.__x = x

    def move(self, keystroke, m: int) -> 'Cursor':
        if keystroke == curses.KEY_DOWN:
            return Cursor(min(self.__y + 1, m), self.__x)
        elif keystroke == curses.KEY_UP:
            return Cursor(max(self.__y - 1, 0), self.__x)
        elif keystroke == curses.KEY_RIGHT:
            return Cursor(self.__y, min(self.__x + 1, m))
        elif keystroke == curses.KEY_LEFT:
            return Cursor(self.__y, max(self.__x - 1, 0))
        return Cursor(self.__y, self.__x)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
