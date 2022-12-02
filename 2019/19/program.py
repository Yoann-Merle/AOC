#!/usr/bin/python3

import random
import time
from computer import Computer

file_ = open("input", "r") 
org_entry = list(map(int, file_.read().split(",")))
file_.close()

n = 0
c = 0
x_ = y_ = 0

for x in range(1300, 7000):
        print(str(x))
        h = 0
        maxH = 0
        for y in range(6000):
                comp = Computer(org_entry)
                output = comp.run(x)
                output = comp.run(y)

                if output == 1:
                        h +=1
                        if h > maxH:
                                maxH = h
                        if h >= 100: 
                                comp = Computer(org_entry)
                                comp.run(x + 99)
                                ou = comp.run(y - 99)
                                if ou == 1:
                                        print('x: ' + str(x) + ' y: ' + str(y - 99))
                                        exit()
                if output == 0 and h >= 1:
                        break 
        print('max: ' + str(maxH))
