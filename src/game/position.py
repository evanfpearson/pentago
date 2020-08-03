# +-----+-----+
# |(0,0)|(0,1)|
# +-----+-----+
# |(r,c)|(1,1)|
# +-----+-----+
# col counts left to right
# row counts top to bottom


class Position:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__col
