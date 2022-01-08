f = open('input.txt', 'r')
input = f.read().splitlines()
inputInput = []

rDec = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def decode(rawinput):
    global gotcha
    gotcha = []
    input = []
    for i in rawinput:
        s = []
        for o in i:
            s.append(o)
        input.append(s)

    one = ''
    global two
    two = ''
    global four
    four = ''
    global six
    six = ''
    seven = ''
    global eight
    eight = ''
    global nine
    nine = ''

    output = {}

    for i in input:
        #print(i)
        if len(i) == 2:
            one = i
            #print('one')
        elif len(i) == 4:
            four = i
            #print('four')
        elif len(i) == 3:
            seven = i
            #print('seven')
        elif len(i) == 7:
            eight = i
            #print('eight')

    for i in seven:
        if i not in one:
            output['a'] = i
            gotcha.append(i)


    for i in input:
        no = False
        #print(i)
        if len(i) == 6 and output['a'] in i:
            #print(i)

            for o in four:
                if o not in i:
                    no = True
                    #print(no)
                    break
            
            if not no:
                nine = i
                #print('nine')
                #print(nine)
                break

    for i in eight:
        #print(i)
        #global nine
        if i not in nine:
            output['e'] = i
            gotcha.append(i)

    for o in nine:
        if o not in four and o != output['a']:
            output['g'] = o
            gotcha.append(o)


    for i in input:
        if len(i) == 6 and output['e'] in i and i != nine:
            if one[0] not in i or one[1] not in i:
                six = i
                #print(six)
    
    for i in eight:
        if i not in six:
            output['c'] = i
            gotcha.append(i)

    for i in one:
        if i != output['c']:
            output['f'] = i
            gotcha.append(i)

    for i in input:
        if len(i) == 5 and output['a'] in i and output['c'] in i and output['e'] in i and output['g'] in i and output['f'] not in i:
            two = i
    
    #print(two)

    for i in two:
        if i not in gotcha:
            output['d'] = i
            gotcha.append(i)

    for i in eight:
        if i not in gotcha:
            output['b'] = i

    return {v: k for k, v in output.items()}

def checkLists(x, y):
    if len(x) != len(y):
        return False
    true = 0
    for i in x:
        if i in y:
            true += 1
    
    if true == len(x):
        return True
    return False


rOutput = 0
for line in input:
    num = ''
    dec = decode(line.split(' |')[0].split(' '))
    #print(dec)
    for o in line.split(' | ')[1].split(' '):
        #print('next line')
        num1 = ''
        for l in o[::-1]:
            #print(l)
            num1 += dec[l]

        #print(set(num1))
        for j in rDec:
            #print(set(j))
            #print(num1, j)
            if checkLists(num1, j):
                #print('yes')
                
                num += str(rDec.index(j))
                #print('yes')
                #print(num)
    
    rOutput += int(num)

print(rOutput)