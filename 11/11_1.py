import time
start = time.time()

#https://adventofcode.com/2021/day/11

input = open('input.txt', 'r').read().splitlines()
allOctos = []

def findOct(x, y):
    for i in allOctos:
        if i.x == x and i.y == y:
            return i

def getAdj(me):
    x = me.x
    y = me.y
    
    adj = []
    adja = []

    adj.append(findOct(x - 1, y - 1))
    adj.append(findOct(x - 1, y))
    adj.append(findOct(x - 1, y + 1))
    adj.append(findOct(x, y - 1))
    adj.append(findOct(x, y + 1))
    adj.append(findOct(x + 1, y - 1))
    adj.append(findOct(x + 1, y))
    adj.append(findOct(x + 1, y + 1))
    
    for o in adj:
        if o != None:
            adja.append(o)
    
    return adja

#hallo


class octo:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.val = int(val)
        self.hasFlashed = False

    def initPlus(self):
        self.val += 1
        self.hasFlashed = False
    
    def plus(self):
        self.val += 1
    
    def flash(self):
        if self.val > 9 and not self.hasFlashed:
            for i in getAdj(self):
                i.plus()
            self.hasFlashed = True
            return True


for y, i in enumerate(input):
    for x, o in enumerate(i):
        oct = octo(x, y, o)
        allOctos.append(oct)

allFlashes = 0

for step in range(0, 100):
    flashes = 0
    #print('step: ', step + 1)
    
    #print(f'{flashes=}')
    for i in allOctos:
        i.initPlus()

    while True:
        s = False
        for i in allOctos:
            if i.flash():
                #print(i.pos)
                flashes += 1
                s = True
        
        if not s:
            break
    
    for i in allOctos:
        if i.hasFlashed:
            i.val = 0
    
    allFlashes += flashes


print(f'{allFlashes=}')
