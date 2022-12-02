#!/usr/bin/python3

def calculateIndFuel(mass):
        if mass < 8:
                return 0
        if mass >= 8:
                fuel = int(mass/3) - 2
                return fuel + calculateIndFuel(fuel)

def calculateFuel(masses):
        allAmount = 0
        for i in masses:
                allAmount += calculateIndFuel(i)

        return allAmount

allValue = []
entry = input()
while entry != "":
        allValue.append(int(entry))
        entry = input()

print(str(calculateFuel(allValue)))

