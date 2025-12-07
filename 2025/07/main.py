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


def main():
    lines = read_file()
    beams = set()
    new_beams = set()
    beams_count = {}
    new_beams_count = {}
    split = 0
    for i in range(len(lines[0])):
        if lines[0][i] == 'S':
            beams = {i}
            beams_count = {i: 1}
    for li in lines[1:]:
        for b in beams:
            if li[b] == '.':
                new_beams.add(b)
                if b in new_beams_count.keys():
                    new_beams_count[b] += beams_count[b]
                else:
                    new_beams_count[b] = beams_count[b]
            elif li[b] == '^':
                split += 1
                new_beams.add(b-1)
                new_beams.add(b+1)
                if b - 1 in new_beams_count.keys():
                    new_beams_count[b-1] += beams_count[b]
                else:
                    new_beams_count[b-1] = beams_count[b]
                if b + 1 in new_beams_count.keys():
                    new_beams_count[b+1] += beams_count[b]
                else:
                    new_beams_count[b+1] = beams_count[b]
        beams = new_beams
        new_beams = set()
        beams_count = new_beams_count
        new_beams_count = {}

    print('Star 1: ', split)
    print('Star 1: ', sum(beams_count.values()))



main()
