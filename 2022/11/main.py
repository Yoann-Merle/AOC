#!/bin/python3
import sys
from functools import reduce
from monkey import Monkey

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def main():
    lines = read_file()
    monkeys = []
    for i in range(0, len(lines)-1, 7):
        monkeys.append(Monkey(lines[i:i+6]))
    for _ in range(20):
        for m in range(len(monkeys)):
            trown_objects = monkeys[m].operate_and_throw()
            for mn, it in trown_objects:
                monkeys[mn].add_item(it)

    list_inspected = [m.items_inspected for m in monkeys]
    list_inspected.sort()
    print("Start 1: ", reduce(lambda x, y: x * y, list_inspected[-2:], 1))

    monkeys = []
    for i in range(0, len(lines)-1, 7):
        monkeys.append(Monkey(lines[i:i+6], False))
    for i in range(10000):
        for m in range(len(monkeys)):
            trown_objects = monkeys[m].operate_and_throw()
            for mn, it in trown_objects:
                monkeys[mn].add_item(it)

    list_inspected = [m.items_inspected for m in monkeys]
    list_inspected.sort()
    print("Start 2: ", reduce(lambda x, y: x * y, list_inspected[-2:], 1))

main()
