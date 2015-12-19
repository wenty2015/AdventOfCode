import numpy

## constant
space = ' '
comma = ','

## convert string of position to pos(x,y)
def extractPos(posStr):
    commaN = posStr.find(comma)
    x = int(posStr[:commaN])
    y = int(posStr[commaN+1:])
    return [x,y]

## read file
with open('day6.txt','r') as file:
    array = []
    for line in file:
        tmp = line.replace('turn ','')
        array.append(tmp)

## 0 - off, 1 - on
grid = numpy.zeros((1000,1000))

## process every line
for i in range(0, len(array)):
    str = array[i]
    spaceN = str.find(space)
    cmd = str[:spaceN] ## command

    str = str[spaceN+1:]
    spaceN = str.find(space)
    firstPos = extractPos(str[: spaceN]) ## first position    

    str = str[spaceN+1:]
    spaceN = str.find(space)
    secondPos = extractPos(str[spaceN+1:]) ## second position

    if cmd == 'toggle':
        for x in range(firstPos[0],secondPos[0]):
            for y in range(firstPos[1],secondPos[1]):
                grid[x][y] = 1- grid[x][y]
    else:
        if cmd == 'on':
            l = 1
        else:
            l = 0
        for x in range(firstPos[0],secondPos[0]):
            for y in range(firstPos[1],secondPos[1]):
                grid[x][y] = l
    
print(firstPos[0])
print(secondPos[1])
print(numpy.sum(grid))
print(grid[564][900])

