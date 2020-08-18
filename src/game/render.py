import curses
from game.cursor import Cursor
from game.game import Game
from game.move import Position, Rotation
from utils import MoveError


def render(stdscr, game: Game):
    keystroke = 0
    cursor = Cursor(0, 0)

    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Header and title
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Cursor location

    while keystroke != ord('q'):
        keystroke, game, cursor = render_loop(stdscr, game, keystroke, cursor)


def render_loop(stdscr, game: Game, keystroke: int, cursor: Cursor):
    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    max_cursor = calc_max_cursor(game)
    cursor = cursor.move(keystroke, max_cursor)

    # Draw Title
    draw_centred_title(stdscr, "PENTAGO", width)

    # Draw Menu
    menu_string = f"Press 'q' to quit | row: {cursor.get_y()}, col: {cursor.get_x()} | stage: {game.get_stage()}"
    draw_menu(stdscr, menu_string, width, height)

    if not game.is_over():
        # Handle moves
        game, cursor = handle_move(keystroke, game, cursor)

        # Rotate String
        if game.get_stage() == 1:
            draw_rotate_string(stdscr, game, width)

    if game.is_over():
        draw_winner_string(stdscr, game, width)

    # Draw Board
    draw_centred_board(stdscr, game, width, cursor)

    # Wait for input
    return stdscr.getch(), game, cursor


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


def draw_rotate_string(stdscr, game: Game, screen_width: int):
    rotate_string = "[ - rotate anticlockwise : rotate clockwise - ]"
    whitespace = (screen_width - len(rotate_string)) // 2
    stdscr.addstr(game.draw_height() + 6, whitespace, rotate_string)


def draw_winner_string(stdscr, game, screen_width):
    win_str = f"Player {game.winner()} wins!"
    whitespace = (screen_width - len(win_str)) // 2
    stdscr.addstr(game.draw_height() + 6, whitespace, win_str)


def handle_move(keystroke, game, cursor):
    try:
        if keystroke in (curses.KEY_ENTER, 10, 13):
            if game.get_stage() == 0:
                return game.marble_move(cursor.get_y(), cursor.get_x()), Cursor(cursor.get_y() // game.block_size(), cursor.get_x() // game.block_size())
        if game.get_stage() == 1:
            block_pos = Position(cursor.get_y(), cursor.get_x())
            if keystroke == ord('['):
                return game.choose_block(block_pos).rotate(False), Cursor(0, 0)
            if keystroke == ord(']'):
                return game.choose_block(block_pos).rotate(True), Cursor(0, 0)
        return game, cursor
    except MoveError:
        return game, cursor


def calc_max_cursor(game: Game):
    if game.get_stage() == 0:
        return game.notch_width() - 1
    if game.get_stage() == 1:
        return game.board_size() - 1
    return 1
