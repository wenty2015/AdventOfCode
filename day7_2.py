import re

## constant
space = ' '

# operators[] - [x,operator,y]
# variables[] - var
# results[] - result
operators = []
variables = []
results = []

# get the value of requested variable
def getVar(ind,opr = []):
    #print('getVar',variables[resultInd],ind)
    if re.search('[0-9]',opr[ind]) is None: # var is a variable
        return findValue(opr[ind])
    else: # var is a number
        return int(opr[ind])
    
# get the value of stri
def findValue(stri):
    #print('findValue',stri)
    index = variables.index(stri)
    if results[index] is not None: # extract exists result
        return results[index]
    
    if len(operators[index]) == 1:
        result = getVar(0,operators[index])
        #print(index,stri,result)
    else:
        x = getVar(0,operators[index])
        y = getVar(2,operators[index])
        operator = operators[index][1]
        
        if operator == 'AND':
            result = x&y
        elif operator == 'OR':
            result = x|y
        elif operator == 'LSHIFT':
            result = x<<y
        elif operator ==  'RSHIFT':
            result = x>>y
        elif operator ==  'NOT':
            result = ~y

        #print(index,stri,result)
    results[index]=result
    return result

## read file
with open('day7.txt','r') as file:
    array = []
    for line in file:
        tmp = line.replace('NOT','0 NOT')
        tmp = tmp.replace('-> ','')
        tmp = tmp.replace('\n','')
        array.append(tmp)

for i in range(0, len(array)):
    lst = re.split(space,array[i])
    if len(lst) == 2: # statement to var
        index = 1
    else:
        index = 3        
    operators.append(lst[0:index])
    variables.append(lst[index])

results = [None for x in range(len(array))]

stri = 'a'
x = findValue(stri)
print(x)
striB = 'b'
i = variables.index(striB)
operators[i][0] = str(x)

results = [None for x in range(len(array))]
x = findValue(stri)
print(x)
#print(results)
