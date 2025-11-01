import unittest
import torch
from src.chess_engine.utils import board_to_tensor
from src.chess_engine.board import Board

class TestUtils(unittest.TestCase):
    def test_board_to_tensor(self):
        board = Board()
        tensor = board_to_tensor(board.board)
        self.assertEqual(tensor.shape, (1, 12, 8, 8))

if __name__ == '__main__':
    unittest.main()
