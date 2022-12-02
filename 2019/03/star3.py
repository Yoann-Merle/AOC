#!/usr/bin/python3

intersection = []

directions1 = input().split(",")
directions2 = input().split(",")

def distance(pointA, pointB):
        xA, yA = pointA
        xB, yB = pointB
        return abs(yB - yA) + abs(xB -xA)

def nextPoints(lastPoint, direction):
        card = direction[:1]
        number = int(direction[1:])
        collectionPoints = []
        x, y = lastPoint
        for n in range(1, number + 1):
                if card == 'U':
                        collectionPoints.append((x, y + n))
                elif card == 'D':
                        collectionPoints.append((x, y - n))
                elif card == 'R':
                        collectionPoints.append((x + n, y))
                else:
                        collectionPoints.append((x - n, y))
        if card == 'U':
               return ((x, y + number), collectionPoints)
        elif card == 'D':
               return ((x, y - number), collectionPoints)
        elif card == 'R':
               return ((x + number, y), collectionPoints)
        else:
               return ((x - number, y), collectionPoints)

def getPath(directions):
        lastPoint = (0, 0) #copy?
        path = []
        for direction in directions:
                lastP, nextPs = nextPoints(lastPoint, direction)
                path += nextPs
                lastPoint = lastP

        return path

def distanceReal(point, path, path2):
        return path.index(point) + path2.index(point) + 2

path1 = getPath(directions1)
path2 = getPath(directions2)
print(path1)
setpath1 = set(path1)
setpath2 = set(path2)

intersects = setpath1.intersection(setpath2)

min_dist = ''
for i in intersects:
        dist = distanceReal(i, path1, path2)
        if min_dist == '' or dist < min_dist:
                min_dist = dist
                j = i


print('j:' + str(j) + ' min_dist: ' + str(min_dist))
