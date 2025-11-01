import chess
import torch
import numpy as np

def board_to_tensor(board: chess.Board):
    """
    Converts a chess board to a 12x8x8 tensor.
    """
    tensor = np.zeros((12, 8, 8), dtype=np.float32)
    for i in range(64):
        piece = board.piece_at(i)
        if piece:
            piece_type = piece.piece_type
            color = int(piece.color)
            tensor[piece_type - 1 + 6 * color, i // 8, i % 8] = 1
    return torch.from_numpy(tensor).unsqueeze(0)
