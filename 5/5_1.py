import time

start = time.time()
f = open('input.txt', 'r')
input = f.read().splitlines()

allLines = []

class Line:
    def __init__(self, cords):
        self.rawCoords = cords
        self.allPoints = []
        self.xPos = []
        self.yPos = []
        self.extractInfo()
        self.myPoints()

    def showCoords(self):
        print(self.rawCoords)

    def extractInfo(self):
        self.xPos = [int(self.rawCoords.split(' -> ')[0].split(',')[0]), int(self.rawCoords.split(' -> ')[1].split(',')[0])]
        self.yPos = [int(self.rawCoords.split(' -> ')[0].split(',')[1]), int(self.rawCoords.split(' -> ')[1].split(',')[1])]

    def myPoints(self):
        if self.xPos[0] == self.xPos[1] or self.yPos[0] == self.yPos[1]:
            if self.xPos[1] >= self.xPos[0]:
                for x in range(self.xPos[0], self.xPos[1] + 1):
                    if self.yPos[1] >= self.yPos[0]:
                        for y in range(self.yPos[0], self.yPos[1] + 1):
                            self.allPoints.append([x, y])
                    elif self.yPos[1] < self.yPos[0]:
                        for y in range(self.yPos[1], self.yPos[0] + 1):
                            self.allPoints.append([x, y])

            elif self.xPos[1] < self.xPos[0]:
                for x in range(self.xPos[1], self.xPos[0] + 1):
                    if self.yPos[1] >= self.yPos[0]:
                        for y in range(self.yPos[0], self.yPos[1] + 1):
                            self.allPoints.append([x, y])
                    elif self.xPos[1] < self.xPos[0]:
                        for y in range(self.yPos[1], self.yPos[0] + 1):
                            self.allPoints.append([x, y])


for i in input:
    if i.split(' -> ')[0].split(',')[0] == i.split(' -> ')[1].split(',')[0] or i.split(' -> ')[0].split(',')[1] == i.split(' -> ')[1].split(',')[1]:
        allLines.append(Line(i))


#for i in range(0, len(allLines)):
#    print(allLines[i].allPoints)

cuts = 0
checkedPoints = []
deadlyPoints = []
for i in allLines:
    for c in i.allPoints:
        if c not in checkedPoints:
            checkedPoints.append(c)
        else:
            if c not in deadlyPoints:
                cuts += 1
                deadlyPoints.append(c)

print('result: ' + str(cuts) + ' in ' + str(time.time() - start))