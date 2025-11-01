import argparse
from src.chess_engine.uci import UCILoop
from src.chess_engine.self_play import generate_data
from src.chess_engine.train import train_model

def main():
    parser = argparse.ArgumentParser(
        description="MyChessEngine: A hybrid chess engine with a NegaMax search and a neural network evaluator.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "mode",
        nargs="?",
        default="play",
        choices=["play", "generate", "train"],
        help="""The mode to run the engine in:
'play'     - Starts the engine in UCI mode to play chess. (Default)
'generate' - Generates self-play game data for training.
'train'    - Trains the neural network on game data."""
    )
    # Arguments for the 'generate' mode
    parser.add_argument("--num-games", type=int, default=10, help="Number of games to generate for training data.")
    parser.add_argument("--depth", type=int, default=2, help="The search depth for the engine during self-play.")

    # Arguments for the 'train' mode
    parser.add_argument("--data-file", type=str, default="game_data.json", help="The file to save/load game data from.")
    parser.add_argument("--model-path", type=str, default="model.pth", help="The file to save/load the trained model from.")
    parser.add_argument("--epochs", type=int, default=10, help="Number of times to loop over the training data.")
    parser.add_argument("--lr", type=float, default=0.001, help="Learning rate for the training process.")


    args = parser.parse_args()

    if args.mode == "play":
        print("Starting engine in UCI mode...")
        loop = UCILoop()
        loop.run()
    elif args.mode == "generate":
        print(f"Generating {args.num_games} games of self-play data...")
        generate_data(num_games=args.num_games, max_depth=args.depth, output_file=args.data_file)
    elif args.mode == "train":
        print(f"Training the model for {args.epochs} epochs...")
        train_model(data_file=args.data_file, model_path=args.model_path, epochs=args.epochs, learning_rate=args.lr)


if __name__ == "__main__":
    main()
