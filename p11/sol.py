#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()

seating = []

for i in range(0, len(lines)):
    seating.append(list(lines[i].strip()))

def checkSeat(row, col, seating):
    if row < 0 or row >= len(seating):
        return 0
    if col < 0 or col >= len(seating[0]):
        return 0
    if seating[row][col] == '#':
        return 1
    return 0

def getAdjacentSeatsPart1(row, col, seating):
    adjacent = 0;
    adjacent += checkSeat(row-1, col-1, seating)
    adjacent += checkSeat(row-1, col, seating)
    adjacent += checkSeat(row-1, col+1, seating)
    adjacent += checkSeat(row, col-1, seating)
    adjacent += checkSeat(row, col+1, seating)
    adjacent += checkSeat(row+1, col-1, seating)
    adjacent += checkSeat(row+1, col, seating)
    adjacent += checkSeat(row+1, col+1, seating)
    return adjacent

def checkDirection(h, v, row, col, seating):
    row += h
    col += v

    while row >= 0 and row < len(seating) and col >= 0 and col < len(seating[0]):
        if checkSeat(row, col, seating):
            return 1
        if seating[row][col] != '.':
            break;
        row += h
        col += v
    return 0

def getAdjacentSeats(row, col, seating):
    adjacent = 0;
    adjacent += checkDirection(-1, -1, row, col, seating)
    adjacent += checkDirection(-1, 0, row, col, seating)
    adjacent += checkDirection(-1, 1, row, col, seating)
    adjacent += checkDirection(0, -1, row, col, seating)
    adjacent += checkDirection(0, 1, row, col, seating)
    adjacent += checkDirection(+1, -1, row, col, seating)
    adjacent += checkDirection(+1, 0, row, col, seating)
    adjacent += checkDirection(+1, 1, row, col, seating)
    return adjacent

#for i in range(0, len(seating)):
#    for j in range(0, len(seating[0])):
#        print(getAdjacentSeats(i, j, seating))

def getNumSeats(seating):
    numSeats = 0
    for row in seating:
        for seat in row:
            if seat == '#':
                numSeats += 1
    return numSeats

def isSeat(row, col, seating):
    return seating[row][col] != '.'

def doRound(seating):
    newSeating = []
    for i in range(0, len(seating)):
        newRow = []
        for j in range(0, len(seating[0])):
            if isSeat(i, j, seating):
                if getAdjacentSeats(i, j, seating) == 0 and checkSeat(i, j, seating) == 0:
                    newRow.append('#')
                # 4 -> 5 for part 2
                elif getAdjacentSeats(i, j, seating) >= 5 and checkSeat(i, j, seating) == 1:
                    newRow.append('L')
                else:
                    newRow.append(seating[i][j])
            else:
                newRow.append('.')
        newSeating.append(newRow)
    return newSeating

def printSeatingArrangement(seating):
    for row in seating:
        print("[ " + ' '.join(row) + " ]\n")

def execute(seating):
    prevState = -1
    currState = 0
    numRounds = 0
    while prevState != currState:
        prevState = currState
        seating = doRound(seating)
        printSeatingArrangement(seating)
        print("{}: {} seats\n\n".format(numRounds, getNumSeats(seating)))
        currState = ''
        for row in seating:
            currState += ''.join(row)
        numRounds += 1

execute(seating)


