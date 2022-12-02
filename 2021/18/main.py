#!/bin/python3
import numpy as np
import re
import copy
import time
import ast

class FishNb:
    @staticmethod
    def fromArray(a):
        if isinstance(a[0], list):
            x = self.fromArray(a[0])
        else:
            x = a[0]
        if isinstance(a[1], list):
            y = self.fromArray(a[1])
        else:
            y = a[1]
        return FishNb(x, y)

    def __init__(self, a, b):
        if not isinstance(a, int) and not isinstance(a, FishNb):
            raise Exception("FishNb must not contains ", type(a))
        if not isinstance(b, int) and not isinstance(b, FishNb):
            raise Exception("FishNb must not contains ", type(b))
        self.x = a
        self.y = b

    def add(self, new):
        self.x = FishNb(self.x, self.y)
        self.y = new

    def explode(self, deepness = 0):
        if deepness < 2:
            xEx = False
            yEx = False
            if isinstance(self.x, FishNb):
                d, xEx = self.x.explode(deepness + 1)
                if d == 1:
            if isinstance(self.y, FishNb):
                yEx = self.y.explode(deepness + 1)
            return xEx and yEx
        else:
            if isinstance(self.x, FishNb):
                self.y += self.x.y
                r = self.x.x
                self.x = 0
                return -1, r
            if isinstance(self.y, FishNb):
                self.x += self.y.x
                r = self.y.y
                self.y = 0
                return 1, r
        return 0, 0

    def split(self):
        return
    def reduce(self):
        while True:
            if self.explode():
                continue
            if self.split():
                continue
            break

def read_input():
    filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def main():
    start = time.time()
    lines = read_input()

    sum = ast.literal_eval(lines[0])
    for line in lines[1:]:
        fish_nb = ast.literal_eval(line)
        fish_nb_ = FishNb.fromArray(fish_nb)
        print(fish_nb_)
        # sum = [sum, fish_nb]
        # reduce(sum)

    # Star 1
    print('Start 1: ', sum)
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

    # Star 2
    print('Start 2: ',)
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

main()
