#!/bin/python3
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def find_next_point(m, p):
    x, y = p
    next_points = set()
    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        dx = x + i
        dy = y + j
        if dx >= 0 and dy >= 0 and dx < len(m) and dy < len(m[0]):
            ord_dest = ord(m[dx][dy])
            ord_origin = ord(m[x][y])
            if m[x][y] == 'S':
                 ord_origin  = ord('a')
            if m[dx][dy] == 'E':
                 ord_dest = ord('z')
            if ord_dest - ord_origin <= 1:
                next_points.add((dx, dy))

    return next_points

def build_paths(m, cp):
    paths = [[cp]]
    visited_points = set([cp])
    while True:
        found_new_path = False
        new_paths = []
        for path in paths:
            if m[path[-1][0]][path[-1][1]] == 'E':
                new_paths.append(path)
                continue
            nps = find_next_point(m, path[-1])
            nps = nps ^ (nps & visited_points)
            for np in nps:
                found_new_path = True
                visited_points.add(np)
                new_paths.append(path + [np])
        if not found_new_path:
            break
        paths = new_paths

    return new_paths


def main():
    lines = read_file()
    starting_position = (0, 0)
    possible_start_positions = set()
    mapping = []
    for i in range(len(lines)):
        mapping.append([])
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                starting_position = (i, j)
                possible_start_positions.add((i, j))
            if lines[i][j] == 'a':
                possible_start_positions.add((i, j))
            mapping[i].append(lines[i][j])

    min_path = 100000
    for psp in possible_start_positions:
        possible_paths = build_paths(mapping, psp)
        min_ = 100000
        for pp in possible_paths:
            if mapping[pp[-1][0]][pp[-1][1]] == 'E' \
                and len(pp) - 1 < min_:
                min_ = len(pp) - 1
        if psp == starting_position:
            print("Start 1: ", min_)

        if min_ < min_path:
            min_path = min_
    print("Start 2: ", min_path)



main()
