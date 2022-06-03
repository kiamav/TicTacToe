from tkinter import *
from board import Board

BOARD_SIZE = 1000
# number of squares in width/length. total num squares is NUM_SQUARES^2
NUM_SQUARES = 3
SQUARE_LEN = BOARD_SIZE / NUM_SQUARES
OFFSET = SQUARE_LEN * 0.1

root = Tk()
canvas = Canvas(width=BOARD_SIZE, height=BOARD_SIZE)
board = Board(canvas, BOARD_SIZE, NUM_SQUARES)


def test_event(event):
	x = event.x
	y = event.y
	top_left_x = x - (x % SQUARE_LEN)
	top_left_y = y - (y % SQUARE_LEN)
	board.move(top_left_x, top_left_y)


canvas.bind('<Button-1>', test_event)
root.mainloop()
