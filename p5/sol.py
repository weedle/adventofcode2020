import re
import math
file1 = open('data.txt', 'r') 
lines = file1.readlines() 
minInit = 0
maxInit = 128
idsSeen = []
for i in range(0,870):
    idsSeen.append(False)

def giveRange(min, max, front):
    tiny = 0
    if (min+max) % 2 == 0:
        tiny = 1
    if min + 1 == max:
        if front:
            return (min, min)
        else:
            return (max, max)
    if(front):
        return (min, math.floor((min+max)/2) - tiny)
    else:
        return (math.ceil((min+max)/2), max)

def parseLine(line):
    (lmin, lmax) = (minInit, maxInit)
    for l in line[0:7]:
        (lmin, lmax) = giveRange(lmin, lmax, l == "F")
        #print("  " + str(lmin) + " " + str(lmax) + " " + l)
    row = lmin
    lmin, lmax = 0, 8
    for l in line[7:10]:
        (lmin, lmax) = giveRange(lmin, lmax, l == "L")
        #print("  " + str(lmin) + " " + str(lmax) + " " + l)
    idVal = row*8 + lmin
    print("pos: [" + str(row) + "," + str(lmin) + "] -> " + str(idVal))
    return idVal
    
    
maxVal = 0
for line in lines:
    val = parseLine(line)
    maxVal = max(maxVal, val)
    idsSeen[int(val)] = True

print("Max id: " + str(maxVal))

for i in range(0, 865):
    if(idsSeen[i] != True):
        print("Didn't see " + str(i))


