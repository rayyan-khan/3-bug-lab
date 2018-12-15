import time

neighbors = {'A':['B','a'],'B':['C','b'],'C':['D','c'],'D':['E','d'],'E':['A','e'],'a':['e','A'],'b':['a','B'],'c':['b','C'],'d':['c','D'],'e':['a','E']}

class positionNums():
    positionNumbers = {}
    def __init__(self):
        self.positionNumbers = {n:0 for n in 'ABCDEabcde'}

    def setPosNum(self, position, wtr):
        self.positionNumbers[position] = wtr

    def increment(self, position):
        self.positionNumbers[position] = self.positionNumbers[position]+1

    def getPosNum(self,position):
        return self.positionNumbers[position]

    def getDict(self):
        return self.positionNumbers

class position():
    pos = ''
    level = 0

    def __init__(self, position, level):
        self.level = level
        self.pos = position

    def setLevel(self, level):
        self.level = level

    def getPos(self):
        return self.pos

    def getLevel(self):
        return self.level

def bfs(maxLevel):
    #create dictionary k:v = levels, dictionary of numbers per position
    dictLevels = {n:positionNums() for n in range(1, maxLevel+2)}
    del dictLevels[maxLevel+1]
    parseMe = [position('A', 0)]
    sum = 0
    while sum < 2**(maxLevel+1)-2:
        current = parseMe.pop(0)
        newLevel = current.getLevel()+1
        for k in neighbors[current.getPos()]:
            #increment times reached
            dictLevels[newLevel].increment(k)
            sum += 1
            parseMe.append(position(k,newLevel))
    return dictLevels

def printDictLevels(dictLevels):
    for k in dictLevels:
        print('LEVEL: ', k)
        current = dictLevels[k].getDict()
        for n in current:
            if current[n] != 0:
                print('Position: ', n, ' Ways: ', current[n])

def printDictLevels1(dictLevels):
    dictPositions = {n:[] for n in 'ABCDEabcde'}
    for k in dictLevels:
        current = dictLevels[k].getDict()
        for c in current:
            dictPositions[c].append(current[c])
    for x in dictPositions:
        print(x, ':', dictPositions[x])



printDictLevels1(bfs(10))







