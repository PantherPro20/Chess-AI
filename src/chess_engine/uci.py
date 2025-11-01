from src.chess_engine.engine import Engine

class UCILoop:
    def __init__(self):
        self.engine = Engine()

    def run(self):
        while True:
            line = input()
            if not line:
                continue

            parts = line.split()
            command = parts[0]

            if command == "uci":
                print("id name MyChessEngine")
                print("id author Jules")
                print("uciok")
            elif command == "isready":
                print("readyok")
            elif command == "ucinewgame":
                self.engine = Engine()
            elif command == "position":
                self.handle_position(parts)
            elif command == "go":
                self.handle_go()
            elif command == "quit":
                break

    def handle_position(self, parts):
        if parts[1] == "startpos":
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            moves_start_index = 2
        elif parts[1] == "fen":
            fen = " ".join(parts[2:8])
            moves_start_index = 8
        else:
            return

        self.engine.set_position(fen)

        if len(parts) > moves_start_index and parts[moves_start_index] == "moves":
            for move_str in parts[moves_start_index+1:]:
                self.engine.board.push_san(move_str)


    def handle_go(self):
        best_move = self.engine.find_best_move(3)
        print(f"bestmove {best_move}")

if __name__ == "__main__":
    loop = UCILoop()
    loop.run()
