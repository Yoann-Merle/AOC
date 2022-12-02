#!/usr/bin/python3
import itertools

class Computer:
        def __init__(self, _settings, conf):
                self.entry = _settings.copy()
                self.conf = conf
                self.i = 0
        def getConf(self):
                return self.conf

        def run(self, input1):
                args = ['args1', 'args2', 'args3']
                modes = ['mod1', 'mod2', 'mod3']
                while True:
                        entryString = ''
                        if len(str(self.entry[self.i])) <= 5:
                                entryString = (5 - len(str(self.entry[self.i]))) * '0' + str(self.entry[self.i])
                
                        opc = entryString[3:]
                        modes[0] = entryString[2:3]
                        modes[1] = entryString[1:2]
                        modes[2] = entryString[:1]
                        
                        if int(opc) == 1:
                                self.override(self.getArg(modes,0, self.i + 1) + self.getArg(modes, 1, self.i + 2), self.i + 3)
                                self.i += 4
                        elif int(opc) == 2:
                                self.override(self.getArg(modes,0, self.i + 1) * self.getArg(modes, 1, self.i + 2), self.i + 3)
                                self.i += 4
                        elif int(opc) == 3:
                                if self.conf != '':
                                        valueToStore = self.conf
                                        self.conf = ''
                                else:
                                        valueToStore = input1
                                self.override(valueToStore, self.i + 1)
                                self.i += 2
                        elif int(opc) == 4:
                                self.i += 2
                                return self.getArg(modes, 0, self.i - 1)
                        elif int(opc) == 5:
                                if self.getArg(modes, 0, self.i + 1) != 0:
                                        self.i = self.getArg(modes, 1, self.i + 2)
                                else:
                                        self.i += 3
                        elif int(opc) == 6:
                                if self.getArg(modes, 0, self.i + 1) == 0:
                                        self.i = self.getArg(modes, 1, self.i + 2)
                                else:
                                        self.i += 3
                        elif int(opc) == 7:
                                if self.getArg(modes, 0, self.i + 1)  < self.getArg(modes, 1, self.i + 2):
                                        self.override(1, self.i + 3)
                                else:
                                        self.override(0, self.i + 3)
                                self.i += 4 
                        elif int(opc) == 8:
                                if self.getArg(modes, 0, self.i + 1) == self.getArg(modes, 1, self.i + 2):
                                        self.override(1, self.i + 3)
                                else:
                                        self.override(0, self.i + 3)
                                self.i += 4       
                        else:
                                return ''

        def override(self, value, place):
                self.entry[self.entry[place]] = value
        
        def position(self, num):
                return self.entry[self.entry[num]]
        
        def immediate(self, num):
                return self.entry[num]
        
        def getArg(self, modes, indexArg, indice):
                if int(modes[indexArg]) == 1:
                        return self.immediate(indice)
                elif int(modes[indexArg]) == 0:
                        return self.position(indice)

org_entry = list(map(int, input('Entry: ').split(",")))
confsAmp = [5, 6, 7, 8, 9]
max_result = ''
for combinaison in itertools.permutations(confsAmp, 5):
    AllAmp = []
    for conf in combinaison:
        AllAmp.append(Computer(org_entry, conf))

    in_ = 0
    i = 0
    lastResult = ''
    while True:
        out_ = AllAmp[i].run(in_)
        if i == 4:
                lastResult = out_
        if out_ == '':
                break
        in_ = out_
        i = (i + 1) % 5
   
    if max_result == '' or max_result < lastResult:
         max_result = lastResult
         max_combinaison = combinaison

print(str(max_result))
print(str(max_combinaison))
