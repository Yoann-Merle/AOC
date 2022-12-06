#!/bin/python3
def read_file(test = True):
    filename = 'input.txt'
    if test:
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def priority(l: str):
    gap = 38
    if l.islower():
        gap = 96
    return ord(l) - gap

def main():
    lines = read_file(False)
    p = 0
    for l in lines:
        duplicate_element = set()
        first_half = l[:int(len(l)/2)]
        sec_half = l[int(len(l)/2):]
        for letter in first_half:
            if letter in sec_half and letter not in duplicate_element:
                duplicate_element.add(letter)
                p += priority(letter)

    print('Start 1: ', p)

    p = 0
    for i in [x for x in range(len(lines)) if x % 3 == 0]:
        for l in lines[i]:
            if l in lines[i+1] and l in lines[i+2]:
                p += priority(l)
                break

    print('Start 2: ', p)

main()
