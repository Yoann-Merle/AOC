#!/bin/python3
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def sum_signal(cycle, signal):
    if cycle % 40 == 20:
        print(cycle, signal)
        return cycle * signal
    return 0

def draw(cycle, register):
    position = cycle % 40
    if abs(position - register -1 ) <= 1:
        return '#'
    return '.'

def main():
    lines = read_file()
    register = 1
    cycle = 0
    res = 0
    screen = []
    screen_line = ''
    for line in lines:
        command = line.split()[0]
        cycle += 1
        res += sum_signal(cycle, register)
        screen_line += draw(cycle, register)
        if cycle % 40 == 0:
            screen.append(screen_line)
            screen_line = ''
        if command == 'addx':
            cycle += 1
            res += sum_signal(cycle, register)
            screen_line += draw(cycle, register)
            if cycle % 40 == 0:
                screen.append(screen_line)
                screen_line = ''
            register += int(line.split()[1])

    print("Start 1: ", res)
    print("Start 2: ")
    for sl in screen:
        print(sl)

main()
