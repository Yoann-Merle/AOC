#!/usr/bin/python3

import display
import random
import time
from computer import Computer

file_ = open("input", "r") 
org_entry = list(map(int, file_.read().split(",")))
file_.close()

def interAndPath(screen):
        path = []
        intersections = []
        for x, y in screen:
                if (x, y + 1) in screen and (x + 1, y) in screen and (x - 1, y) in screen and (x, y -1) in screen and screen[(x, y + 1)] == screen[(x + 1, y)] == screen[(x - 1, y)] == screen[(x, y -1)] == screen[(x, y)] == 35:
                        intersections.append((x, y))
                if screen[(x, y)] in [35, 94, 60, 62, 118]: # #,^,<,>,v
                        path.append((x,y))
        return path, intersections

def asciiInput():
                input_ = input()
                asciiCodes = []
                for in_ in input_:
                        asciiCodes.append(str(ord(in_)))
                asciiCodes.append(10)
                return asciiCodes

def calculateMap(feed):
        c = 0
        l = 0
        mapping = {}
        for f in feed:
                if f == 10:
                        c = 0
                        l += 1
                elif f in [35, 46, 94, 60, 62, 118]: # #,.,^,<,>,v
                        mapping[(c,l)] = f
                        c += 1
        return mapping 

comp = Computer(org_entry)
screen = {}
feed = []
in_ = []
feed = []
while True:
        output = comp.run(in_)
        in_ = []
        if output == 'EOP':
                break
        elif output == 'IND':
                in_ = asciiInput()
        else:
                feed.append(output)
                if output == 10:
                        display.drawAsciiLine(feed)
                        feed = []

path, inter = interAndPath(screen)
