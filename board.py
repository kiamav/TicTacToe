from tkinter import messagebox

from board_square import BoardSquare


class Board:

    LEFT_CLICK_BIND = '<Button-1>'
    TKINTER_DELETE_ALL = 'all'
    TKINTER_QUESTION_YES = 'yes'
    GAME_OVER_TITLE = 'Game Over!'
    TIE_GAME_MESSAGE = 'The game has ended in a tie! Play Another?'
    WINNER_GAME_MESSAGE = 'Congratulations to player {}! You won! Play Another?'
    # maps from direction to relative position.
    # H -> horizontal, V -> vertical
    # / -> diagonal , \ -> other diagonal
    DIRECTION_MAPPINGS = {
        'H': [(1, 0), (-1, 0)],
        'V': [(0, 1), (0, -1)],
        '/': [(1, -1), (-1, 1)],
        '\\': [(1, 1), (-1, -1)]
    }
    PLAYER_TO_MARKER = {True: 'X', False: 'O'}

    def __init__(self, root, canvas, board_size, n, needed_to_win):
        self._root = root
        self._canvas = canvas
        self._board_size = board_size
        self._n = n
        self._needed_to_win = needed_to_win
        self._game_over = False
        self._square_len = board_size / self._n
        self._x_turn = True
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

    def _reset(self):
        self._canvas.delete(self.TKINTER_DELETE_ALL)
        self.__init__(self._root, self._canvas, self._board_size, self._n, self._needed_to_win)

    def _draw_board(self):
        for i in range(1, self._n):
            self._canvas.create_line(self._square_len * i, 0, self._square_len * i, self._board_size, width=5)
            self._canvas.create_line(0, self._square_len * i, self._board_size, self._square_len * i, width=5)
        self._canvas.pack()

    def _check_if_game_won(self, i, j):
        # check if the game has been won by filling the square at i,j
        # do bfs in each of the 4 directions, vertical, horizontal, and both diagonals
        for direction in self.DIRECTION_MAPPINGS:
            game_over, visited = self._bfs(i, j, direction)
            if game_over:
                self._game_over = True
                self._fill_visited_squares(visited)
                self._root.update()
                # we use not self._x_turn because before the call to _check_if_game_won() we switched the _x_turn var
                winner_message = self.WINNER_GAME_MESSAGE.format(self.PLAYER_TO_MARKER[not self._x_turn])
                self._ask_game_over_question(self.GAME_OVER_TITLE, winner_message)

    def _ask_game_over_question(self, title, message):
        if messagebox.askquestion(title, message) == self.TKINTER_QUESTION_YES:
            self._reset()
        else:
            self._root.destroy()

    def _fill_visited_squares(self, visited):
        # color in the winning line
        for i in range(self._n):
            for j in range(self._n):
                if visited[i][j]:
                    self._grid[i][j].fill_square()

    def _check_if_game_tied(self):
        if self._filled_squares == self._n ** 2:
            self._game_over = True
            self._root.update()
            self._ask_game_over_question(self.GAME_OVER_TITLE, self.TIE_GAME_MESSAGE)

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
                    return True, visited
                for d_x, d_y in self.DIRECTION_MAPPINGS[direction]:
                    q.append((i + d_x, j + d_y, direction))
        return False, visited





