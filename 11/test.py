import time
start = time.time()

input = open('tinput.txt', 'r').read().splitlines()
allOctos = []

def findOct(x, y):
    for i in allOctos:
        if i.x == x and i.y == y:
            return i

def getAdj(input, me):
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

class octo:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.val = int(val)

    def plus(self):
        self.val += 1
    
    def flash(self):
        pass


for y, i in enumerate(input):
    for x, o in enumerate(i):
        oct = octo(x, y, o)
        allOctos.append(oct)

for step in range(0, 10):
    for i in allOctos:
        i.plus()

print('me: ', allOctos[18].pos)

for i in getAdj(input, allOctos[18]):
    print(i.pos)