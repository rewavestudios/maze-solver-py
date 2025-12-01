import sys
from os import path
import unittest

# Ensure src is importable
sys.path.insert(0, path.join(path.dirname(__file__), 'src'))

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_different_sizes(self):
        cases = [
            (1, 1),
            (2, 3),
            (5, 2),
            (10, 10),
        ]
        for cols, rows in cases:
            with self.subTest(cols=cols, rows=rows):
                m = Maze(0, 0, rows, cols, 5, 7)
                self.assertEqual(len(m._Maze__cells), cols)
                self.assertEqual(len(m._Maze__cells[0]), rows)

    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 3
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        # call the private method via name mangling
        m._Maze__break_entrance_and_exit()
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()
