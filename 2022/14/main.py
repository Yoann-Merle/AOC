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


def generate_points(pp, p):
    points = []
    if pp[0] == p[0]:
        p_sup = p[1] > pp[1]
        for i in range(1, abs(p[1] - pp[1]) + 1):
            y = pp[1] + i if p_sup else pp[1] - i
            points.append((p[0], y))
    elif pp[1] == p[1]:
        p_sup = p[0] > pp[0]
        for i in range(1, abs(p[0] - pp[0]) + 1):
            x = pp[0] + i if p_sup else pp[0] - i
            points.append((x, p[1]))
    else:
        raise Exception()

    return points

def add_point(points, point_x, point_y):
    if point_y in points:
        points[point_y].append(point_x)
    else:
        points[point_y] = [point_x]

def drop_sand(m, b=None):
    pos = (500, 0)
    max_ = max(m.keys())
    while True:
        x = pos[0]
        y = pos[1]
        if pos[1] >= max_ and b == None:
            return False
        if y+1 == b and b != None:
            return pos
        if y + 1 not in m:
            pos = (x, y+1)
            continue
        if x not in m[y+1]:
            pos = (x, y+1)
            continue
        if x-1 not in m[y+1]:
            pos = (x-1, y+1)
            continue
        if x+1 not in m[y+1]:
            pos = (x+1, y+1)
            continue
        return pos

def main():
    lines = read_file()
    map_ = {}
    for l in lines:
        anchors = l.split(' -> ')
        for i in range(len(anchors)):
            [x, y] = [int(a) for a in anchors[i].split(',')]
            if i == 0:
                add_point(map_, x, y)
            else:
                [xp, yp] = [int(a) for a in anchors[i-1].split(',')]
                new_points = generate_points((xp, yp), (x, y))
                for np in new_points:
                    add_point(map_, np[0], np[1])

    map_copy = copy.deepcopy(map_)
    sand_drop = 0
    while True:
        rested = drop_sand(map_copy)
        if rested == False:
            break
        if rested[1] in map_copy:
            map_copy[rested[1]].append(rested[0])
        else:
            map_copy[rested[1]] = [rested[0]]
        sand_drop += 1
    print('Star 1: ', sand_drop)

    map_copy = copy.deepcopy(map_copy)
    bottom = max(map_copy.keys()) + 2
    while True:
        rested = drop_sand(map_copy, bottom)
        sand_drop += 1
        if rested == (500, 0):
            break
        if rested[1] in map_copy:
            map_copy[rested[1]].append(rested[0])
        else:
            map_copy[rested[1]] = [rested[0]]
    print('Star 2: ', sand_drop)

main()
