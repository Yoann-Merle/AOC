#!/usr/bin/python3
import re
import time


def dealIntoNew(stack):
        stack.reverse()

def cutNcard(stack, n):
        return stack[n:] + stack[:n]

def incrementN(stack, n):
        newStack = []
        for i in range(nCards):
                newStack.append(0)
        for i in range(nCards):
                newStack[(i*n) % nCards] = stack[i]

        return newStack

# create initial stack
#initStack = []
#nCards = 100007
#for i in range(nCards):
#        initStack.append(i)
#
#val = ''
#for instruct in instructs:
#        if re.search("\Adeal with increment", instruct):
#                n = int(re.split("\s", instruct)[-1])
#                initStack = incrementN(initStack, n)
#        if re.search("\Acut", instruct):
#                n = int(re.split("\s", instruct)[-1])
#                initStack = cutNcard(initStack, n)
#        if re.search("\Adeal into new stack", instruct):
#                dealIntoNew(initStack)

file_ = open("input4", "r")
instructs = list(file_.read().split("\n"))
file_.close()

nCards = 10 #119315717514047
currentPosition = 3 #2020
instructs.reverse()
for currentPosition in range(10):
        result = ''
        for instruct in instructs:
                if re.search("\Adeal with increment", instruct):
                        n = int(re.split("\s", instruct)[-1])
                        ind_section = int(currentPosition/n)
                        m_loop = 0
                        cycles = 0
                        while True:
                                #print()
                                #print('cp: ' + str(currentPosition))
                                #print('ind_section: ' + str(ind_section))
                                #print('m_loop: ' + str(m_loop))
                                #print('cycles: ' + str(cycles))
                                if currentPosition == ind_section * n + m_loop:
                                        currentPosition = cycles + ind_section
                                        break
                                else:
                                        cycles += int((nCards - m_loop) / n) + 1
                                        m_loop = n - ((nCards - m_loop) % n)

                if re.search("\Acut", instruct):
                        n = int(re.split("\s", instruct)[-1])
                        if n > 0:
                                if currentPosition >= nCards - n:
                                        currentPosition = currentPosition - nCards + n
                                else:
                                        currentPosition = currentPosition + n
                        else: 
                                if currentPosition >= -n:
                                        currentPosition += n
                                else:
                                        currentPosition = currentPosition + nCards + n
                if re.search("\Adeal into new stack", instruct):
                        currentPosition = nCards - 1 - currentPosition
        
                result += ' ' + str(currentPosition)
        print('**** : ' + str(result))
