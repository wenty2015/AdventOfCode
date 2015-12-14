file = open('day3.txt','r')
str = file.read()

pos = []
strLen = len(str)
i = 0
x = 0
y = 0

while i < strLen:
    if str[i] == '^':
        y += 1
    elif str[i] == 'v':
        y -= 1
    elif str[i] == '>':
        x += 1
    elif str[i] == '<':
        x -= 1
    pos.append([x,y])
    i += 1

pos.sort()

i = 1
posN = 1
while i < strLen:
    posN += (abs(pos[i][0] - pos[i-1][0]) + abs(pos[i][1] - pos[i-1][1]) > 0) 
    i += 1

print(posN)

