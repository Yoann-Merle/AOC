#!/usr/bin/python3
from fractions import gcd
class Moon:

        def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z
                self.vx = 0
                self.vy = 0
                self.vz = 0

        def applyVelocity(self):
                self.x += self.vx
                self.y += self.vy
                self.z += self.vz

        def gravitationPull(self, dimensions, moon2):
                if 'x' in dimensions:
                        self.gravitationPull_X(moon2)
                if 'y' in dimensions:
                        self.gravitationPull_Y(moon2)
                if 'z' in dimensions:
                        self.gravitationPull_Z(moon2)

        def gravitationPull_X(self, moon2):
                if moon2.x > self.x:
                        self.vx += 1
                elif moon2.x < self.x:
                        self.vx -= 1

        def gravitationPull_Y(self, moon2):
                if moon2.y > self.y:
                        self.vy += 1
                elif moon2.y < self.y:
                        self.vy -= 1

        def gravitationPull_Z(self, moon2):
                if moon2.z > self.z:
                        self.vz += 1
                elif moon2.z < self.z:
                        self.vz -= 1
        def energy(self):
                return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vx) + abs(self.vy) + abs(self.vz))
        
def LCM( x , y , z ):
    ans = int((x * y) / (gcd(x, y)))
    return int((z * ans) / (gcd(ans, z)))

Io = Moon(-17, 9, -5)
Europa = Moon(-1, 7, 13)
Ganymede = Moon(-19, 12, 5)
Callisto = Moon(-6, -6, -4)

#Io = Moon(-8,-10,0)
#Europa = Moon(5, 5, 10)
#Ganymede = Moon(2, -7, 3)
#Callisto = Moon(9, -8, -3)
allMoon = [Io, Europa, Ganymede, Callisto]
for i in range(10000):
        for l in allMoon:
                for l2 in allMoon:
                        if l2 != l:
                                l.gravitationPull('xyz', l2)
        for l in allMoon:
                l.applyVelocity()
        if Io.x == -17 and Europa.x == -1 and Ganymede.x == -19 and Callisto.x == -6 and Io.vx == 0 and Europa.vx == 0 and Ganymede.vx == 0 and Callisto.vx == 0:
                #print(str(Io.energy() + Europa.energy() + Ganymede.energy() + Callisto.energy()))
                print('x : ' + str(i))
        if Io.y == 9 and Europa.y == 7 and Ganymede.y == 12 and Callisto.y == -6 and  Io.vy == 0 and Europa.vy == 0 and Ganymede.vy == 0 and Callisto.vy == 0:
                print('y :\t ' + str(i))
        if Io.z == -5 and Europa.z == 13 and Ganymede.z == 5 and Callisto.z == -4 and Io.vz == 0 and Europa.vz == 0 and Ganymede.vz == 0 and Callisto.vz == 0:
                print('z :\t\t ' + str(i))
print(str(LCM(186028, 231614, 60424)))
