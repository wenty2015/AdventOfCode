file = open('day3.txt','r')
str = file.read()

pos = []
strLen = len(str)
i = 0
xS = 0
yS = 0
xR = 0
yR = 0
deltaX = 0
deltaY = 0
    
while i < strLen:
    if str[i] == '^':
        deltaY = 1
    elif str[i] == 'v':
        deltaY= -1
    elif str[i] == '>':
        deltaX = 1
    elif str[i] == '<':
        deltaX = -1

    if i % 2 == 0: ## Santa
        xS += deltaX
        yS += deltaY
        pos.append([xS,yS])
    else: ## Robot
        xR += deltaX
        yR += deltaY
        pos.append([xR,yR])
    
    i += 1
    deltaX = 0
    deltaY = 0

pos.sort()

i = 1
posN = 1
while i < strLen:
    posN += (abs(pos[i][0] - pos[i-1][0]) + abs(pos[i][1] - pos[i-1][1]) > 0) 
    i += 1

print(posN)

