import numpy

with open('day6.txt','r') as file:
    array = []
    for line in file:
        tmp = line.replace('turn ','')
        array.append(tmp)

## 0 - off, 1 - on
grid = numpy.zeros((1000,1000))

## constant
space = ' '

for i in range(0,1):##range(0, len(array)):
    str = array[i]
    spaceN = str.find(space)
    cmd = str[:spaceN] ## command
    
    spaceN = str.find(space,spaceN+1)

    

print(grid.count(1))

