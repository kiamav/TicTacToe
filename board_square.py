class BoardSquare:
    def __init__(self, x, y, canvas, square_len):
        # x, y corresponds to top left point of the square x,y coords in the canvas
        self.is_filled = False
        self.is_x = True
        self.canvas = canvas
        self.square_len = square_len
        self.offset = self.square_len * 0.1
        self.x1, self.x2, self.y1, self.y2 = self._get_offset_coords(x, y)
        # allows us to map from x_turn to the function to use for drawing shape based on whose turn it is
        self.turn_to_shape = {True: self._draw_x, False: self._draw_circle}

    def _draw_x(self):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, width=5)
        self.canvas.create_line(self.x1, self.y2, self.x2, self.y1, width=5)

    def _draw_circle(self):
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, width=1)

    def _get_offset_coords(self, x, y):
        # gets the offset coordinates for top left and bottom right of the square. where x,y is original top left
        x1 = x + self.offset
        x2 = x + self.square_len - self.offset
        y1 = y + self.offset
        y2 = y + self.square_len - self.offset
        return x1, x2, y1, y2

    def move(self, is_x) -> bool:
        # return if the move is valid or not
        if not self.is_filled:
            self.is_filled = True
            self.is_x = is_x
            self.turn_to_shape[is_x]()
            return True
        return False

