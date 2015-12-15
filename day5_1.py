with open('day5.txt','r') as file:
    array = []
    for line in file:
        array.append(line)

niceN = 0;

for i in range(0, len(array)):
    str = array[i]
    vowelN = str.count('a') + str.count('e') + str.count('i') +  str.count('o') + str.count('u')
    nonNaughtyFlay = str.find('ab') < 0 and str.find('cd') < 0 and str.find('pq') < 0 and str.find('xy') < 0

    if vowelN >= 3 and nonNaughtyFlay:
        tmps = sorted(str)
        for j in range(1, len(str)):
            if str[j] == str[j-1]:
                niceN += 1
                break

print(niceN)
