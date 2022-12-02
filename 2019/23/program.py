#!/usr/bin/python3

from computer import Computer

file_ = open("input", "r") 
org_entry = list(map(int, file_.read().split(",")))
file_.close()

comp_list = list()
messages = {}
receving_comps = []
nat = []
lastNat = ''
for i in range(50):
    receving_comps.append(True)
    messages[i] = []
    prog = org_entry.copy()
    comp = Computer(prog)
    comp.run([i])
    comp_list.append(comp)

while True:
        for c in range(50):
                if c in messages and messages[c] != []:
                        mess = messages[c].pop(0)
                else:
                        mess = [-1]
                address = comp_list[c].run(mess)
                assert(address != 'EOP')
                if address == 'IND':
                        receving_comps[c] = True
                        continue
                receving_comps[c] = False
                x = comp_list[c].run()
                y = comp_list[c].run()

                if address == 255:
                        nat = [x, y]
                        continue

                messages[address].append([x, y])

        if all(receving_comps) and not any(messages.values()):
                if lastNat == nat[1]:
                        print(str(lastNat))
                        exit()
                messages[0].append(nat)
                lastNat = nat[1]
