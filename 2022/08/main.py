#!/bin/python3
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def compute_senic_score(m, h, w):
    height = len(m)
    width = len(m[0])

    count_total = 1
    count = 0
    for i in reversed(range(h)):
        count += 1
        if m[i][w] >= m[h][w]:
            break
    count_total *= count
    count = 0
    for i in range(h+1, height):
        count += 1
        if m[i][w] >= m[h][w]:
            break
    count_total *= count
    count = 0
    for i in reversed(range(w)):
        count += 1
        if m[h][i] >= m[h][w]:
            break
    count_total *= count
    count = 0
    for i in range(w+1, width):
        count += 1
        if m[h][i] >= m[h][w]:
            break
    count_total *= count
    return count_total

def is_visible(m, h, w):
    height = len(m)
    width = len(m)
    if h == 0 or w == 0 or h == height - 1 or w == width - 1:
        return True

    return all([m[i][w] < m[h][w] for i in range(h)]) or \
        all([m[i][w] < m[h][w] for i in range(h+1, height)]) or \
        all([m[h][j] < m[h][w] for j in range(w)]) or \
        all([m[h][j] < m[h][w] for j in range(w+1, width)])

def main():
    lines = read_file()
    matrice = [[n for n in l] for l in lines]
    height = len(matrice)
    width = len(matrice[0])
    visible_trees = 0
    is_visible(matrice, 1, 3)
    max_senic_score = 0
    compute_senic_score(matrice, 1, 2)
    for h in range(height):
        for w in range(width):
            visible_trees += is_visible(matrice, h, w)
            senic_score = compute_senic_score(matrice, h, w)
            if senic_score > max_senic_score:
                max_senic_score = senic_score

    print("Start 1: ", visible_trees)
    print("Start 2: ", max_senic_score)

main()
