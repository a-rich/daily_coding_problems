import time
import math
import numpy as np
from copy import deepcopy
from random import randint
import matplotlib.pyplot as plt

def plot_board(board):
    new_board = deepcopy(board)
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == '*':
                new_board[i][j] = 1
            else:
                new_board[i][j] = 0

    return new_board

def print_board(board):
    '''Print the matrix of the board state centered around the live cells.'''

    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

def create_board(state):
    '''Returns matrix of cells from STATE, a list of live cell coordinates.'''

    if not state:
        return None

    # Find the boundaries of the board to minimize the number of dead cells
    # that must be rendered.
    min_x, min_y = min([x[0] for x in state]), min([y[1] for y in state])
    max_x, max_y = max([x[0] for x in state]), max([y[1] for y in state])

    # Shift the cell coordinates in the board's state using the calculated
    # minimums.
    for i, (x,y) in enumerate(state):
        state[i] = (x-min_x, y-min_y)

    return [['*' if (x,y) in state else '.' for y in range(max_y+1-min_y)]
            for x in range(max_x+1-min_x)]

def start_life(state, steps):
    '''Play Conway's Game of Life.'''

    def update(state):
        '''Updates the state of the board.'''

        def count_neighbors(i, j, track_dead_cells=False):
            '''For a given cell, count the number of living neighbors.'''

            count = 0
            for x,y in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1),
                    (i+1,j-1), (i+1,j), (i+1,j+1)]:
                try:
                    if x >= 0 and y >= 0 and board[x][y] == '*':
                        count += 1
                    elif track_dead_cells:
                        dead_cells.add((x,y))
                except:
                    if track_dead_cells:
                        dead_cells.add((x,y))

            return count

        dead_cells = set()

        for x,y in list(state):
            live_neighbors = count_neighbors(x, y, True)
            if live_neighbors < 2 or live_neighbors > 3:
                state = [coord for coord in state if coord != (x,y)]

        for x,y in dead_cells:
            if count_neighbors(x,y) == 3:
                state.append((x,y))

        return state

    plt.tick_params(
    axis='both',
    which='both',
    left=False,
    right=False,
    bottom=False,
    top=False,
    labelleft=False,
    labelbottom=False)

    start_steps = steps
    while steps:
        board = create_board(state)

        if not board:
            print('GAME OVER')

        print('Step {}:'.format(start_steps - steps + 1))
        #print_board(board)
        #time.sleep(0.5)
        new_board = plot_board(board)
        if steps == start_steps:
            img = plt.imshow(np.array(new_board), vmin=0, vmax=1)
        else:
            img.set_data(new_board)
        plt.pause(0.5)
        state = update(state)
        steps -= 1

    plt.show(block=False)
    plt.close('all')
    print('GAME OVER')

if __name__ == '__main__':
    steps = 20 # Number of steps for Conway's Game of Life
    n = 200    # Number of live cells to begin with.
    max_size = math.ceil(math.sqrt(n)) + int(n/50)

    # Initialize the state of the board with random live cells.
    state = []
    while len(state) < n:
        coord = (randint(0, max_size), randint(0, max_size))
        if coord not in state:
            state.append(coord)

    # Begin Conway's Game of Life.
    start_life(state, steps)
