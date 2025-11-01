from src.chess_engine.board import Board
from src.chess_engine.model import EvaluationNet
from src.chess_engine.utils import board_to_tensor
import torch

# Instantiate the network
net = EvaluationNet()
# Load pre-trained weights if available (we will train it later)
# net.load_state_dict(torch.load("model.pth"))
net.eval()

def evaluate_board(board: Board):
    """
    Evaluates the board using the neural network.
    """
    if board.is_game_over():
        if board.board.result() == "1-0":
            return 1.0
        elif board.board.result() == "0-1":
            return -1.0
        else:
            return 0.0

    tensor = board_to_tensor(board.board)
    with torch.no_grad():
        eval = net(tensor).item()
    return eval

def negamax(board: Board, depth: int, alpha: float, beta: float):
    """
    NegaMax search algorithm with alpha-beta pruning.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    max_eval = float('-inf')
    for move in board.get_legal_moves():
        board.push(move)
        eval = -negamax(board, depth - 1, -beta, -alpha)
        board.pop()
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break
    return max_eval

def find_best_move(board: Board, max_depth: int):
    """
    Finds the best move for the current position using iterative deepening.
    """
    best_move = None
    max_eval = float('-inf')

    for depth in range(1, max_depth + 1):
        alpha = float('-inf')
        beta = float('inf')
        for move in board.get_legal_moves():
            board.push(move)
            eval = -negamax(board, depth - 1, -beta, -alpha)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)

    return best_move
