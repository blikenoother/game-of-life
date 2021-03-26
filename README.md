# Game of Life exercise

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.
Rules

At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction

### Run code
  - close the code or download just `game_of_life.py` file
  - `python3 game_of_life.py`

Supported comamnds:
  - if you want to use default grid, just type `default` and it will initialize with default 5 x 10 grid
  - to input own grid value, type `grid 5 10`
  - and then enter each row value, Eg: 0001110000 (here 0 means inactive cell and 1 means live cell)
  - type `next_gen` to generate next generation of cells (you can execute this command multiple time to generate N level of generation)
