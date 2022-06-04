from board_square import BoardSquare


class Board:
    def __init__(self, canvas, board_size, n):
        self._canvas = canvas
        self._board_size = board_size
        self._n = n
        self._square_len = board_size / self._n
        self._x_turn = True
        self.grid = [[BoardSquare(self._square_len * i, self._square_len * j, self._canvas, self._square_len)
                      for j in range(self._n)] for i in range(self._n)]
        self._draw_board()
        self._canvas.bind('<Button-1>', self.move)

    def _draw_board(self):
        for i in range(1, self._n):
            self._canvas.create_line(self._square_len * i, 0, self._square_len * i, self._board_size, width=5)
            self._canvas.create_line(0, self._square_len * i, self._board_size, self._square_len * i, width=5)
        self._canvas.pack()

    def move(self, event):
        # we get a callback to this method when the left mouse is clicked. the event contains
        # the x,y coord of where was clicked within the canvas
        grid_i = int(event.x // self._square_len)
        grid_j = int(event.y // self._square_len)
        board_square: BoardSquare = self.grid[grid_i][grid_j]
        is_valid_move = board_square.fill_square(self._x_turn)
        if is_valid_move:
            self._x_turn = not self._x_turn
