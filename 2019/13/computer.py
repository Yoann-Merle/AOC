#!/usr/bin/python3
import itertools
import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

class Computer:
        def __init__(self, _settings):
                self.entry = _settings.copy()
                self.i = 0
                self.opc = ''
                self.relativeBase = 0
                self.modes = [0, 0, 0]

        def extractsModes(self):
                if len(str(self.entry[self.i])) <= 5:
                        entryString = (5 - len(str(self.entry[self.i]))) * '0' + str(self.entry[self.i])
                self.modes[0] = int(entryString[2:3])
                self.modes[1] = int(entryString[1:2])
                self.modes[2] = int(entryString[:1])
                return entryString[3:]
                

        def run(self, input1 = ''):
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
                                if input1 == '':
                                        return 'IND'
                                else:
                                        self.write(int(input1), 0)
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

def paint(point, color, paintBlack, paintWhite):
        if color == 0:
                paintBlack.add(point)
                if point in paintWhite:
                        paintWhite.remove(point)
        else:
                paintWhite.add(point)
                if point in paintBlack:
                        paintBlack.remove(point)
        return point, paintBlack, paintWhite

def move(location, orient, angle):
        compass = ['up', 'right', 'down', 'left'] 
        if angle == 0:
                orient = compass[(compass.index(orient) + 1) % 4]
        else:
                orient = compass[(compass.index(orient) - 1) % 4]

        if orient == 'up':
                location = (location[0], location[1] + 1)
        if orient == 'down':
                location = (location[0], location[1] - 1)
        if orient == 'left':
                location = (location[0] - 1, location[1])
        if orient == 'right':
                location = (location[0] + 1, location[1])
        return location, orient
def clean(nb_lines):
        for l in range(nb_lines):
                sys.stdout.write(CURSOR_UP_ONE)
                sys.stdout.write(ERASE_LINE)
                
def draw(screen, score):
        height = max(screen, key= lambda x : x[1])[1] + 1
        width = max(screen, key= lambda x : x[0])[0] + 1
        clean(height + 4)
        for h in range(height):
                line = ''
                for c in range(width):
                        block = ' '
                        if (c, h) in screen:
                                block = screen[(c, h)]
                        if block == 0:
                                block = ' '
                        if block == 1:
                                block = 'x'
                        if block == 2:
                                block = '%'
                        if block == 3:
                                block = '-'
                        if block == 4:
                                block = '0'
                        line += block
                print(line)
        print()
        print('-----------')
        print('|  ' + str(score) + '     |')
        print('-----------')

        
def mapping(inp):
        inp += '  '
        if inp[0] == 'f':
                return 1
        elif inp[0] == 's':
                return -1
        else:
                return 0

file_ = open("input", "r") 
org_entry = list(map(int, file_.read().split(",")))
file_.close()

comp = Computer(org_entry)
screen = {}
cache = []
score = 0
me_x = ball_x = 0
while True:
        output = comp.run()

        if output == 'EOP':
                break

        if output == 'IND':
                draw(screen, score)
                if ball_x > me_x:
                        output = comp.run(1)
                elif ball_x < me_x:
                        output = comp.run(-1)
                else:
                        output = comp.run(0)
                time.sleep(0.05)

        cache.append(output)
        if len(cache) == 3 and cache[0] == -1 and cache[1] == 0:
                score = cache[2]
                cache = []

        if len(cache) == 3:
                assert(cache[2] in range(5))
                screen[(cache[0], cache[1])] = cache[2]
                if cache[2] == 4:
                        ball_x = cache[0]
                if cache[2] == 3:
                        me_x = cache[0]
                cache = []

print(str(score))
