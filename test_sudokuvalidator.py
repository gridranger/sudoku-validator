from unittest import TestCase
from unittest.mock import patch
from sudoku import Sudoku

valid_data = [5, 8, 9, 3, 1, 2, 4, 6, 7,
              7, 6, 1, 4, 9, 8, 2, 3, 5,
              2, 3, 4, 5, 7, 6, 1, 9, 8,
              3, 7, 8, 2, 4, 1, 9, 5, 6,
              4, 5, 2, 6, 8, 9, 3, 7, 1,
              1, 9, 6, 7, 3, 5, 8, 4, 2,
              6, 4, 5, 8, 2, 3, 7, 1, 9,
              9, 2, 3, 1, 5, 7, 6, 8, 4,
              8, 1, 7, 9, 6, 4, 5, 2, 3]

invalid_data = [5, 8, 9, 3, 1, 2, 4, 6, 7,
                7, 6, 1, 4, 9, 8, 2, 3, 5,
                2, 3, 4, 5, 7, 6, 1, 9, 8,
                3, 7, 8, 2, 4, 9, 9, 5, 6,
                4, 5, 2, 6, 8, 9, 3, 7, 1,
                1, 9, 6, 7, 3, 5, 8, 4, 2,
                6, 4, 5, 8, 2, 3, 7, 1, 9,
                9, 2, 3, 1, 5, 7, 6, 8, 4,
                8, 1, 7, 9, 6, 4, 5, 2, 5]


class TestSudokuSolver(TestCase):

    def test_valid_should_pass(self):
        self.assertIsNone(Sudoku.check(valid_data))

    def test_invalid_should_fail(self):
        with self.assertRaises(RuntimeError):
            Sudoku.check(invalid_data)

    @patch("sudoku.Sudoku.check_data_part")
    def test_check_quadrant(self, x):
        Sudoku.check_quadrant(invalid_data, 5)
        x.assert_called_with([9, 5, 6, 3, 7, 1, 8, 4, 2], 5, "quadrant")

    @patch("sudoku.Sudoku.check_data_part")
    def test_check_row(self, x):
        Sudoku.check_row(valid_data, 7)
        x.assert_called_with([9, 2, 3, 1, 5, 7, 6, 8, 4], 7, "row")

    @patch("sudoku.Sudoku.check_data_part")
    def test_check_column(self, x):
        Sudoku.check_column(valid_data, 5)
        x.assert_called_with([2, 8, 6, 1, 9, 5, 3, 7, 4], 5, "column")

