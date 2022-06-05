import argparse
from tkinter import Tk, Canvas

from board import Board

BOARD_SIZE = 1000


def main():
    dimensions, needed_to_win = parse_args()
    root = Tk()
    canvas = Canvas(width=BOARD_SIZE, height=BOARD_SIZE)
    # initialize the board
    Board(root, canvas, BOARD_SIZE, dimensions, needed_to_win)
    root.mainloop()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dimensions', type=int, required=False,
                        help='display the number of squares in a row for the board (n X n)', default=3)
    parser.add_argument("--needed_to_win", type=int, required=False,
                        help='display the number of squares in a row which are needed to win the game', default=3)
    args = parser.parse_args()
    if args.dimensions <= 0:
        raise Exception('dimensions value must be greater than or equal to 0')
    if args.needed_to_win <= 0:
        raise Exception('needed_to_win value must be greater than or equal to 0')
    if args.needed_to_win > args.dimensions:
        raise Exception('needed_to_win value must be less than or equal to dimensions value')
    return args.dimensions, args.needed_to_win


if __name__ == "__main__":
    main()
