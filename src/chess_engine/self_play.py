from src.chess_engine.board import Board
from src.chess_engine.search import find_best_move
import json

def play_game(max_depth: int):
    """
    Plays a single game of self-play and returns the game data.
    """
    board = Board()
    game_data = []

    while not board.is_game_over():
        move = find_best_move(board, max_depth)
        board.push(move)
        game_data.append(board.get_fen())

    result = board.board.result()
    if result == "1-0":
        final_result = 1
    elif result == "0-1":
        final_result = -1
    else:
        final_result = 0

    return [(fen, final_result) for fen in game_data]

def generate_data(num_games: int, max_depth: int, output_file: str):
    """
    Generates self-play data and saves it to a file.
    """
    all_game_data = []
    for i in range(num_games):
        print(f"Playing game {i+1}/{num_games}")
        game_data = play_game(max_depth)
        all_game_data.extend(game_data)

    with open(output_file, "w") as f:
        json.dump(all_game_data, f)

    print(f"Generated {len(all_game_data)} positions from {num_games} games.")
