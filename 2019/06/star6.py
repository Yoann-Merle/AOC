#!/usr/bin/python3

allOrbits = []

def findCenter(orb):
        for pair in allOrbits:
                if pair[1] == orb:
                        return pair[0]
while True:
        line = input()
        if line == '':
                break
        center, orbit = line.split(')')
        allOrbits += [[center, orbit]]

allOrbitingObjects = set()
for pair in allOrbits:
        allOrbitingObjects.add(pair[1])

directAndIndirect = 0
for aOO in allOrbitingObjects:
        directAndIndirect += 1        
        center = findCenter(aOO)
        while center != 'COM':
                directAndIndirect += 1        
                center = findCenter(center)

print(directAndIndirect)      
