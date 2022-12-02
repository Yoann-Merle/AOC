#!/usr/bin/python3

def cyclePoint(x, y, index, matrices):
        if index == 0 or index == len(matrices) - 1:
                return 0
        count = 0
        # Left count
        if x == 0:
                count += matrices[index - 1][2][1]
        elif (x == 3 and y == 2):
                count += sum(i[4] for i in matrices[index + 1])
        else:
                count += matrices[index][y][x - 1]

        # Right count
        if x == len(matrices[index][0]) - 1:
                count += matrices[index - 1][2][3]
        elif (x == 1 and y == 2):
                count += sum(i[0] for i in matrices[index + 1])
        else:
                count += matrices[index][y][x + 1]


        # Up count
        if y == 0:
                count += matrices[index - 1][1][2]
        elif (x == 2 and y == 3): 
                count += sum(matrices[index + 1][4])
        else:
                count += matrices[index][y - 1][x]

        # Down count
        if y == len(matrices[index]) - 1:
                count += matrices[index - 1][3][2]
        elif (x == 2 and y == 1): 
                count += sum(matrices[index + 1][0])
        else:
                count += matrices[index][y + 1][x]

        if matrices[index][y][x] == 1:
                if count == 1:
                        return 1
                else:
                        return 0
        else:
                if count == 1 or count == 2:
                        return 1
                else:
                        return 0
                
def getFullCycle(matrices):
        new_matrices = []
        for matrice_index in range(len(matrices)):
                new_matrice = []
                for y in range(len(matrices[matrice_index])):
                        new_matrice.append([])
                        for x in range(len(matrices[matrice_index][0])):
                                if x == 2 and y == 2:
                                        new_matrice[y].append(0)
                                else:
                                        new_matrice[y].append(cyclePoint(x, y, matrice_index, matrices))

                new_matrices.append(new_matrice)
        return new_matrices

def biodiversity(matrice):
        point = 1
        rating = 0
        for y in range(len(matrice)):
                for x in range(len(matrice[0])):
                        if matrice[y][x] == 1:
                                rating += point
                        point *= 2
        return rating

lines = []
file_ = open("input", "r") 
while True:
        line = list(map(int, file_.readline().rstrip('\n').replace('#', '1').replace('.', '0')))
        if line == []:
                break
        lines.append(line)
file_.close()

all_matrices = []
for i in range(200):
        matrice = []
        for l in range(5):
                line = []
                for k in range(5):
                        line.append(0)                        
                matrice.append(line)
        all_matrices.append(matrice)

all_matrices.append(lines)
for i in range(200):
        matrice = []
        for l in range(5):
                line = []
                for k in range(5):
                        line.append(0)                        
                matrice.append(line)
        all_matrices.append(matrice)

for c in range(200):
        for l in all_matrices:
                print(str(l))
        print()
        print()
        print()
        all_matrices = getFullCycle(all_matrices)

count = 0
for m in all_matrices:
        for l in m:
                count += sum(l)

print(str(count))
