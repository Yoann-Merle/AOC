#!/usr/bin/python3

import display
import random
import time
from computer import Computer

def mappingInput(letterInput):
        if letterInput == 'z':
                return 1
        elif letterInput == 's':
                return 2
        elif letterInput == 'q':
                return 3
        else:
                return 4
 
def nextPos(org, mouv):
        if mouv == 1:
                return (org[0], org[1] - 1)
        elif mouv == 2:
                return (org[0], org[1] + 1)
        elif mouv == 3:
                return (org[0] - 1, org[1])
        else: 
                return (org[0] + 1, org[1])

file_ = open("input", "r") 
org_entry = list(map(int, file_.read().split(",")))
file_.close()

comp = Computer(org_entry)
myPos = (0, 0)
p_wall = 'x' 
p_me = 'o' 
p_oxy = 'P' 
coor_oxy = ''
p_empty = '.' 
p_current = '.' 

auto = False
scores = []
screen = {myPos: p_me}
minDistByPoint = {}
i = 0
while True:
        i += 1
        scores = [i]
        if len(minDistByPoint) > 0:
                maxDist = max(minDistByPoint.values())
                scores =  [i, maxDist]

        display.draw(screen, scores)
        potentielMov = [1, 2, 3, 4]
        pot = list(map(lambda x : screen[nextPos(myPos, x)] if nextPos(myPos, x) in screen else ' ', potentielMov))
        if ' ' in pot:
                mouvement = potentielMov[pot.index(' ')]
        else:
                indices = [i for i, x in enumerate(pot) if x == '.']
                indice = random.choice(indices)
                mouvement = potentielMov[indice]

        if i % 50000 == 0 or auto == False:
                input_ = input()
                if input_ == 'a':
                        auto = True
                        continue
                else:
                        auto = False
                        mouvement = mappingInput(input_)

        output = comp.run(mouvement)
        myNextPos = nextPos(myPos, mouvement)

        if output == 'EOP':
                break

        if output == 0:
                screen[myNextPos] = p_wall
        else:
                if myPos in minDistByPoint:
                        if myNextPos not in minDistByPoint:
                                minDistByPoint[myNextPos] = minDistByPoint[myPos] + 1 
                        else:
                                if minDistByPoint[myNextPos] > minDistByPoint[myPos] + 1:
                                        minDistByPoint[myNextPos] = minDistByPoint[myPos] + 1 


                screen[myPos] = p_current
                myPos = myNextPos
                screen[myPos] = p_me
                if output == 1:
                        p_current = p_empty
                if output == 2:
                        coor_oxy = myPos
                        minDistByPoint[myPos] = 0
                        p_current = p_oxy
