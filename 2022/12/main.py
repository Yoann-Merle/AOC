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
    current_position = (0, 0)
    mapping = []
    for i in range(len(lines)):
        mapping.append([])
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                current_position = (i, j)
            mapping[i].append(lines[i][j])
    possible_paths = build_paths(mapping, current_position)
    min_ = 100000
    shortest_path = []
    for pp in possible_paths:
        if mapping[pp[-1][0]][pp[-1][1]] == 'E' \
            and len(pp) < min_:
            shortest_path = pp
            min_ = len(pp)
    print("Start 1: ", len(shortest_path))


main()
