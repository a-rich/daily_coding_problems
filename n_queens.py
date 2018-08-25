from __future__ import print_function
import sys

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()

def valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row,N), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQueens(board, col, print_solution=False):
    if col >= N:
        global solutions
        solutions += 1
        if print_solution:
            printSolution(board)
    for row in range(N):
        if valid(board, row, col):
            board[row][col] = 1
            if solveNQueens(board, col+1, print_solution):
                return True
            board[row][col] = 0
    return False

if __name__ == '__main__':
    N, solutions = 4, 0
    board = [[0 for _ in range(N)] for _ in range(N)]

    solveNQueens(board, 0, False)

    if solutions:
        print("{} solutions exist.".format(solutions))
    else:
        print("No solution exists for a {}x{} board.".format(N, N))
