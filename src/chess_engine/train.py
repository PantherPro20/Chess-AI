import torch
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from src.chess_engine.model import EvaluationNet
from src.chess_engine.utils import board_to_tensor
from src.chess_engine.board import Board
import json
import chess

def train_model(data_file: str, model_path: str, epochs: int, learning_rate: float):
    """
    Trains the neural network on the self-play data.
    """
    # Load the data
    with open(data_file, "r") as f:
        game_data = json.load(f)

    fens, results = zip(*game_data)

    # Convert FENs to tensors
    tensors = torch.cat([board_to_tensor(chess.Board(fen)) for fen in fens])
    results = torch.tensor(results, dtype=torch.float32).unsqueeze(1)

    dataset = TensorDataset(tensors, results)
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    # Initialize the model, loss function, and optimizer
    model = EvaluationNet()
    criterion = torch.nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Training loop
    for epoch in range(epochs):
        for i, (inputs, labels) in enumerate(dataloader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

    # Save the trained model
    torch.save(model.state_dict(), model_path)
    print(f"Model saved to {model_path}")
