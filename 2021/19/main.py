#!/bin/python3
import numpy as np
import re
import copy
import time

class Scanner:
    orients_axes = [
        ['x', 'y', 'z'],
        ['x', 'z', 'y'],
        ['y', 'x', 'z'],
        ['y', 'z', 'x'],
        ['z', 'x', 'y'],
        ['z', 'y', 'x'],
    ]

    def __init__(self, beacons):
        self.orient_axe = 0
        self.orient_it = 0
        self.beacons = beacons

    def addBeacon(self, beacon):
        self.beacons.append(beacon)

    def rotate(self):
        self.orient_it += 1
        self.orient_it %= 4
        if self.orient_it == 0:
            self.orient_axe += 1
            self.orient_axe %= len(self.orients_axes)

    def getBeacons(self):
        axe = self.orients_axes[self.orient_axe]
        orient_beacons = []
        for b in self.beacons:
            new_b = {}
            new_b['x'] = b[axe[0]]
            new_b['y'] = b[axe[1]]
            new_b['z'] = b[axe[2]]
            if self.orient_it == 0:
                new_b['x'] *= -1
            elif self.orient_it == 1:
                new_b['y'] *= -1
            elif self.orient_it == 2:
                new_b['z'] *= -1
            orient_beacons.append(new_b)
        return orient_beacons

class Matrice:
    def __init__(self):
        self.points = set()
        self.scanners = set()

    def addScanner(self, scanner):
        beacons = scanner.getBeacons()
        if len(self.points) == 0:
            self.scanners.add((0, 0, 0))
            for b in beacons:
                self.points.add((b['x'], b['y'], b['z']))
            return True
        else:
            for point in self.points:
                for b in beacons:
                    relative_beacons = 
                    for rb in relative_beacons:
                        if rb not in self.points and rb
                            break
                        if 
                    # update beacons positions


def read_input():
    filename = 'input-test2.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def build_scanners(lines):
    scanners = []
    scanner = Scanner([])
    for line in lines:
        if '--' in line:
            scanner = Scanner([])
            scanners.append(scanner)
            continue
        elif '' == line:
            continue
        else:
            x, y, z = line.split(',')
            beacon = {'x': int(x), 'y': int(y), 'z': int(z)}
            scanner.addBeacon(beacon)
    return scanners

def main():
    start = time.time()
    lines = read_input()
    scanners = build_scanners(lines)
    matrice = Matrice()
    for scanner in scanners:
        matrice.addScanner(scanner)

    print(matrice.points)

    # Star 1
    print('Start 1: ', len(scanners))
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

    # Star 2
    print('Start 2: ',)
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

main()
