#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()

values = []

for line in lines:
    line = line.strip()
    values.append(int(line))

values.sort()

print(values)

currJoltage = 0
oneJInc = 0
threeJInc = 0

for i in range(0, len(values)):
    diff = values[i] - currJoltage
    if diff == 1:
        oneJInc += 1
    elif diff == 3:
        threeJInc += 1
    currJoltage = values[i]

threeJInc += 1

print("Sorted: {}".format(values))
print("Done: {} 1J jumps and {} 3J jumps, product is {}".format(oneJInc, threeJInc, oneJInc * threeJInc))

paths = []
for v in values:
    if v <= 3:
        paths.append(1)
    else:
        paths.append(0)
def findChain(index, currJoltage, values):
    for i in range(0, len(values)-1):
        print("{}: {}".format(i, values[i]))
        for j in range(i+1, min(i+4, len(values))):
            print("   {}: {}".format(j, values[j]))
            if values[j] - values[i] <= 3:
                paths[j] += paths[i]
findChain(0, 0, values)
print("Values: {}".format(values))
print("Paths: {}".format(paths))
