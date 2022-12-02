#!/usr/bin/python3

start = 264793 #int(input()) #264793
finish = 803935 #int(input()) #803935

def isConform(number):
        twoConsecutive = False
        last = int(str(number)[1:2])
        count = 0
        beforeLast = int(str(number)[:1])
        if beforeLast > last:
                return False
        if beforeLast == last:
                count = 1
        for i in str(number)[2:]:
                if int(i) < int(last):
                        return False
                elif int(i) == int(last):
                        count += 1
                else:
                        if count == 1:
                                twoConsecutive = True
                        count = 0
                beforeLast = last
                last = i
        if count == 1:
                twoConsecutive = True 

        return twoConsecutive

j = start                        
count = 0
while j <= finish:
        if isConform(j):
                count += 1
        j += 1
        
print(count)
