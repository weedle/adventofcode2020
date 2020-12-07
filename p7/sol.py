#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r') 
lines = datafile.readlines() 

bags = {}

def parseLine(line):
    line = line.strip()
    bagType = line.split('bags')[0].strip()
    matches = re.findall('((\d)+ (\w+ \w+) bags?,?)+.', line)
    contents = []
    for match in matches:
        innerBag = (match[2], int(match[1]))
        contents.append(innerBag)
    bags[bagType] = contents

def populateBags(lines):
    for line in lines:
        parseLine(line)

def checkBagType(bagToCheck, target):
    contents = bags[bagToCheck]
    for innerBag in contents:
        if innerBag[0] == target:
            return True
        if checkBagType(innerBag[0], target):
            return True
    return False

def sumBagContents(bagToCheck):
    contents = bags[bagToCheck]
    numInnerBags = 0
    for innerBag in contents:
        numInnerBags += innerBag[1] * sumBagContents(innerBag[0]) + innerBag[1]
    return numInnerBags

def checkAllBags(target):
    numBags = 0
    for bagType in bags.keys():
        result = checkBagType(bagType, target)
        if result:
            numBags += 1
    return numBags


populateBags(lines)

key = 'shiny gold'
print('Number of bags containing {}: {}'.format(key, checkAllBags(key)))
print('Number of bags in {}: {}'.format(key, sumBagContents(key)))
