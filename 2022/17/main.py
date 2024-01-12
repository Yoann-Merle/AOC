#!/bin/python3
import copy
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def fill_points(nbp, sp, bp):
    md = abs(bp[0] - sp[0]) + abs(bp[1] - sp[1])


def main():
    lines = read_file()
    for l in lines:

    print('Star 1: ', )

main()
