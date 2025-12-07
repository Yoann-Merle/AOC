#!/bin/python
import math
import sys


def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def main():
    lines = read_file()
    operations = [[] for _ in lines[0].split()]
    for line in lines:
        i = 0
        for el in line.split():
            operations[i].append(el)
            i += 1
        result = []
        i = 0
        for op in operations:
            if op[-1] == '+':
                result.append(sum(map(int, op[:-1])))
            if op[-1] == '*':
                result.append(math.prod(map(int, op[:-1])))

    print('Star 1: ', sum(result))


main()
