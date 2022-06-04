from board_square import BoardSquare


class Board:
    def __init__(self, canvas, board_size, n):
        self.canvas = canvas
        self.board_size = board_size
        self.n = n
        self.square_len = board_size / self.n
        self.x_turn = True
        self._init_grid()
        self._draw_board()

    def _draw_board(self):
        for i in range(1, self.n):
            self.canvas.create_line(self.square_len * i, 0, self.square_len * i, self.board_size, width=5)
            self.canvas.create_line(0, self.square_len * i, self.board_size, self.square_len * i, width=5)
        self.canvas.pack()

    def _init_grid(self):
        self.grid = [[BoardSquare(self.square_len*i, self.square_len*j, self.canvas, self.square_len)
                      for j in range(self.n)] for i in range(self.n)]

    def move(self, x, y):
        # place an X or O at x,y coordinate square based on whose turn it is
        grid_i = int(x//self.square_len)
        grid_j = int(y//self.square_len)
        board_square: BoardSquare = self.grid[grid_i][grid_j]
        is_valid_move = board_square.move(self.x_turn)
        if is_valid_move:
            self.x_turn = not self.x_turn
