#!/usr/bin/python3

import display
import random
import time
from computer import Computer

file_ = open("input", "r") 
org_entry = list(map(int, file_.read().split(",")))
file_.close()

def asciiInput():
                input_ = input()
                asciiCodes = []
                for in_ in input_:
                        asciiCodes.append(str(ord(in_)))
                asciiCodes.append(10)
                return asciiCodes

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

print(str(feed))
