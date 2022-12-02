#!/usr/bin/python3
import itertools
import time
import sys

class Computer:
        def __init__(self, memory):
                self.entry = memory.copy()
                self.i = 0
                self.opc = ''
                self.relativeBase = 0
                self.modes = [0, 0, 0]
                self.input_= []

        def extractsModes(self):
                if len(str(self.entry[self.i])) <= 5:
                        entryString = (5 - len(str(self.entry[self.i]))) * '0' + str(self.entry[self.i])
                self.modes[0] = int(entryString[2:3])
                self.modes[1] = int(entryString[1:2])
                self.modes[2] = int(entryString[:1])
                return entryString[3:]
                

        def run(self, run_input = []):
                self.input_ += run_input
                while True:
                        entryString = ''
                        opc = self.extractsModes()

                        if int(opc) == 1:
                                self.write(self.getArg(0) + self.getArg(1))
                                self.i += 4

                        elif int(opc) == 2:
                                self.write(self.getArg(0) * self.getArg(1))
                                self.i += 4

                        elif int(opc) == 3:
                                if self.input_ == []:
                                        return 'IND'
                                else:
                                        self.write(int(self.input_.pop(0)), 0)
                                        self.i += 2
                                
                        elif int(opc) == 4:
                                output_ = self.getArg(0)
                                self.i += 2
                                return output_

                        elif int(opc) == 5:
                                if self.getArg(0) != 0:
                                        self.i = self.getArg(1)
                                else:
                                        self.i += 3

                        elif int(opc) == 6:
                                if self.getArg(0) == 0:
                                        self.i = self.getArg(1)
                                else:
                                        self.i += 3
                                        
                        elif int(opc) == 7:
                                if self.getArg(0)  < self.getArg(1):
                                        self.write(1)
                                else:
                                        self.write(0)
                                self.i += 4 

                        elif int(opc) == 8:
                                if self.getArg(0) == self.getArg(1):
                                        self.write(1)
                                else:
                                        self.write(0)
                                self.i += 4       

                        elif int(opc) == 9:
                                self.relativeBase += self.getArg(0)
                                self.i += 2

                        else:
                                return 'EOP'

        def write(self, value, indice = 2):
                try:
                        self.entry[self.getLocationToWrite(indice)] = value
                except Exception:
                        self.extendComp(self.getLocationToWrite(indice))
                        self.entry[self.getLocationToWrite(indice)] = value

        def extendComp(self, indice):
                for i in range(len(self.entry), indice + 1):
                        self.entry.extend([0])
                
        def position(self, place):
                try:
                        return self.entry[self.entry[place]]
                except Exception:
                        self.extendComp(self.entry[place])
                        return self.entry[self.entry[place]]

        def relativePosition(self, num):
                try:
                        return self.entry[self.entry[num] + self.relativeBase]
                except Exception:
                        self.extendComp(self.entry[num] + self.relativeBase)
                        return self.entry[self.entry[num] + self.relativeBase]
        
        def getArg(self, indice):
                if int(self.modes[indice]) == 1:
                        return self.entry[self.i + indice + 1]
                elif int(self.modes[indice]) == 0:
                        return self.position(self.i + indice + 1)
                elif int(self.modes[indice]) == 2:
                        return self.relativePosition(self.i + indice + 1)

        def getLocationToWrite(self, indice):
                if int(self.modes[indice]) == 1:
                        return self.i + indice + 1
                elif int(self.modes[indice]) == 0:
                        try:
                                return self.entry[indice + self.i + 1]
                        except Exception:
                                self.extendComp(indice)
                                return self.entry[indice + self.i + 1]
                                
                elif int(self.modes[indice]) == 2:
                        try:
                                return self.entry[indice + self.i + 1] + self.relativeBase
                        except Exception:
                                self.extendComp(indice)
                                return self.entry[indice + self.i + 1] + self.relativeBase

