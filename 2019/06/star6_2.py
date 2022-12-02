#!/usr/bin/python3

allOrbits = []

def findCenter(orb):
        for pair in allOrbits:
                if pair[1] == orb:
                        return pair[0]
def findPath(center):
        path = set()
        while center != 'COM':
                path.add(center)
                center = findCenter(center)
        return path
        
while True:
        line = input()
        if line == '':
                break
        center, orbit = line.split(')')
        allOrbits += [[center, orbit]]

allOrbitingObjects = set()
for pair in allOrbits:
        allOrbitingObjects.add(pair[1])

myPathToCOM = findPath('YOU')
sanPathToCOM = findPath('SAN')
differenceSet = myPathToCOM.symmetric_difference(sanPathToCOM)
print(str(len(differenceSet) - 2))
