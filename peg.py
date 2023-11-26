from copy import deepcopy as copy
import argparse
from animation import draw

class Node():
    def __init__(self, board, jumpfrom = None, jumpover = None, jumpto = None):
        self.board = board
        self.jumpfrom = jumpfrom
        self.jumpover = jumpover
        self.jumpto = jumpto

class peg:
    def __init__(self, start_row, start_col, rule):
        self.size = 5
        self.start_row, self.start_col, self.rule = start_row, start_col, rule
        # board
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[start_row][start_col] = 0
        self.start = Node(copy(self.board))
        # path
        self.path = []
        # Do some initialization work here if you need:
        self.path.append(Node(copy(self.board))) # initialize the list of self.path with a Node

    def draw(self, board):
        if self.success(board):
            draw(self.path, self.start_row, self.start_col, self.rule)
        else:
            print("No solution were found!")

    def success(self, board):
        # your code goes here:
        peng_count = 0
        for row in board:
            for peng in row:
                if peng == 1:
                    peng_count += 1
                    if peng_count > 1:
                        return False
        if peng_count == 1:
            return True

    def available_jumps(self, curr_board):
        available_jumps = []

        current = Node(copy(curr_board)) # deepcopy of the current board

        for row in range(len(current.board)):
            for col in range(row+1):
                if current.board[row][col] == 0: # find where the hole is
                    #check row+1, col+1
                    if 0 <= row + 1 < len(current.board) and 0 <= col + 1 < len(current.board[row + 1]) and \
                            0 <= row + 2 < len(current.board) and 0 <= col + 2 < len(current.board[row + 2]) and \
                            current.board[row + 1][col + 1] == 1 and current.board[row + 2][col + 2] == 1:
                        temp = Node(copy(current.board))  # temporary deepcopy of the current board
                        # change the temporary board
                        temp.board[row+2][col+2] = 0
                        temp.board[row+1][col+1] = 0
                        temp.board[row][col] = 1
                        # change information of the node
                        temp.jumpfrom = (row+2, col+2)
                        temp.jumpover = (row+1, col+1)
                        temp.jumpto = (row,col)
                        available_jumps.append(temp)
                    # check row-1, col-1
                    if 0 <= row - 1 < len(current.board) and 0 <= col - 1 < len(current.board[row - 1]) and \
                            0 <= row - 2 < len(current.board) and 0 <= col - 2 < len(current.board[row - 2]) and \
                            current.board[row - 1][col - 1] == 1 and current.board[row - 2][col - 2] == 1:
                        temp = Node(copy(current.board))  # temporary deepcopy of the current board
                        # change the temporary board
                        temp.board[row-2][col-2] = 0
                        temp.board[row-1][col-1] = 0
                        temp.board[row][col] = 1
                        # change information of the node
                        temp.jumpfrom = (row - 2, col - 2)
                        temp.jumpover = (row - 1, col - 1)
                        temp.jumpto = (row, col)
                        available_jumps.append(temp)
                    # check row+1, col
                    if 0 <= row + 1 < len(current.board) and 0 <= col < len(current.board[row + 1]) and \
                            0 <= row + 2 < len(current.board) and 0 <= col < len(current.board[row + 2]) and \
                            current.board[row + 1][col] == 1 and current.board[row + 2][col] == 1:
                        temp = Node(copy(current.board))  # temporary deepcopy of the current board
                        # change the temporary board
                        temp.board[row+2][col] = 0
                        temp.board[row+1][col] = 0
                        temp.board[row][col] = 1
                        # change information of the node
                        temp.jumpfrom = (row + 2, col)
                        temp.jumpover = (row + 1, col)
                        temp.jumpto = (row, col)
                        available_jumps.append(temp)
                    # check row-1, col
                    if 0 <= row - 1 < len(current.board) and 0 <= col < len(current.board[row - 1]) and \
                            0 <= row - 2 < len(current.board) and 0 <= col < len(current.board[row - 2]) and \
                            current.board[row - 1][col] == 1 and current.board[row - 2][col] == 1:
                        temp = Node(copy(current.board))  # temporary deepcopy of the current board
                        # change the temporary board
                        temp.board[row-2][col] = 0
                        temp.board[row-1][col] = 0
                        temp.board[row][col] = 1
                        # change information of the node
                        temp.jumpfrom = (row - 2, col)
                        temp.jumpover = (row - 1, col)
                        temp.jumpto = (row, col)
                        available_jumps.append(temp)
                    #check row, col+1
                    if 0 <= row < len(current.board) and 0 <= col + 1 < len(current.board[row]) and \
                            0 <= row < len(current.board) and 0 <= col + 2 < len(current.board[row]) and \
                            current.board[row][col + 1] == 1 and current.board[row][col + 2] == 1:
                        temp = Node(copy(current.board))  # temporary deepcopy of the current board
                        # change the temporary board
                        temp.board[row][col+2] = 0
                        temp.board[row][col+1] = 0
                        temp.board[row][col] = 1
                        # change information of the node
                        temp.jumpfrom = (row, col + 2)
                        temp.jumpover = (row, col + 1)
                        temp.jumpto = (row, col)
                        available_jumps.append(temp)
                    # check row, col-1
                    if 0 <= row < len(current.board) and 0 <= col - 1 < len(current.board[row]) and \
                            0 <= row < len(current.board) and 0 <= col - 2 < len(current.board[row]) and \
                            current.board[row][col - 1] == 1 and current.board[row][col - 2] == 1:
                        temp = Node(copy(current.board))  # temporary deepcopy of the current board
                        # change the temporary board
                        temp.board[row][col-2] = 0
                        temp.board[row][col-1] = 0
                        temp.board[row][col] = 1
                        # change information of the node
                        temp.jumpfrom = (row, col - 2)
                        temp.jumpover = (row, col - 1)
                        temp.jumpto = (row, col)
                        available_jumps.append(temp)

        return available_jumps

    def solve(self, board):
        # your code goes here:
        current_board = Node(copy(board)) # copying the board into node

        if self.success(current_board.board):
            return current_board.board

        available_jumps = self.available_jumps(current_board.board)
        for jump in available_jumps:
            self.path.append(jump)
            solution = self.solve(jump.board)
            if solution:
                return solution

                # backtrack board and path
            self.path.pop()
        return False

        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='peg game')

    parser.add_argument('-hole', dest='position', required = True, nargs = '+', type = int, help='initial position of the hole')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='index of rule')

    args = parser.parse_args()

    start_row, start_col = args.position
    if start_row > 4:
        print("row must be less or equal than 4")
        exit()
    if start_col > start_row:
        print("column must be less or equal than row")
        exit()

    # Example: 
    # python peg.py -hole 0 0 -rule 0
    game = peg(start_row, start_col, args.rule)
    final_board = game.solve(game.board)
    game.draw(final_board)
    