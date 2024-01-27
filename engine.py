import chess

class ChessEngine:
    def __init__(self):
        self.board = chess.Board()

    def list_possible_moves(self):
        return list(self.board.legal_moves)

    def make_move(self, move):
        try:
            chess_move = chess.Move.from_uci(move)
            if chess_move in self.board.legal_moves:
                self.board.push(chess_move)
                return True
            else:
                return False
        except ValueError:
            return False


    def is_checkmate(self):
        return self.board.is_checkmate()

    def is_stalemate(self):
        return self.board.is_stalemate()

    def get_board(self):
        # Returns a copy of the current board state
        return self.board.copy()

    def is_game_over(self):
        # Checks if the game is over
        return self.board.is_game_over()

    def get_game_result(self):
        # Determines the result of the game if it is over
        if self.board.is_checkmate():
            return "checkmate"
        elif self.board.is_stalemate() or self.board.can_claim_draw():
            return "draw"
        else:
            return "undecided"

    def undo_move(self):
        # Undoes the last move made
        if len(self.board.move_stack) > 0:
            self.board.pop()

    def is_player_turn(self):
        return self.board.turn == chess.WHITE

    def get_board_state(self):
        return self.get_board()

    def display_board(self):
        # This method uses python-chess's built-in __str__() method which prints
        # the board in a simple text format. We're going to add ranks and files for clarity.
        board_str = str(self.board).split('\n')
        print('  +--------------------------------+')
        for rank in range(1, 9):
            print(f'{9 - rank} | ' + ' '.join(board_str[rank - 1]) + ' |')
        print('  +--------------------------------+')
        print('    a   b   c   d   e   f   g   h  ')


# Testing the engine
