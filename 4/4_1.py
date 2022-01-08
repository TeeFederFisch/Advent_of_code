import time

start = time.time()
f = open('input.txt', 'r')
input = f.read().splitlines()

numbers = input.pop(0).split(',')
input.pop(0)

class Board:
    def __init__(self, list):
        self.rawBoard = list
        self.checkedNums = []
        self.board = []
        self.splitBoard()

    def splitBoard(self):
        someList = []
        self.board = []
        for i in self.rawBoard:
            for o in i.split(' '):
                if o != '':
                    someList.append(o)
            
            self.board.append(someList)
            someList = []
    
    def checkOnWin(self, number):
        self.checkedNums.append(number)
        for i in self.board:
            yes = 0
            for o in i:
                if o in self.checkedNums:
                    yes += 1
            
            if yes == 5:
                return True
            
        for ind in range(0, len(self.board[0])):
            yes = 0
            for i in self.board:
                if i[ind] in self.checkedNums:
                    yes += 1
        
        if yes == 5:
            return True

    def calcPoints(self, num):
        somePoints = 0
        allNums = []
        for i in self.rawBoard:
            for o in i.split(' '):
                if o != '':
                    allNums.append(o)
        
        for i in allNums:
            if i not in self.checkedNums:
                somePoints += int(i)

        return somePoints * int(num)
            
aBoard = []
allBoards = []
for anyRow in input:
    if anyRow == '':
        b = Board(aBoard)
        allBoards.append(b)
        aBoard = []
    else:
        aBoard.append(anyRow)
allBoards.append(Board(aBoard))

won = False
for num in numbers:
    if won == False:
        for board in allBoards:
            if board.checkOnWin(num):
                won = True
                print(board.calcPoints(num))
                print(time.time() - start)
                break