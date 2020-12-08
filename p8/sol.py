#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
linesOrig = datafile.readlines()
linesVisited = []

# Set all lines to not visited
def prepLinesVisited(lines):
    global linesVisited
    linesVisited = []
    for line in lines:
        linesVisited.append(False)

# Each line returns a new index
def executeLine(acc, index, lines):
    if index == len(linesVisited):
        print("Success!")
        return (acc, -1)
    if linesVisited[index] == True:
        print("Found loop")
        return (acc, -2)
    line = lines[index].strip()
    print("instr {}: acc {}\t{}".format(index, acc, line))
    instr = line[0:3]
    plus = line[4] == '+'
    num = int(line[5:])
    linesVisited[index] = True
    if instr == "nop":
        return (acc, index + 1)
    elif instr == "acc":
        if plus:
            return (acc + num, index + 1)
        else:
            return (acc - num, index + 1)
    else:
        if plus:
            return (acc, index + num)
        else:
            return (acc, index - num)

def runProgram(lines):
    prepLinesVisited(lines)
    acc, index = 0, 0
    while(index >= 0):
        (acc, index) = executeLine(acc, index, lines)
    if index == -1:
        return True
    else:
        return False

def tryMutations(lines):
    for i in range(0,len(lines)-1):
        line = lines[i]
        instr = line[0:3]
        if instr == 'nop':
            print("Trying mutation of nop on line " + str(i))
            lines[i] = line.replace('nop', 'jmp')
            if runProgram(lines):
                print("Found solution! Mutate nop in line " + str(i+1))
                break
            lines[i] = line.replace('jmp', 'nop')
        elif instr == 'jmp':
            print("Trying mutation of jmp on line " + str(i))
            lines[i] = line.replace('jmp', 'nop')
            if runProgram(lines):
                print("Found solution! Mutate jmp in line " + str(i+1))
                break
            lines[i] = line.replace('nop', 'jmp')

tryMutations(linesOrig)
