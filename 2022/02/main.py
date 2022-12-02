#!/bin/python3
def read_file(test):
    filename = 'input.txt'
    if test:
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def calculate_score(op, me):
    if me == 'X':
        s = 1
        if op == 'A':
            return s + 3
        if op == 'B':
            return s + 0
        if op == 'C':
            return s + 6
    elif me == 'Y':
        s = 2
        if op == 'A':
            return s + 6
        if op == 'B':
            return s + 3
        if op == 'C':
            return s + 0
    elif me == 'Z':
        s = 3
        if op == 'A':
            return s + 0
        if op == 'B':
            return s + 6
        if op == 'C':
            return s + 3
    return 0

def calculate_score_2(op, me):
    if me == 'X':
        s = 0
        if op == 'A':
            return s + 3
        if op == 'B':
            return s + 1
        if op == 'C':
            return s + 2
    elif me == 'Y':
        s = 3
        if op == 'A':
            return s + 1
        if op == 'B':
            return s + 2
        if op == 'C':
            return s + 3
    elif me == 'Z':
        s = 6
        if op == 'A':
            return s + 2
        if op == 'B':
            return s + 3
        if op == 'C':
            return s + 1
    return 0

def main():
    lines = read_file(False)
    s = 0
    for l in lines:
        op, me = l.split()
        s += calculate_score(op, me)

    print('Start 1: ', s)

    s = 0
    for l in lines:
        op, me = l.split()
        s += calculate_score_2(op, me)

    print('Start 2: ', s)

main()
