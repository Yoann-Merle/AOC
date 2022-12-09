#!/bin/python3
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def move_knot(k, mov):
    direction = mov
    x, y = k
    if direction == 'U':
        return (x, y+1)
    elif direction == 'D':
        return (x, y-1)
    elif direction == 'L':
        return (x-1, y)
    elif direction == 'R':
        return (x+1, y)
    return (0, 0)

def move_tail(head_pos, tail_pos):
    h_x, h_y = head_pos
    t_x, t_y = tail_pos
    x_diff = abs(h_x - t_x)
    y_diff = abs(h_y - t_y)
    x_shift = 1 if h_x > t_x else -1
    y_shift = 1 if h_y > t_y else -1
    if  x_diff <= 1 and  y_diff <= 1:
        return tail_pos
    elif x_diff == 0:
        return (t_x, h_y - y_shift)
    elif y_diff == 0:
        return (h_x - x_shift, t_y)
    else:
        return (t_x + x_shift, t_y + y_shift)

def main():
    lines = read_file()

    head_pos = (0, 0)
    tail_pos = (0, 0)
    tail_path = set()
    tail_path.add(tail_pos)
    for movement in lines:
        direction, iteration = movement.split()
        for _ in range(int(iteration)):
            head_pos = move_knot(head_pos, direction)
            tail_pos = move_tail(head_pos, tail_pos)
            tail_path.add(tail_pos)

    rope = [(0, 0) for _ in range(10)]
    tail_path = set()
    tail_path.add(rope[9])
    for movement in lines:
        direction, iteration = movement.split()
        for _ in range(int(iteration)):
            rope[0] = move_knot(rope[0], direction)
            for i in range(1, len(rope)):
                rope[i] = move_tail(rope[i-1], rope[i])
            tail_path.add(rope[len(rope) - 1])

    print("Start 1: ", len(tail_path))

main()
