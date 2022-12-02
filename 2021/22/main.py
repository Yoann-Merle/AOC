#!/bin/python3
import numpy as np
import re
import copy
import time

def read_input():
    filename = 'input.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def main():
    start = time.time()
    lines = read_input()
    reboot_steps = []
    for line in lines:
        comp_line = re.findall(r'([oOnf]*)\sx=(-?\d+)\.\.(-?\d+),?y=(-?\d+)\.\.(-?\d+),?z=(-?\d+)\.\.(-?\d+)', line)[0]
        step = {
            'order': 1 if comp_line[0] == 'on' else 0,\
            'x': [int(comp_line[1]), int(comp_line[2])],\
            'y': [int(comp_line[3]), int(comp_line[4])],\
            'z': [int(comp_line[5]), int(comp_line[6])],\
        }
        reboot_steps.append(step)

    # Star 1
    matrice = set()
    for rs in reboot_steps:
        minz = np.min(rs['z']) if np.min(rs['z']) >= -50 else -50
        maxz = np.max(rs['z']) if np.max(rs['z']) <= 50 else 50
        miny = np.min(rs['y']) if np.min(rs['y']) >= -50 else -50
        maxy = np.max(rs['y']) if np.max(rs['y']) <= 50 else 50
        minx = np.min(rs['x']) if np.min(rs['x']) >= -50 else -50
        maxx = np.max(rs['x']) if np.max(rs['x']) <= 50 else 50
        for z in range(minz, maxz + 1):
            for y in range(miny, maxy + 1):
                for x in range(minx, maxx + 1):
                    if rs['order'] == 1:
                        matrice.add((x, y, z))
                    else:
                        matrice.discard((x, y, z))


    print('Start 1: ',len(matrice))
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

    # Star 2
    matrice = set()
    for rs in reboot_steps:
        for z in range(minz, maxz + 1):
            for y in range(miny, maxy + 1):
                for x in range(minx, maxx + 1):
                    if rs['order'] == 1:
                        matrice.add((x, y, z))
                    else:
                        matrice.discard((x, y, z))
    print('Start 2: ',)
    end = time.time()
    print('Execution time %3.1f s' %(end - start))
main()
