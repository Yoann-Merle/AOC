#!/usr/bin/python3
import time
import timeit
start = timeit.default_timer()

input_ = input()
print(str(len(input_)))
pattern = [0, 1, 0, -1]

def getNext(input_, pattern):
        result = ''
        for k in range(1, len(input_) + 1):
                line = 0
                for j in range(1, len(input_) + 1):
                        index = int(j / k) % (len(pattern))
                        line += int(input_[j- 1]) * int(pattern[index])
                result +=  str(line)[-1:]
        return result
def getRightHalf(totalLength, input_):
        result = ''
        before = 0
        for k in range(int(totalLength - 5978199)):
                if k == 0:
                        result =  str(int(input_[-1:]) + before) + result
                        before = (int(input_[-1:]) + before) % 10
                else:
                        now = (int(input_[-k-1:-k]) + before) % 10
                        result = str(now) + result
                        before = now
        return result
        
        
i = 0
input_ = input_ * 10000
totalLength = len(input_)
while i < 100:
        print(str(i))
        #print(str(input_))
        #print(str(inpu))
        input_ = getRightHalf(totalLength, input_)
        #inpu = getNext(inpu, pattern)
        i += 1
print(input_[:10])

stop = timeit.default_timer()
print('Time: ', stop - start)
