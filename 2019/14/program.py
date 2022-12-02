#!/usr/bin/python3
import math

treeScience = {}
while True:
        data = input().split('=>')
        if data == ['']:
                break
        nb, key = data[1].strip().split(' ')
        treeScience[key.strip()] = {}
        treeScience[key.strip()]['output'] = int(nb.strip())
        treeScience[key.strip()]['input'] = []
        for ing in data[0].split(','):
                q, i = ing.strip().split(' ')
                treeScience[key.strip()]['input'].append((int(q), i))


def getIngredients(element, qt = 1):
        nbreaction = math.ceil(qt / treeScience[element]['output'])
        needed = list(map(lambda x : (x[0] * nbreaction, x[1]), treeScience[element]['input']))
        left = int(nbreaction * treeScience[element]['output'] - qt )

        return needed, left

def calculusOREForFuel(n_f):
        needed = {'FUEL': n_f}
        leftOver = {}
        while 'ORE' not in needed or len(needed) != 1:
                ings = left = ''
                for l in needed:
                        if l == 'ORE':
                                continue
                        el, nb = l, needed[l]   
                        if el in leftOver:
                                if nb >= leftOver[el]:
                                        nb -= leftOver.pop(el)
                                else:
                                        leftOver[el] -= nb
                                        ings = []
                                        left = 0
                                        break
                                        
                        ings, left = getIngredients(el, nb)
                        break
        
                if el in leftOver:
                        leftOver[el] += left
                else:
                        leftOver[el] = left
                for ing in ings:
                        qt = ing[0]
                        ele = ing[1]
                        if ele in needed:
                                needed[ele] += qt
                        else:
                                needed[ele] = qt
                needed.pop(el)
        return needed['ORE']


min_ = 0
goal = 1000000000000
max_ = int(goal * 5 / 485720)
while True:
        middle = int((max_ + min_) / 2)
        nb = calculusOREForFuel(middle)
        if nb < goal:
                if max_ - middle == 1:
                        print(str(middle))
                        exit()
                min_ = middle
        elif nb >= goal:
                max_ = middle
