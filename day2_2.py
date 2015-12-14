with open('day2.txt','r') as file:
    array = []
    for line in file:
        array.append(line)

area = 0
i = 0

while i < len(array):
    comb = []

    i1 = array[i].find('x')
    comb.append( int(array[i][0:i1]))
    i2 = array[i].find('x',i1+1)
    comb.append( int(array[i][i1+1:i2]))
    comb.append( int(array[i][i2+1:]))

    comb.sort()
    
    area += comb[0] * comb[1] * comb[2]  + 2 * (comb[0] + comb[1])
    i += 1

print(area)
