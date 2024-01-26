# main.py

# Import your chess engine and AI modules
from engine import ChessEngine
from ai import ChessAI
import chess
# Import any other necessary modules


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

        if engine.is_player_turn():
            # Get the player's move
            # This might be input from the console, a GUI, etc.
            player_move = get_player_move()
            engine.make_move(player_move)
        else:
            # Use the AI to determine its move
            ai_move = ai.determine_best_move(engine.get_board_state()).uci()
            engine.make_move(ai_move)

        # Check for end-game conditions (checkmate, stalemate, etc.)
        check_game_over_conditions(engine)

    # Game is over - display the result (win/lose/draw)
    display_game_result(engine)


def get_player_move():
    engine.list_possible_moves()
    print("Your move options include ")
    move = input("Enter your move: ")
    return move


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


if __name__ == "__main__":
    main()
