# Import your chess engine and AI modules
from engine import ChessEngine
from ai import ChessAI
import chess
# Import any other necessary modules
import os


def main():
    # Initialize your chess engine and AI
    engine = ChessEngine()
    ai = ChessAI()
    # Set up the user interface (if you have one)
    # This could be a command-line interface, a graphical interface, etc.
    
    # Main game loop
    while not engine.is_game_over():
        # Display the current state of the game
        # This might be printing the board to the console, updating a GUI, etc.
        engine.display_board()

        if engine.is_player_turn():
            player_move = get_player_move(engine)
            engine.make_move(player_move)
        else:
            # Use the AI to determine its move
            ai_move = ai.determine_best_move(engine.get_board_state()).uci()
            engine.make_move(ai_move)
        # Check for end-game conditions (checkmate, stalemate, etc.)
        check_game_over_conditions(engine)

    # Game is over - display the result (win/lose/draw)
    display_game_result(engine)

def check_game_over_conditions(engine):
    if engine.is_checkmate():
        print("Checkmate!")
    elif engine.is_stalemate():
        print("Stalemate!")


def display_game_result(engine):
    result = engine.get_game_result()
    if result == "checkmate":
        if engine.board.turn == chess.WHITE:
            print("Black wins by checkmate")
        else:
            print("White wins by checkmate")
    elif result == "draw":
        print("The game is a draw")
    else:
        print("Game is still ongoing")



def get_piece_name(self, piece):
    if piece is None:
        return "Empty"
    piece_names = {
        chess.PAWN: "Pawn",
        chess.KNIGHT: "Knight",
        chess.BISHOP: "Bishop",
        chess.ROOK: "Rook",
        chess.QUEEN: "Queen",
        chess.KING: "King",
    }
    return piece_names.get(piece.piece_type, "Unknown")


def move_to_string(board, move):
    piece = board.piece_at(move.from_square)
    piece_name = piece.symbol().upper() if piece.color == chess.WHITE else piece.symbol()
    return f"{piece_name} to {chess.square_name(move.to_square)}"


def get_player_move(engine):
    while True:
        possible_moves = engine.list_possible_moves()
        print("Your move options include:", [move.uci() for move in possible_moves])
        move = input("Enter your move: ")

        return move


if __name__ == "__main__":
    main()

# Notes
# Add table bases for start and end game.
# Iterative Deepening:
#
# Implement iterative deepening, which iteratively deepens the search depth. This approach allows the engine to use intermediate results to order moves and improve the efficiency of the alpha-beta pruning.
# Move Ordering:
#
# Implement move ordering to examine potentially better moves first. Moves that lead to captures, checks, or promote pawn advancement can be prioritized. This improves the efficiency of the alpha-beta pruning.
# Transposition Table:
#
# Use a transposition table to store previously evaluated positions. If the same position is reached again, the stored evaluation can be used instead of re-evaluating. This is typically implemented with a hash table.
# Quiescence Search:
#
# Implement a quiescence search to handle the horizon effect. Extend the search in positions with pending tactical threats like captures or checks.
# Evaluation Function Improvement:
#
# Enhance the evaluation function to consider more chess-specific factors such as pawn structure, piece mobility, king safety, control of the center, etc.
# Opening Book:
#
# Implement an opening book to use well-established opening moves, saving computation time in the early game.
# Endgame Tablebases:
#
# Use endgame tablebases for perfect play in late-game scenarios with few pieces left.
# ALso an executable
