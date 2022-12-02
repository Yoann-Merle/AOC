#!/bin/python3
def read_file(test):
    filename = 'input.txt'
    if test:
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def split_by_empty_line(lines):
    blocks = []
    block = []
    for line in lines:
        if line == '':
            blocks.append(block)
            block = []
        else:
            block.append(int(line))


    return blocks

def main():
    blocks = split_by_empty_line(read_file(False))
    max_ = 0
    for b in blocks:
        s = sum(b)
        if s > max_:
            max_ = s

    print('Start 1: ', max_)

    maxs = []
    for b in blocks:
        maxs.append(sum(b))
    maxs.sort(reverse=True)

    print('Start 2: ', sum(maxs[:3]))

main()
