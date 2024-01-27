import chess
import random
import chess.polyglot
class ChessAI:
    def __init__(self):
        pass

    def evaluate_board(self, board):
        # A simple evaluation function to score the board
        # White pieces are positive, black pieces are negative
        # This is a very naive implementation; you'll want to replace it
        # with something that considers piece positions, control of the center, etc.
        score = 0
        for piece in board.piece_map().values():
            value = {
                chess.PAWN: 1,
                chess.KNIGHT: 3,
                chess.BISHOP: 3,
                chess.ROOK: 5,
                chess.QUEEN: 9,
                chess.KING: 0  # King's value is not considered here
            }.get(piece.piece_type, 0)
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
        return score

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth-1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth-1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self, board, depth):
        piece_symbols = {
            chess.PAWN: 'Pawn',
            chess.KNIGHT: 'Knight',
            chess.BISHOP: 'Bishop',
            chess.ROOK: 'Rook',
            chess.QUEEN: 'Queen',
            chess.KING: 'King'
        }
        try:
            with chess.polyglot.open_reader("./Data/baronbook30/baron30.bin") as reader:
                for entry in reader.find_all(board):
                    print(f"Using opening book move: {entry.move.uci()} with weight {entry.weight}")
                    return entry.move
        except IOError as e:
            print(f"Error opening book: {e}")  # Debug print

        best_move = chess.Move.null()
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        # Sort moves heuristically for better pruning
        sorted_moves = self.sort_moves(board, board.legal_moves)

        for move in sorted_moves:
            board.push(move)
            move_value = self.minimax(board, depth-1, alpha, beta, False)
            board.pop()
            if move_value > best_value:
                best_value = move_value
                best_move = move
            alpha = max(alpha, move_value)

        return best_move

    def sort_moves(self, board, moves):
        # A simple, heuristic move ordering
        captures = [move for move in moves if board.is_capture(move)]
        others = [move for move in moves if not board.is_capture(move)]
        return captures + others  # Prioritize captures

    def determine_best_move(self, board, depth=3):
        # Finds the best move for the AI at a given board state
        # 'depth' determines how many moves ahead the AI will consider
        return self.find_best_move(board, depth)