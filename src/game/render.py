import curses
from game.cursor import Cursor
from game.game import Game
from game.move import Position, Rotation


def render(stdscr, game: Game):
    keystroke = 0
    cursor = Cursor(0, 0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Header and title
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Cursor location

    while keystroke != ord('q'):
        keystroke, cursor = render_loop(stdscr, game, keystroke, cursor)


def render_loop(stdscr, game: Game, keystroke: int, cursor: Cursor):
    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    cursor = cursor.move(keystroke, 5)

    # Draw Title
    draw_centred_title(stdscr, "PENTAGO", width)

    # Draw Menu
    draw_menu(stdscr, f"Press 'q' to quit | {cursor.get_y()}, {cursor.get_x()}", width, height)

    handle_marble_placement(keystroke, game, cursor)

    # Draw Board
    draw_centred_board(stdscr, game, width, cursor)

    # Wait for input
    return stdscr.getch(), cursor


def draw_centred_title(stdscr, title, screen_width):
    title_whitespace = (screen_width - len(title)) // 2
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(" " * title_whitespace)
    stdscr.addstr(title)
    stdscr.addstr(" " * title_whitespace)
    stdscr.attroff(curses.color_pair(1))


def draw_centred_board(stdscr, game: Game, screen_width: int, cursor: Cursor):
    board_whitespace = (screen_width - game.draw_width()) // 2
    game.draw(stdscr, 3, board_whitespace, cursor)
    stdscr.refresh()


def draw_menu(stdscr, menu_text, screen_width, screen_height):
    left_padding = 2
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(screen_height - 1, 0, " " * left_padding)
    stdscr.addstr(menu_text)
    stdscr.addstr(" " * (screen_width - len(menu_text) - left_padding - 1))
    stdscr.attroff(curses.color_pair(1))


def handle_marble_placement(keystroke, game, cursor):
    if keystroke in (curses.KEY_ENTER, 10, 13):
        game.marble_move(0, cursor.get_y(), cursor.get_x())
