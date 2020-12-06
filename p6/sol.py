import re
import math
file1 = open('data.txt', 'r') 
lines = file1.readlines() 

newEntry = True
entry = []

entryQuestions = []

numQuestions = 0
numQuestionsB = 0

def parseLine(line):
    global newEntry
    if newEntry:
        entry.append([line.strip()])
        newEntry = False
    else:
        if line.strip() == "":
            newEntry = True
        else:
            entry[len(entry)-1].append(line.strip())

for line in lines:
    parseLine(line)
    
for e in entry:
    setQuestions = set()
    setQuestionsB = set()
    setQuestions.update(e[0])
    setQuestionsB.update(e[0])
    for s in e[1:]:
        setQuestions.update(list(s))
        setQuestionsB = setQuestionsB.intersection(list(s))
    entryQuestions.append(setQuestions)
    numQuestions += len(setQuestions)
    numQuestionsB += len(setQuestionsB)

print("Total questions for p1: " + str(numQuestions))
print("Total questions for p2: " + str(numQuestionsB))
