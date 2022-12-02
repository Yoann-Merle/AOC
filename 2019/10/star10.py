#!/usr/bin/python3
import time

mapping = []
height = 0
width = 0
while True:
        line = list(input())
        if line == []:
                break
        width =len(line)
        height += 1
        mapping.append(line)

def findBetween(a, b):
        xa, ya = a
        xb, yb = b
        # Régler division par zéro
        if xb -xa != 0:
                coef = (yb - ya) / (xb - xa)
                bf = ya - coef * xa
        
        range_ = range(height)
        if ya >= yb:
                range_y = range(yb, ya + 1)
        else:
                range_y = range(ya, yb + 1)

        if xa >= xb:
                range_x = range(xb, xa + 1)
        else:
                range_x = range(xa, xb + 1)

        for nl in range_y:
                for nc in range_x:
                        if mapping[nl][nc] != '.' and ((nc != xa or nl != ya) and (nc != xb or nl != yb)):
                                if xb - xa == 0 and nc == xa:
                                        return True
                                if xb - xa != 0 and -0.0001 < coef * nc + bf - nl < 0.0001:
                                        return True
        return False

def countdirectSight(mapping, x, y):
        directOnes = []
        for nl in range(height):
                for nc in range(width):
                        if mapping[nl][nc] != '.' and ( nc != x or nl != y ):
                                if not findBetween((x, y), (nc, nl)):
                                       directOnes.append((nc, nl))
        return directOnes

def destroy(mapping, x, y):
        mapping[y][x] = '.'
        return mapping

def findVerticalUp(point, listPoint):
        list_ = set()
        for point2 in listPoint:
                if point[0] == point2[0] and point[1] > point2[1]:
                       list_.add((1, point2)) 
        return list_

def findVerticalDown(point, listPoint):
        list_ = set()
        for point2 in listPoint:
                if point[0] == point2[0] and point[1] < point2[1]:
                       list_.add((1, point2)) 
        return list_
                       
def getCoef(item):
        return item[0]

def findRight(point, listPoint):
        list_ = set()
        for point2 in listPoint:
                if point[0] < point2[0]:
                        list_.add(((point[1] - point2[1]) / (point2[0] - point[0]), point2))
        return sorted(list_, key=getCoef, reverse=True)

def findLeft(point, listPoint):
        list_ = set()
        for point2 in listPoint:
                if point[0] > point2[0]:
                        list_.add(((point[1] - point2[1]) / (point[0] - point2[0]), point2))
        return sorted(list_, key=getCoef)
                
def search(mapping):
        maxDirectSight = -1
        maxCoordonate = -1
        for nl in range(height):
                for nc in range(width):
                        if mapping[nl][nc] == '#':
                                listDirectContact = countdirectSight(mapping, nc, nl)
                                if len(listDirectContact) > maxDirectSight:
                                        maxDirectSight = len(listDirectContact)
                                        maxCoordonate = (nc, nl)
        return maxCoordonate

index = 1
i = 0
maxList = []
maxCoordonate = (0, 0)
listDirectContact = set()
maxCoordonate = search(mapping)
print(str(maxCoordonate))
listDirectContact = countdirectSight(mapping, maxCoordonate[0], maxCoordonate[1])
while index <= 200:
        print('******************' + str(i))
        if i % 4 == 0:
                result = findVerticalUp(maxCoordonate, listDirectContact)
        if i % 4 == 1:
                result = findRight(maxCoordonate, listDirectContact)
        if i % 4 == 2:
                result = findVerticalDown(maxCoordonate, listDirectContact)
        if i % 4 == 3:
                result = findLeft(maxCoordonate, listDirectContact)
        for r in result:
                if index == 200 or index == 199 or index == 50 or index == 20:
                        print('index' + str(index) + '_______' + str(r))
                if index == 200:
                        print(str(r))
                        exit()
                mapping = destroy(mapping, r[1][0], r[1][1])
                index += 1
        if i % 4 == 3:
                listDirectContact = countdirectSight(mapping, maxCoordonate[0], maxCoordonate[1])
        i += 1
