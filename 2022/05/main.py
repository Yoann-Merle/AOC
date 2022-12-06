#!/bin/python3
import sys
import copy

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def main():
    lines = read_file()
    columns = [[] for _ in range(10)]
    break_ind = 0
    for i in range(len(lines)):
        for v in range(len(lines[i])):
            if v % 4 == 1 and lines[i][v] != ' ':
                columns[int(v/4)].append(lines[i][v])
        if lines[i] == '':
            break_ind = i + 1
            break
    for c in range(len(columns)):
        columns[c].reverse()

    columns_clone = copy.deepcopy(columns)
    for order in lines[break_ind:]:
        number = int(order.split(' ')[1])
        origin = int(order.split(' ')[3]) - 1
        destination = int(order.split(' ')[5]) - 1
        for _ in range(number):
            columns_clone[destination].append(columns_clone[origin].pop())
    print('Start 1: ')
    for c in range(len(columns_clone)):
        print(columns_clone[c][-1:])


    columns_clone = copy.deepcopy(columns)
    for order in lines[break_ind:]:
        number = int(order.split(' ')[1])
        origin = int(order.split(' ')[3]) - 1
        destination = int(order.split(' ')[5]) - 1
        columns_clone[destination] += columns_clone[origin][-number:]
        columns_clone[origin] = columns_clone[origin][:-number]
    print('Start 2: ')
    for c in range(len(columns_clone)):
        print(columns_clone[c][-1:])


main()
