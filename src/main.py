import os
import curses
from game.game import Game
from game.render import render


def main():
    wd, _ = os.path.split(__file__)
    os.chdir(wd)
    game = Game.from_config('config.yaml')
    curses.wrapper(render, game)


if __name__ == "__main__":
    main()
