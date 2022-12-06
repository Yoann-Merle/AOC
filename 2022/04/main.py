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
    c = 0
    for l in lines:
        first_elf, second_elf = l.split(',')
        [min_first, max_first] = first_elf.split('-')
        [min_sec, max_sec] = second_elf.split('-')
        if (int(min_first) >= int(min_sec) and int(max_first) <= int(max_sec)) or \
            (int(min_sec) >= int(min_first) and int(max_sec) <= int(max_first)):
                c = c+1

    print('Start 1: ', c)

    c = 0
    for l in lines:
        first_elf, second_elf = l.split(',')
        [min_first, max_first] = first_elf.split('-')
        [min_sec, max_sec] = second_elf.split('-')
        if not (int(max_first) < int(min_sec)  or int(max_sec) < int(min_first)):
                c = c+1
    print('Start 2: ', c)


main()
