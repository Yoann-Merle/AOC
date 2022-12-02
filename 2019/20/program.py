#!/usr/bin/python3
import time
import sys
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def findAdjacents(x, y, collection):
        Adjacents = []
        if (x + 1, y) in collection['path']:
               Adjacents.append((x + 1, y))
        if (x - 1, y) in collection['path']:
               Adjacents.append((x - 1, y))
        if (x , y + 1) in collection['path']:
               Adjacents.append((x, y + 1))
        if (x, y - 1) in collection['path']:
               Adjacents.append((x, y - 1))
        return Adjacents

def findGate(x, y, mapping):
        first_letter = mapping[y][x]
        letters = ''
        coords = (0, 0)
        if mapping[y][x - 1].isalpha():
                letters = mapping[y][x - 1] + first_letter
                if mapping[y][x - 2] == '.':
                        coords = (x - 2, y)
                else:
                        coords = (x + 1, y)
        elif mapping[y][x + 1].isalpha():
                letters = first_letter + mapping[y][x + 1]
                if mapping[y][x - 1] == '.':
                        coords = (x - 1, y)
                else:
                        coords = (x + 2, y)
        elif mapping[y - 1][x].isalpha():
                letters = mapping[y - 1][x] + first_letter
                if mapping[y + 1][x] == '.':
                        coords = (x, y + 1)
                else:
                        coords = (x, y - 2)
        elif mapping[y + 1][x].isalpha():
                letters = first_letter + mapping[y + 1][x]
                if mapping[y - 1][x] == '.':
                        coords = (x, y - 1)
                else:
                        coords = (x, y + 2)
        else:
                print('****ERROR***')
                exit()
        return letters, coords
        
def isGates(x, y, collection):
        for key, pair in collection['gates'].items():
                if (x, y) in pair:
                        return key
        return False

mapping = []
file_ = open("input", "r") 
while True:
        line = list(file_.readline().rstrip('\n'))
        if line == []:
                break
        mapping.append(line)
file_.close()

def buildCollection():
        collection = {'path': set(), 'gates': {}}
        for l in range(len(mapping)):
                for x in range(len(mapping[0])):
                        if mapping[l][x] == '.':
                                collection['path'].add((x, l))
                        elif mapping[l][x].isalpha():
                                letters, coord = findGate(x, l, mapping)
                                if letters == 'AA':
                                        start = coord
                                        continue
                                if letters == 'ZZ':
                                        finish = coord
                                        continue
                                if letters not in collection['gates']:
                                        collection['gates'][letters] = set()
                                collection['gates'][letters].add((coord))
        return collection, start, finish

collection, start, finish = buildCollection()
collOfCollection = {1: collection}
points = [(1, start)]
minPath = 1
while True:
        nexts = []
        if points == set():
                exit()
        for point in points:
                position = point[1]
                level = point[0]
                if position in collOfCollection[level]['path']:
                        gate = isGates(position[0], position[1], collOfCollection[level])
                        if gate:
                                for g in collOfCollection[level]['gates'][gate]:
                                        if g != position:
                                                if 15 < position[0] < 100 and 20 < position[1] < 100:
                    #                            if 6 < position[0] < 40 and 6 < position[1] < 33:
                                                        if level + 1 not in collOfCollection:
                                                                collOfCollection[level + 1], dump, dump2 = buildCollection()
                                                        if level < 50:
                                                                nexts.append((level + 1, g))
                                                elif level > 1:
                                                        nexts.append((level - 1, g))
                        nexts += list(map(lambda x: (level, x), findAdjacents(position[0], position[1], collOfCollection[level])))
                        collOfCollection[level]['path'].remove(position)

        if (1, finish) in nexts:
                print('distance : ' + str(minPath))
                exit()
        minPath += 1
        points = set(nexts)


