from tkinter import Tk, Canvas
from board import Board

BOARD_SIZE = 1000
# dimensions in width/length. total num squares is DIMENSIONS^2
DIMENSIONS = 3
NEEDED_TO_WIN = 3

root = Tk()
canvas = Canvas(width=BOARD_SIZE, height=BOARD_SIZE)
board = Board(root, canvas, BOARD_SIZE, DIMENSIONS, NEEDED_TO_WIN)
root.mainloop()
