from tkinter import *
from board import Board

BOARD_SIZE = 1000
# number of squares in width/length. total num squares is NUM_SQUARES^2
NUM_SQUARES = 3

root = Tk()
canvas = Canvas(width=BOARD_SIZE, height=BOARD_SIZE)
board = Board(canvas, BOARD_SIZE, NUM_SQUARES)


root.mainloop()
