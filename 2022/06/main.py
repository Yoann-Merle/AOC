#!/bin/python3
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
    length = 4
    res = 0
    for l in lines:
        for i in range(len(l) - length):
            portion_set = set()
            for j in range(length):
                portion_set.add(l[i+j])
            if len(portion_set) == length:
                res = i+length
                break
        print("Start 1: ", res)
    length = 14
    res = 0
    for l in lines:
        for i in range(len(l) - length):
            portion_set = set()
            for j in range(length):
                portion_set.add(l[i+j])
            if len(portion_set) == length:
                res = i+length
                break
        print("Start 2: ", res)
main()
