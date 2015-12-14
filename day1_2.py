file = open('day1_1.txt','r')
str = file.read()

i = 0
stairs = 0
length = len(str)

while stairs >= 0 and i <= length :
    if str[i] == '(':
        stairs += 1
    else:
        stairs -= 1
    i += 1

if i > length :
    print('never enter the basement')
else:
    print(i)
