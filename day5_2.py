with open('day5.txt','r') as file:
    array = []
    for line in file:
        array.append(line)

niceN = 0;

for i in range(0, len(array)):
    str = array[i]
    twoLetterFlag = 0
    oneLetterFlag = 0

    for j in range(0, len(str)-3):
        sub = str[j:j+2]
        twoLetterFlag = max(str[j+2:].find(sub) >= 0,twoLetterFlag)
        oneLetterFlag = max(str[j] == str[j+2],oneLetterFlag)
        if twoLetterFlag and oneLetterFlag:
            niceN += 1
            break
    if twoLetterFlag and oneLetterFlag:
        continue
    else:
        oneLetterFlag = max(str[j+1] == str[j+1+2],oneLetterFlag)
        if twoLetterFlag and oneLetterFlag:
            niceN += 1

print(niceN)
