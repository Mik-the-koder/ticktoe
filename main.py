# Tick tac toe
# for the lolz, and learning

class TickToe:
    def __init__(self):
        self.grid = [[" "]*3,[" "]*3,[" "]*3]
        #self.grid = [list(range(0,3)),list(range(3,6)),list(range(6,9))]
        self.length = 3
        self.bredth = 3
        self.moves = 0

    def checkWin(self,Char):
        rightDiagonal = True
        leftDiagonal = True
        topDown = [True]*3
        rightLeft = [True]*3

        # check for diagonals
        # right diagonal
        for i in range(self.length):
            if self.grid[i][i] == Char:
                rightDiagonal = rightDiagonal and True
            else:
                rightDiagonal = rightDiagonal and False

        # left diagonal
        for i in range(self.length):
            if self.grid[i][-(i+1)] == Char:
                leftDiagonal = leftDiagonal and True
            else:
                leftDiagonal = leftDiagonal and False

        # check for top down
        for i in range(self.length):
            for j in range(self.bredth):
                if self.grid[j][i] == Char:
                    topDown[i] = topDown[i] and  True
                else:
                    topDown[i] = topDown[i] and False

        # check for right left
        for i in range(self.length):
            for j in range(self.bredth):
                if self.grid[i][j] == Char:
                    rightLeft[i] = rightLeft[i] and True
                else:
                    rightLeft[j] = rightLeft[i] and False

        # player wins if any one condition is met
        return (rightDiagonal or leftDiagonal or max(topDown) or max(rightLeft))

    def genericMove(self,player):
        LoopVar = True
        while LoopVar:
            self.showGrid()
            try:
                location = int(input("enter the location where you wanna put a '{}':".format(player) ))
                x = location % self.length
                y = int(location / self.length)
                if self.grid[x][y] == ' ':
                    self.grid[x][y] = player
                    LoopVar = False
                else:
                    print("The location is already filled")
                    LoopVar = True
            except (IndexError,ValueError):
                print("range is b/w 0-9")
                LoopVar = True
        self.moves += 1

    def makeMove(self,player):
        if self.moves != 9:
            self.genericMove(player)
            if self.checkWin(player):
                return True         # return True if a player has won
            return self.showGrid()
        else:
            return False            # return False if the game has reached the maximum number of moves possible

    def showGrid(self):
        return self.grid
##        for i in range(self.length):
##            print('\n-----------------\n',end='')
##            for j in range(self.bredth):
##                print(self.grid[i][j], ' | ',end='')
        #print('\n-----------------',end='')
##        print('\n')

if __name__ == "__main__":
    Game = TickToe()
    Game.main()
