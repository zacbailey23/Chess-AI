import chess
import random

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
        best_move = chess.Move.null()
        best_value = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            move_value = self.minimax(board, depth-1, float('-inf'), float('inf'), False)
            board.pop()
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move


    def determine_best_move(self, board, depth=3):
        # Finds the best move for the AI at a given board state
        # 'depth' determines how many moves ahead the AI will consider
        return self.find_best_move(board, depth)