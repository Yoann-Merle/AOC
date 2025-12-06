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
    position = 50
    counter = 0
    counter_t = 0
    for line in lines:
        D = line[0]
        N = int(line[1:])
        it = 0
        if D == 'R':
            position += N
        elif D == 'L':
            if N >= position and position != 0:
                it = 1
            position -= N
        else:
            raise Exception('No direction')

        it += abs(int(position / 100))
        counter_t += it
        position %= 100
        print(f"p: {position}")
        if position == 0:
            counter += 1
        print(f"{counter}  {counter_t}")

    print('Star 1: ', counter)
    print('Star 2: ', counter_t)

main()
