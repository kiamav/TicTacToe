from board_square import BoardSquare


class Board:

    LEFT_CLICK_BIND = '<Button-1>'

    def __init__(self, canvas, board_size, n, needed_to_win=3):
        self._canvas = canvas
        self._board_size = board_size
        self._n = n
        self._game_over = False
        self._needed_to_win = needed_to_win
        self._square_len = board_size / self._n
        self._x_turn = True
        self._direction_mappings = {
                                    'H': [(1, 0), (-1, 0)],
                                    'V': [(0, 1), (0, -1)],
                                    '/': [(1, -1), (-1, 1)],
                                    '\\': [(1, 1), (-1, -1)]
                                    }
        self._grid = [[BoardSquare(self._square_len * i, self._square_len * j, self._canvas, self._square_len)
                       for j in range(self._n)] for i in range(self._n)]
        self._draw_board()
        self._canvas.bind(self.LEFT_CLICK_BIND, self.move)
        # keep track of how many squares have been filled in case of tie game
        self._filled_squares = 0

    def move(self, event):
        # we get a callback to this method when the left mouse is clicked. the event contains
        # the x,y coord of where was clicked within the canvas
        if not self._game_over:
            grid_i = int(event.x // self._square_len)
            grid_j = int(event.y // self._square_len)
            board_square: BoardSquare = self._grid[grid_i][grid_j]
            is_valid_move = board_square.place_marker(self._x_turn)
            if is_valid_move:
                self._filled_squares += 1
                self._x_turn = not self._x_turn
                self._check_if_game_won(grid_i, grid_j)
                if not self._game_over:
                    self._check_if_game_tied()

    def _draw_board(self):
        for i in range(1, self._n):
            self._canvas.create_line(self._square_len * i, 0, self._square_len * i, self._board_size, width=5)
            self._canvas.create_line(0, self._square_len * i, self._board_size, self._square_len * i, width=5)
        self._canvas.pack()

    def _check_if_game_won(self, i, j):
        # check if the game has been won by filling the square at i,j
        # do bfs in each of the 4 directions, vertical, horizontal, and both diagonals
        for direction in self._direction_mappings:
            game_over, visited = self._bfs(i, j, direction)
            if game_over:
                self._game_over = True
                self._fill_visited_squares(visited)

    def _fill_visited_squares(self, visited):
        # color in the winning line
        for i in range(self._n):
            for j in range(self._n):
                if visited[i][j]:
                    self._grid[i][j].fill_square()

    def _check_if_game_tied(self):
        if self._filled_squares == self._n ** 2:
            print("THE GAME ENDED IN A TIE!")
            self._game_over = True

    def _bfs(self, i, j, direction):
        # returns whether the game has been won or not
        visited = [[False for _ in range(self._n)] for _ in range(self._n)]
        q = [(i, j, direction)]
        starting_is_x = self._grid[i][j].is_x
        count = 0
        while q:
            i, j, direction = q.pop(0)
            if i < 0 or j < 0 or i >= self._n or j >= self._n or visited[i][j]:
                continue
            if self._grid[i][j].is_filled and self._grid[i][j].is_x == starting_is_x:
                count += 1
                visited[i][j] = True
                if count == self._needed_to_win:
                    print("THE GAME HAS BEEN WON!")
                    return True, visited
                for d_x, d_y in self._direction_mappings[direction]:
                    q.append((i + d_x, j + d_y, direction))
        return False, visited





