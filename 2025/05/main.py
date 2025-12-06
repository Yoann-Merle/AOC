#!/bin/python3
import sys


def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def extract_info(lines):
    ranges = []
    ingredients = []
    break_point = 0
    for i in range(len(lines)):
        if lines[i] == '':
            break_point = i
            break
        min, max = map(int, lines[i].split('-'))
        ranges.append([min, max])
    for line in lines[break_point+1:]:
        ingredients.append(int(line))

    return ranges, ingredients


def compact_ranges(range_1, range_2):
    if range_1[0] > range_2[1]:
        return range_2, range_1
    if range_2[0] > range_1[1]:
        return range_1, range_2

    return [[min(range_1[0], range_2[0]), max(range_1[1], range_2[1])]]


def inner_compact(l):
    for i in range(len(l) - 1):
        c_ranges = compact_ranges(l[i], l[i+1])
        if len(c_ranges) == 2:
            continue
        new_ranges = []
        if i > 0:
            new_ranges = l[:i]
        new_ranges += c_ranges + l[i+2:]
        return new_ranges
    return l


def in_range(i, r):
    if (i >= r[0] and i <= r[1]):
        return True
    return False


def main():
    lines = read_file()
    ranges, ingredients = extract_info(lines)
    fresh = 0
    for ingredient in ingredients:
        for r in ranges:
            if in_range(ingredient, r):
                fresh += 1
                break

    sorted_ranges = sorted(ranges, key=lambda ra: ra[0])
    len_ra = len(sorted_ranges)
    while True:
        sorted_ranges = inner_compact(sorted_ranges)
        new_len_ra = len(sorted_ranges)
        if len_ra == new_len_ra:
            break
        len_ra = new_len_ra
    count = 0
    for so_ra in sorted_ranges:
        count += so_ra[1] - so_ra[0] + 1

    print('Star 1: ', fresh)
    print('Star 2: ', count)


main()
