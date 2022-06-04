class BoardSquare:

    def __init__(self, x, y, canvas, square_len):
        # x, y corresponds to top left point of the square x,y coords in the canvas
        self.is_filled = False
        self.is_x = True
        self._canvas = canvas
        self._square_len = square_len
        self._offset = self._square_len * 0.1
        self._x1, self._x2, self._y1, self._y2 = self._get_offset_coords(x, y)
        # allows us to map from x_turn to the function to use for drawing shape based on whose turn it is
        self._turn_to_shape = {True: self._draw_x, False: self._draw_circle}

    def _draw_x(self):
        self._canvas.create_line(self._x1, self._y1, self._x2, self._y2, width=5)
        self._canvas.create_line(self._x1, self._y2, self._x2, self._y1, width=5)

    def _draw_circle(self):
        self._canvas.create_oval(self._x1, self._y1, self._x2, self._y2, width=1)

    def _get_offset_coords(self, x, y):
        # gets the offset coordinates for top left and bottom right of the square. where x,y is original top left
        x1 = x + self._offset
        x2 = x + self._square_len - self._offset
        y1 = y + self._offset
        y2 = y + self._square_len - self._offset
        return x1, x2, y1, y2

    def fill_square(self, is_x) -> bool:
        # return if the move is valid or not
        if not self.is_filled:
            self.is_filled = True
            self.is_x = is_x
            self._turn_to_shape[is_x]()
            return True
        return False

