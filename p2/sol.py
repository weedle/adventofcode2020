#!/usr/bin/python3
# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()

def parseLine(line):
    data = line.split(' ')
    minVal, maxVal = data[0].split('-')
    charReq = data[1][0]
    password = data[2]
    return (int(minVal), int(maxVal), charReq, password)

def checkLine(line):
    good = 0
    minVal, maxVal, charReq, password = parseLine(line)
    count = password.count(charReq)

    if count >= minVal and count <= maxVal:
        print(' passed: {}, has {} {}\'s and needs {}-{}'.format(password, count, charReq, minVal, maxVal))
        return 1
    else:
        print('     failed: {}, has {} {}\'s but needs {}-{}'.format(password, count, charReq, minVal, maxVal))
        return 0

def countGoodPasswords(lines):
    good = 0
    for line in lines:
        good += checkLine(line.strip())
    return good

print(str(countGoodPasswords(lines)) + ' passwords')
