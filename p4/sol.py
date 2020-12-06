import re
import operator
file1 = open('data.txt', 'r') 
lines = file1.readlines() 
good = 0
entries = []
entries.append([])

parsedEntries = []

validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def printSorted(entry):
    return sorted(entry.items(), key=operator.itemgetter(0))

for i in range(0, len(lines)-1):
    line = lines[i].strip()
    if not line:
        entries.append([])
        #print("new entry")
    else:
        entries[len(entries)-1].append(line)

for entry in entries:
    dictEntry = {}
    entryString = ' '.join(entry)
    entrySplit = entryString.split(' ')
    for entryPiece in entrySplit:
        keyVal = entryPiece.split(':')
        if len(keyVal) == 2 and keyVal[0] != 'cid':
            dictEntry[keyVal[0]] = keyVal[1]
    if dictEntry != {}:
        parsedEntries.append(dictEntry)

def valByr(yearStr):
    year = int(yearStr)
    return year >= 1920 and year <= 2002
def valIyr(yearStr):
    year = int(yearStr)
    return year >= 2010 and year <= 2020
def valEyr(yearStr):
    year = int(yearStr)
    return year >= 2020 and year <= 2030
def valHgt(height):
    val = int(height[0:len(height)-2])
    unit = height[len(height)-2:]
    if unit == 'cm':
        return val >= 150 and val <= 193
    elif unit == 'in':
        return val >= 59 and val <= 76
    else:
        return False
def valHcl(color):
    return len(color) == 7 and re.search("#[0-9 a-f]{6}", color) != None
def valEcl(color):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return color in colors
def valPid(pid):
    return len(pid) == 9 and re.search("\d{9}", pid) != None

rules = {'byr': valByr, 'iyr': valIyr, 'eyr': valEyr, 'hgt': valHgt, 'hcl': valHcl, 'ecl': valEcl, 'pid': valPid}

        
def validateEntry(entry):
    #part1
    #if(all(x in entry.keys() for x in validFields) and len(entry.keys()) <= len(validFields)+1):
    #    return True
    #else:
    #    return False
    for key in entry.keys():
        if key not in rules.keys() and key != "cid":
            return False
        if key != 'cid' and not rules[key](entry[key]):
            #print("{} failed rule {}".format(entry[key], key))
            return False
    for key in rules.keys():
        if key not in entry.keys():
            return False
    return True
for entry in parsedEntries:
    if validateEntry(entry):
        print("GOOD: {}".format(printSorted(entry)))
        good += 1
    #else:
    #    print("BAAD: {}".format(entry))

print(str(good) + ' passports')
