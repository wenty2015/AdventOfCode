file = open('day1_1.txt','r')
str = file.read()

stairsUp = str.count('(')
stairsDown = str.count(')')

print(stairsUp - stairsDown)
