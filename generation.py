import numpy as np
import random


class Cell:

    clue = 0
    mine = False

    def makeMine(self):
        self.mine = True

    def isMine(self):
        return self.mine

    def __str__(self):
        if self.isMine():
            return '*'
        elif self.clue == 0:
            return ' '
        else:
            return str(self.clue)


class State:

    # Currently no guarantee that first cell is safe
    def __init__(self, rows, cols, mineCount):
        # The board is stored as a 1d array, with a 1 cell border
        self.cols = cols
        self.rows = rows
        self.board = [Cell() for c in range((rows+2) * (cols+2))]
        mines = random.sample(range(rows*cols), mineCount)
        mines = list(map(self.fixIndex,mines))
        self.placeMines(mines)
        self.makeClues(mines)
    
    def check(self,row,col):
        return str(self.board[self.fixIndex(col + row * self.cols)])

    # Changes an index to account for boundary cells
    def fixIndex(self, idx):
        x = idx % self.cols
        y = idx // self.cols
        return (x+1) + y * (self.cols+2)

    def placeMines(self, mines):
        for mine in mines:
            self.board[mine].makeMine()

        

    def makeClues(self,mines):
        neighbours = lambda x: [x-(self.cols+2)-1, x-(self.cols+2), x-(self.cols+2)+1,
                                x-1              ,                  x+1,
                                x+(self.cols+2)-1, x+(self.cols+2), x+(self.cols+2)+1]
        for idx in range(self.rows*self.cols):
            if self.fixIndex(idx) not in mines:
                n = neighbours(self.fixIndex(idx))
                count = len([x for x in n if x in mines])
                self.board[self.fixIndex(idx)].clue=count

    def __str__(self):
        # Dumb string method, May want to optimise
        strState = ""
        for y in range(self.rows):
            for x in range(self.cols):
                idx = self.fixIndex(x + y * self.cols)
                strState += str(self.board[idx]) + ' '
            strState += '\n'
        return strState

    def getSize(self):
        return "{} by {}".format(self.rows, self.cols)


if __name__ == "__main__":
    state = State(10, 10, 10)
    # with open("board",'w') as f:
        # f.writelines(str(state))
    print(state)
    print(state.getSize())
