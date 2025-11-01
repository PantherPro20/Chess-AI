import unittest
from src.chess_engine.board import Board
from src.chess_engine.search import find_best_move
import chess

class TestSearch(unittest.TestCase):
    def test_find_best_move(self):
        # A position where the best move is obvious
        fen = "rnbqkbnr/pppp1ppp/8/4p3/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
        board = Board(fen)
        move = find_best_move(board, 1)
        self.assertIsInstance(move, chess.Move)

if __name__ == '__main__':
    unittest.main()
