#!/usr/bin/python3

org_entry = list(map(int, input('Entry: ').split(",")))

def incrementConf(confsAmp):
    for i in range(5):
        if confsAmp[i] != 4:
            confsAmp[i] += 1
            break
        else:
            confsAmp[i] = 0
def incrementFilter(confsAmp):
    incrementConf(confsAmp)
    for i in confsAmp:
        if confsAmp.count(i) != 1:
            incrementFilter(confsAmp)
            break

def override(value, place):
        entry[entry[place]] = value

def position(num):
        return entry[entry[num]]

def immediate(num):
        return entry[num]

def getArg(modes, indexArg, indice):
        if int(modes[indexArg]) == 1:
                return immediate(indice)
        elif int(modes[indexArg]) == 0:
                return position(indice)
        else:
                print('************************')

def runComp(input1, input2):
    i = 0
    args = ['args1', 'args2', 'args3']
    modes = ['mod1', 'mod2', 'mod3']
    while i <= len(entry) - 3:
            entryString = ''
            if len(str(entry[i])) <= 5:
                    entryString = (5 - len(str(entry[i]))) * '0' + str(entry[i])
    
            opc = entryString[3:]
            modes[0] = entryString[2:3]
            modes[1] = entryString[1:2]
            modes[2] = entryString[:1]
            
            if int(opc) == 1:
                    override(getArg(modes,0, i + 1) + getArg(modes, 1, i + 2), i + 3)
                    i += 4
            elif int(opc) == 2:
                    override(getArg(modes,0, i + 1) * getArg(modes, 1, i + 2), i + 3)
                    i += 4
            elif int(opc) == 3:
                    valueToStore = int(input1)
                    input1 = input2
                    override(valueToStore, i+1)
                    i += 2
            elif int(opc) == 4:
                    return getArg(modes, 0, i+1)
                    i += 2
            elif int(opc) == 5:
                    if getArg(modes, 0, i + 1) != 0:
                            i = getArg(modes, 1, i+2)
                    else:
                            i += 3
            elif int(opc) == 6:
                    if getArg(modes, 0, i + 1) == 0:
                            i = getArg(modes, 1, i+2)
                    else:
                            i += 3
            elif int(opc) == 7:
                    if getArg(modes, 0, i + 1)  < getArg(modes, 1, i + 2):
                            override(1, i+3)
                    else:
                            override(0, i+3)
                    i += 4 
            elif int(opc) == 8:
                    if getArg(modes, 0, i + 1) == getArg(modes, 1, i + 2):
                            override(1, i+3)
                    else:
                            override(0, i+3)
                    i += 4       
            else:
                    break

confsAmp = [4, 3, 2, 1, 0]
max_result = ''
while confsAmp[0] != 0 or confsAmp[1] != 1 or confsAmp[2] != 2 or confsAmp[3] != 3 or confsAmp[4] != 4:
    out = 0
    for c in range(len(confsAmp)):
        entry = org_entry.copy()
        out = runComp(confsAmp[c], out)
        result = out
        if max_result == '' or max_result < result:
            max_result = result
    incrementFilter(confsAmp)
print(str(max_result))
