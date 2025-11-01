import chess

class Board:
    """
    A wrapper around the python-chess library's Board class.
    """

    def __init__(self, fen=None):
        if fen:
            self.board = chess.Board(fen)
        else:
            self.board = chess.Board()

    def get_legal_moves(self):
        """
        Returns a list of legal moves.
        """
        return self.board.legal_moves

    def push(self, move):
        """
        Makes a move on the board.
        """
        self.board.push(move)

    def pop(self):
        """
        Takes back the last move.
        """
        return self.board.pop()

    def is_game_over(self):
        """
        Checks if the game is over.
        """
        return self.board.is_game_over()

    def get_fen(self):
        """
        Returns the FEN representation of the board.
        """
        return self.board.fen()

    def __str__(self):
        return str(self.board)
