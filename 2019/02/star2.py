#!/usr/bin/python3

org_entry = list(map(int, input().split(",")))
def override(value, place):
        entry[place] = value

for entry_1 in range(99):
        for entry_2 in range(99):
                entry = org_entry.copy()
                i = 0
                while i <= len(entry) - 3:
                        entry[1] = entry_1
                        entry[2] = entry_2
                        if entry[i] == 1:
                                override(entry[entry[i+1]] + entry[entry[i+2]], entry[i+3])
                        elif entry[i] == 2:
                                override(entry[entry[i+1]] * entry[entry[i+2]], entry[i+3])
                        else:
                                break
                        i += 4
                if entry[0] == 19690720:
                        print(str(entry_1) + " " + str(entry_2))
                        exit()

