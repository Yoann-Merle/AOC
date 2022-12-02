#!/usr/bin/python3

org_entry = list(map(int, input().split(",")))
entry = org_entry.copy()

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
        print('i: ' + str(i))
        print('opc: ' + str(opc))
        print('modes: ' + str(modes))
        if int(opc) == 1:
                override(getArg(modes,0, i + 1) + getArg(modes, 1, i + 2), i + 3)
                i += 4
        elif int(opc) == 2:
                override(getArg(modes,0, i + 1) * getArg(modes, 1, i + 2), i + 3)
                i += 4
        elif int(opc) == 3:
                valueToStore = int(input())
                override(valueToStore, i+1)
                i += 2
        elif int(opc) == 4:
                print(str(entry[entry[i+1]]))
                i += 2
        elif int(opc) == 5:
                if getArg(modes, 0, i + 1) != 0:
                        i = getArg(modes, 0, i+2)
                else:
                        i += 3
        elif int(opc) == 6:
                if getArg(modes, 0, i + 1) == 0:
                        i = getArg(modes, 0, i+2)
                else:
                        i += 3
        elif int(opc) == 7:
                if getArg(modes, 0, i + 1) < getArg(modes, 1, i + 2):
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
