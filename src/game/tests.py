import unittest
from game.marble import Marble
from game.notch import Notch
from utils import MoveError
from game.block import Block
from game.position import Position
from game.board import Board
from game.move import Rotation, Placement


class TestMarble(unittest.TestCase):
    def test_get_colour(self):
        colours = [0, 1, 2, 3, None, "hello"]
        for colour in colours:
            self.assertEqual(Marble(colour).get_colour(), colour)


class TestNotch(unittest.TestCase):
    def setUp(self) -> None:
        self.emptyNotch = Notch()
        self.takenNotch = Notch(Marble(1))
        self.test_colour = 0
        self.test_marble = Marble(self.test_colour)

    def test_is_empty(self):
        self.assertFalse(self.takenNotch.is_empty())
        self.assertTrue(self.emptyNotch.is_empty())

    def test_get_colour(self):
        test_notch = self.emptyNotch.play(self.test_marble)
        self.assertEqual(test_notch.get_colour(), self.test_colour)
        self.assertIsNone(self.emptyNotch.get_colour())

    def test_play_raises_error_when_notch_taken(self):
        with self.assertRaises(MoveError):
            self.takenNotch.play(self.test_marble)

    def test_play_raises_error_when_playing_non_marble(self):
        not_a_marble = Notch()
        with self.assertRaises(MoveError):
            self.emptyNotch.play(not_a_marble)


class TestBlock(unittest.TestCase):
    def setUp(self) -> None:
        o = None
        self.test_block = Block.from_int_array([
            [o, o, o],
            [1, 1, 1],
            [0, 1, 0],
        ])

    def test_anticlockwise_rotate(self):
        o = None
        rotated_block = Block.from_int_array([
            [o, 1, 0],
            [o, 1, 1],
            [o, 1, 0],
        ])
        msg = 'rotate anticlockwise not performing as expected'
        self.assertEqual(self.test_block.rotate_anticlockwise(), rotated_block, msg)
        self.assertEqual(self.test_block.
                         rotate_anticlockwise().
                         rotate_anticlockwise().
                         rotate_anticlockwise().
                         rotate_anticlockwise(),
                         self.test_block)

    def test_clockwise_rotate(self):
        o = None
        rotated_block = Block.from_int_array([
            [0, 1, o],
            [1, 1, o],
            [0, 1, o],
        ])
        msg = 'rotate anticlockwise not performing as expected'
        self.assertEqual(self.test_block.rotate_clockwise(), rotated_block, msg)
        self.assertEqual(rotated_block.rotate_anticlockwise().rotate_clockwise(), rotated_block)

    def test_get_notch(self):
        tests = [
            {'pos': Position(0, 0), 'colour': None},
            {'pos': Position(1, 0), 'colour': 1},
            {'pos': Position(1, 2), 'colour': 1},
            {'pos': Position(2, 2), 'colour': 0},
        ]
        for test in tests:
            self.assertEqual(self.test_block.get_notch(test['pos']).get_colour(), test['colour'])

    def test_get_empty_positions(self):
        self.assertEqual(self.test_block.get_empty_positions(), [Position(0, 0), Position(0, 1), Position(0, 2)])

    def test_get_size(self):
        for i in range(1, 10):
            self.assertEqual(Block.blank(i).get_size(), i)


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        o = None
        block00 = Block.from_int_array([[o, o, o], [1, o, o], [1, 1, o]])
        block01 = Block.from_int_array([[o, o, o], [0, 1, o], [1, o, o]])
        block10 = Block.from_int_array([[o, 0, o], [o, o, o], [o, o, o]])
        block11 = Block.from_int_array([[o, o, o], [1, o, o], [1, 1, o]])
        self.test_board = Board([[block00, block01], [block10, block11]])

    def test_get_block_size(self):
        self.assertEqual(self.test_board.get_block_size(), 3)
        for i in range(1, 10):
            self.assertEqual(Board.blank(2, i).get_block_size(), i)

    def test_get_size(self):
        self.assertEqual(self.test_board.get_size(), 2)
        for i in range(1, 10):
            self.assertEqual(Board.blank(i, 3).get_size(), i)

    def test_rotate_block(self):
        o = None
        tests = [
            {'rot': Rotation(Position(0, 0), True), 'new': Block.from_int_array([[1, 1, o], [1, o, o], [o, o, o]])},
            {'rot': Rotation(Position(0, 1), False), 'new': Block.from_int_array([[o, o, o], [o, 1, o], [o, 0, 1]])}
        ]
        for test in tests:
            new_board = self.test_board.rotate_block(test['rot'])
            self.assertEqual(new_board.get_block(test['rot'].get_block_pos()), test['new'])

    def test_play_marble(self):
        o = None
        tests = [
            {
                'move': Placement(Position(0, 0), Position(0, 0)),
                'new': Block.from_int_array([[1, o, o], [1, o, o], [1, 1, o]]),
                'colour': 1
            },
            {
                'move': Placement(Position(0, 1), Position(2, 1)),
                'new': Block.from_int_array([[o, o, o], [0, 1, o], [1, 0, o]]),
                'colour': 0
            }
        ]
        for test in tests:
            new_board = self.test_board.play_marble(test['move'], test['colour'])
            self.assertEqual(new_board.get_block(test['move'].get_block_pos()), test['new'])

    def test_move_error_for_non_extant_block(self):
        rotation_tests = [
            Rotation(Position(100, 100), True),
            Rotation(Position(-1, 0), False),
            Rotation(Position(2, 1), True)
        ]
        placement_tests = [
            Placement(Position(100, 100), Position(2, 2)),
            Placement(Position(-1, 0), Position(2, 2)),
            Placement(Position(2, 1), Position(2, 2))
        ]
        for test in rotation_tests:
            with self.assertRaises(MoveError):
                self.test_board.rotate_block(test)

        for test in placement_tests:
            with self.assertRaises(MoveError):
                self.test_board.play_marble(test, 1)

    def test_move_error_for_non_extant_notch(self):
        placement_tests = [
            Placement(Position(1, 1), Position(3, 2)),
            Placement(Position(0, 0), Position(-1, 2)),
            Placement(Position(0, 1), Position(2, -2))
        ]

        for test in placement_tests:
            with self.assertRaises(MoveError):
                self.test_board.play_marble(test, 1)

