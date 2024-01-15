#!/bin/python3
import sys


def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def move(mapping, X, Y, x, y):
    new_positions = set()
    if x+1 < X and mapping[y][x+1] == '.':
        new_positions.add((y, x+1))
    if x > 0 and mapping[y][x-1] == '.':
        new_positions.add((y, x-1))
    if y+1 < Y and mapping[y+1][x] == '.':
        new_positions.add((y+1, x))
    if y > 0 and mapping[y-1][x] == '.':
        new_positions.add((y-1, x))

    return new_positions



def main():
    lines = read_file()
    mapping = []
    Y = len(lines)
    y = 0
    init = (0, 0)
    for line in lines:
        X = len(line)
        mapping.append([x if x != 'S' else '.' for x in line])
        if 'S' in line:
            init = (line.find('S'), y)
        y += 1
    positions = set([init])
    for i in range(64):
        new_positions = set()
        for p in positions:
            new_positions.update(move(mapping, X, Y, p[0], p[1]))
        positions = new_positions

    print('Star 1: ', len(positions))



main()
