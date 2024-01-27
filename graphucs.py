import tkinter as tk
from PIL import Image, ImageTk
import chess
import os
class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.board = chess.Board()
        self.init_ui()
        self.load_images()

    def init_ui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.draw_board()
        # Add more UI components here

    def load_images(self):
        self.images = {}  # Dictionary to store images
        pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
        colors = ['white', 'black']
        base_dir = './data'  # Base directory where images are stored

        for piece in pieces:
            for color in colors:
                path = os.path.join(base_dir, f'{color}_{piece}.png')  # Construct the file path
                image = Image.open(path)
                self.images[f'{color}_{piece}'] = ImageTk.PhotoImage(image)


    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill=color)

        # Add code to place pieces on the board

root = tk.Tk()
gui = ChessGUI(root)
root.mainloop()
