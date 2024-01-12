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

def add_faces(f, c):
    for d in range(3):
        for w in [-0.5, 0.5]:
            c2 = list(copy.deepcopy(c))
            c2[d] = c2[d] + w
            tuple_c2 = tuple(c2)
            if tuple_c2 in f:
                f.remove(tuple_c2)
            else:
                f.add(tuple_c2)
def main():
    lines = read_file()
    cubes = []
    for l in lines:
        [x, y, z] = map(int, l.split(','))
        cubes.append((x, y, z))
    faces = set()
    for cube in cubes:
        add_faces(faces, cube)
    print('Star 1: ', len(faces))

main()
