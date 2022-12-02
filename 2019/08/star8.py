#!/usr/bin/python3

width = 25
height = 6
pixels = input()

def subset(data, width):
        subsets = []
        startSub = indexSub = 0
        while startSub + width <= len(data):
                subsets.append(list(data[startSub:startSub + width]))
                indexSub += 1
                startSub = indexSub * width
        return subsets

def buildScreen(width, height):
        layer = []
        for h in range(height):
                line = []
                for w in range(width):
                        line.append('')
                layer.append(line)
        return layer
                        
def findFinalImage(layers, width, height):
        layerF = buildScreen(width, height)
        for la in layers:
                line = 0
                for li in la:
                        index = 0
                        for x in li:
                                if layerF[line][index] != '1' and layerF[line][index] != '0':
                                        layerF[line][index] = str(x)
                                index += 1 
                        line += 1
        return layerF
                                

def printS(screen):
        for l in screen:
                li = ''
                for i in l:
                        if i == '0':
                                i = ' '
                        if i == '1':
                                i = '0'
                        li += i
                print(li)
                 
def countN(layer, N):
        count = 0
        for line in layer:
                count += line.count(N)
        return count

#def findLayerWithLowestCountN(layers, N):
#        lowest = '' 
#        lowestL = ''
#        for l in layers:
#                if lowest == '' or lowest > countN(l, N):
#                        lowest = countN(l, N)
#                        lowestL = l
#        
#        return lowestL

lines_ = subset(pixels, width)
layers_ = subset(lines_, height)

final = findFinalImage(layers_, width, height) 
printS(final)
