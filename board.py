class Board:
    def __init__(self, canvas, board_size, n):
        self.canvas = canvas
        self.board_size = board_size
        self.n = n
        self.square_len = board_size / self.n
        self.offset = self.square_len * 0.1
        self.x_turn = True
        # allows us to map from x_turn to the function to use for drawing shape based on whose turn it is
        self.turn_to_shape = {True: self._draw_x, False: self._draw_circle}
        self._draw_board()

    def _draw_board(self):
        for i in range(1, self.n):
            self.canvas.create_line(self.square_len * i, 0, self.square_len * i, self.board_size, width=5)
            self.canvas.create_line(0, self.square_len * i, self.board_size, self.square_len * i, width=5)
        self.canvas.pack()

    def _draw_x(self, x, y):
        # draws an X in the box with the top left coordinate (x,y)
        x1 = x + self.offset
        x2 = x + self.square_len - self.offset
        y1 = y + self.offset
        y2 = y + self.square_len - self.offset
        self.canvas.create_line(x1, y1, x2, y2, width=5)
        self.canvas.create_line(x1, y2, x2, y1, width=5)

    def _draw_circle(self, x, y):
        # draws an O in the box with the top left coordinate (x,y)
        x1 = x + self.offset
        x2 = x + self.square_len - self.offset
        y1 = y + self.offset
        y2 = y + self.square_len - self.offset
        self.canvas.create_oval(x1, y1, x2, y2, width=1)

    def move(self, x, y):
        self.turn_to_shape[self.x_turn](x, y)
        self.x_turn = not self.x_turn
