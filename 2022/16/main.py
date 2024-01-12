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

def fill_points(nbp, sp, bp):
    md = abs(bp[0] - sp[0]) + abs(bp[1] - sp[1])


def main():
    lines = read_file()
    no_beacon_points = set()
    for l in lines:
        sensor, beacon = l.split(':')
        raw_s_x, raw_s_y = sensor.split(',')
        raw_b_x, raw_b_y = beacon.split(',')
        sx = int(raw_s_x.split('=')[-1])
        sy = int(raw_s_y.split('=')[-1])
        bx = int(raw_b_x.split('=')[-1])
        by = int(raw_b_y.split('=')[-1])
        fill_points(no_beacon_points, (x, y), (bx, by))

    print('Star 1: ', )

main()
