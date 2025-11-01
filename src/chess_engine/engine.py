from src.chess_engine.board import Board
from src.chess_engine.search import find_best_move
from src.chess_engine.model import EvaluationNet
import torch

class Engine:
    def __init__(self, model_path="model.pth"):
        self.board = Board()
        self.net = EvaluationNet()
        try:
            self.net.load_state_dict(torch.load(model_path))
        except FileNotFoundError:
            print("No model found. Using an untrained network.")
        self.net.eval()

    def set_position(self, fen):
        self.board = Board(fen)

    def find_best_move(self, max_depth):
        return find_best_move(self.board, max_depth)
