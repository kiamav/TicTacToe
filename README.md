# TicTacToe

This code allows the user to play tic-tac-toe on a NxN board. The default is the standard 3x3 board in which 
3 squares in a row are needed to win the game but the user has the option to specify the size of the board
as well as how many squares are needed in a row to win the game.

### Setup Instructions

1) Install python3 on your machine. I am personally using python3.8 but any python3 version should do. On mac you can run the command below:
```sh
$ brew install python@3.8
```
2) Run the starter.py script and enjoy the game!

The code allows the user the option to specify the board size if he/she chooses.
For the standard 3x3 board which requires 3 squares in a row to win the game simply run the below command:
 ```sh
$ python3 play.py
```
If you wish to specify the board dimensions and the number of squares in a row needed to win, then you can do so via 
the command line. For example, if you wish to play on a 10x10 board and require 4 squares in a row to win, you can run
the command below:
 ```sh
$ python3 play.py --dimensions=10 --needed_to_win=4
```