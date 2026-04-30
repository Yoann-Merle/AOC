#!/bin/python
import math
import sys


def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def distance(pointA, pointB):
    dx = abs(pointA[0] - pointB[0])
    dy = abs(pointA[1] - pointB[1])
    dz = abs(pointA[2] - pointB[2])
    return math.sqrt((dx*dx) + (dy*dy) + (dz*dz))


def build_circuits(circuits, link):
    a, b = link.split('-')
    k, l = -1, -1
    for i in range(len(circuits)):
        if a in circuits[i]:
            k = i
        if b in circuits[i]:
            l = i
    if k != -1 and l == -1:
        circuits[k].add(b)
    if k == -1 and l != -1:
        circuits[l].add(a)
    if k == -1 and l == -1:
        circuits.append(set({a, b}))
    if k != -1 and l != -1 and k != l:
        circuits[k] = circuits[k].union(circuits[l])
        circuits.pop(l)

    return circuits


def find_all_distances(boxes):
    distances = {}
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if j <= i:
                continue
            distances[f"{i}-{j}"] = distance(boxes[i], boxes[j])
    return dict(sorted(distances.items(), key=lambda item: item[1]))


def main():
    lines = read_file()
    boxes = {}
    for i in range(len(lines)):
        x, y, z = lines[i].split(',')
        boxes[i] = (int(x), int(y), int(z))

    circuits = []
    ds = find_all_distances(boxes)
    i = 0
    for l, d in ds.items():
        i += 1
        print(l)
        circuits = build_circuits(circuits, l)
        print(circuits)
        if i >= 1000:
            break
    circuits_sorted = sorted(circuits, key=lambda item: len(item), reverse=True)

    print('Star 1: ', len(circuits_sorted[0]) * len(circuits_sorted[1]) * len(circuits_sorted[2]))

main()
