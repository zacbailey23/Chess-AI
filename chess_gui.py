import tkinter as tk
from PIL import Image, ImageTk
import chess

class ChessGUI:
    def __init__(self, root, engine, ai):
        self.root = root
        self.engine = engine
        self.selected_piece = None
        self.images = {}
        self.load_images()
        self.init_ui()
        self.ai = ai
        self.legal_moves = []

    def load_images(self):
        # Load images for each piece
        pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
        colors = ['white', 'black']
        for color in colors:
            for piece in pieces:
                path = f'Data/{color}_{piece}.png'  # Notice the capital 'D' here
                image = Image.open(path)
                self.images[f'{color}_{piece}'] = ImageTk.PhotoImage(image)

    def init_ui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.draw_board()

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.engine.board.piece_at(chess.square(i, j))
                if piece:
                    # Construct the full name of the piece
                    piece_color = 'white' if piece.color == chess.WHITE else 'black'
                    piece_name = \
                    {chess.PAWN: 'pawn', chess.KNIGHT: 'knight', chess.BISHOP: 'bishop', chess.ROOK: 'rook',
                     chess.QUEEN: 'queen', chess.KING: 'king'}[piece.piece_type]
                    image_key = f'{piece_color}_{piece_name}'
                    # Now use image_key to access the image
                    if image_key in self.images:
                        # Flip the coordinates
                        self.canvas.create_image((7 - i) * 50 + 25, (7 - j) * 50 + 25, image=self.images[image_key])

    def on_square_clicked(self, event):
        # Convert pixel coordinates to chess board coordinates
        print("Click event triggered")  # Add this line

        col, row = (7 - event.y // 50), event.x // 50  # Swap row and col
        square = chess.square(col, row)
        piece = self.engine.board.piece_at(square)

        if self.selected_piece and square in self.legal_moves:
            print ("selected piece")
            # Make the move
            move = chess.Move(self.selected_piece, square)
            self.engine.make_move(move.uci())
            self.selected_piece = None
            self.selected_square = None
            self.legal_moves = []
        elif piece and piece.color == self.engine.board.turn:
            if self.selected_piece is None:
                # Select the piece
                self.selected_piece = square
                self.selected_square = (col, row)
                self.legal_moves = self.get_legal_moves(square)
            else:
                # Deselect the piece
                self.selected_piece = None
                self.selected_square = None
                self.legal_moves = []
        else:
            self.selected_piece = None
            self.selected_square = None
            self.legal_moves = []

        self.draw_board()
        self.check_and_make_ai_move()


    def draw_board(self):
        self.canvas.delete("all")
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 != 0 else "gray"
                # Flip the coordinates
                self.canvas.create_rectangle((7 - i) * 50, j * 50, (7 - i + 1) * 50, (j + 1) * 50, fill=color)
        self.draw_pieces()
        self.highlight_legal_moves()

    def check_and_make_ai_move(self):
        if not self.engine.is_player_turn() and not self.engine.is_game_over():
            ai_move = self.ai.determine_best_move(self.engine.get_board_state())
            self.engine.make_move(ai_move)
            self.draw_board()

    def get_legal_moves(self, square):
        # Convert the square to UCI notation
        square_uci = chess.square_name(square)

        # Get all legal moves for the selected piece
        moves = [move.uci() for move in self.engine.board.legal_moves if
                 chess.square_name(move.from_square) == square_uci]
        return moves

    def highlight_legal_moves(self):
        # Highlight legal moves
        square_uci = chess.square_name(self.selected_piece) if self.selected_piece is not None else None
        for move in self.engine.board.legal_moves:
            if square_uci is None or chess.square_name(move.from_square) == square_uci:
                x, y = chess.square_rank(move.to_square), chess.square_file(move.to_square)
                # Updated calculation for x and y
                self.canvas.create_rectangle(y * 50, (7 - x) * 50, (y + 1) * 50, (7 - x + 1) * 50, outline="blue",
                                             width=2)

    def display_message(self, message):
        # Display a message (like "Checkmate!") to the user
        self.canvas.delete("message")  # Remove previous messages
        self.canvas.create_text(200, 200, text=message, font=("Arial", 24), tags="message", fill="red")

