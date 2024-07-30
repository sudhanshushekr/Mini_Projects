# play the game 

import random
import re



class Board:
    def __init__(self, dim_size, num_bombs):
        # lets keep track of these parameter . they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board and the helper function

        self.board = self.make_new_board()
        # initialize the set to keep track of which location we covered 
        self.assign_value_to_board
        self.dug = set()
    
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)]for _ in range(self.dim_size)]
        bomb_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size


            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            bombs_planted += 1
        
        return board
    
    # assigning the value to the board

    def assign_value_to_board(self):
        for r  in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[c][r] == '*':
                    continue
                slef.board[r][c] = self.get_num_nabour_bomb(r, c)
    
    # getting the number of mabouring bomb

    def get_num_nabour_bomb(self,row,col):
        num_of_nabouring_bomb = 0
        for r in range(max( 0, row-1), min(self.dim_size - 1 , row+1) + 1):
            for c in range(max(0,col-1) min(self.dim_size(col + 1)) +1):
                if r= row and c = col:
                    # our original location dont check
                    continue
                if self.board[r][c] == '*':
                    num_of_nabouring_bomb += 1
        return num_of_nabouring_bomb

    def dig(self, row, col):
        # dig at that location 
        # return true if it is a sucessfull dig and false if it is an unsucessfull dig 

        self.dug((row, col))
        if self.board[row][col] = '*':
            return False
        if self.board[row][col] > 0:
            return True
        for r in range(max( 0, row-1), min(self.dim_size - 1 , row+1) + 1):
            for c in range(max(0,col-1) min(self.dim_size(col + 1)) +1):
                if (r,c) in self.dug:
                    continue # dont dig if we alrady dig 
                self.dug(,c)
        return True

    def __str__(self):
        visible_board = [[None for _ in range (self.dim_size)] for _ in range (self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if row, col in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '


def play(dim_size = 10, num_bombs = 0):
    
    # creating the board and planting the bomb
    board = board(dim_size, num_bombs)

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)


        user_input = re.split(input("where would you like to dig? input as row, col: "))
        row, col = int(user_input[0], int(user_input[-1]))

        if row <0 or row >= board.dim_size or col > 0  or col >= board.dim_size:
            print("invalid location , Try again")
            continue

        safe = board.dig(row, col)

        if not safe:
            break
        
    if safe:
        print("Congratulation !!! you are victorious !!")
    else:
        print("sorry game over !!")

    board.dug = [(r, c) for r in range (board.dim_size) for c in range (board.dim_size)]
    print(board)

if __name__ = '__main__':
    play()








    pass

