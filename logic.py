# Tick tac toe
# for the lolz, and learning

class TickToe:
    def __init__(self):
        self.grid = [[" "]*3,[" "]*3,[" "]*3]
        #self.grid = [list(range(0,3)),list(range(3,6)),list(range(6,9))]
        self.whoMove = {'x'}
        self.length = 3
        self.bredth = 3
        self.moves = 0

    def flush(self):
        self.grid = [[" "]*3,[" "]*3,[" "]*3]
        self.whoMove = {'x'}
        self.moves = 0

    def returnWho(self):
        print(self.whoMove, type(self.whoMove))
        return next(iter(self.whoMove))

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

    def genericMove(self,player,location):
        try:
            x = location % self.length
            y = int(location / self.length)
            if self.grid[x][y] == ' ':
                self.grid[x][y] = player
                self.whoMove = {'x','o'} - set(player)
            else:
                return ("The location is already filled",True)
        except (IndexError,ValueError):
                self.whoMove = set(player)
                return ("range is b/w 0-9",True)
        return (self.showGrid(),False)
        self.moves += 1

    def makeMove(self,player,location):
        if self.moves != 9:
            self.genericMove(player,location)
            if self.checkWin(player):
                self.flush()
                return ("{} won the game !!".format(player),False)
            return self.showGrid()
        else:
            self.flush()
            return ("Maximum number of moves reached, it's a tie !",True)

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
    Game.makeMove()
