import unittest
from src.chess_engine.board import Board

class TestBoard(unittest.TestCase):
    def test_initial_position(self):
        board = Board()
        self.assertEqual(board.get_fen(), "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def test_fen_position(self):
        fen = "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2"
        board = Board(fen)
        self.assertEqual(board.get_fen(), fen)

if __name__ == '__main__':
    unittest.main()
