#!/usr/bin/python3
# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()

def calculatePath(lines, slopes, display):
    x, trees = 0, 0
    for y in range(0, len(lines), slopes[1]):
        line = list(lines[y].strip())
        if line[x] == '#':
            line[x] = 'X'
            trees += 1
        else:
            line[x] = 'O'
        if(display):
            print(''.join(line))
        x += slopes[0]
        x = x % len(line)
    return trees

def calculateForAllSlopes(lines, display):
    allSlopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    allTrees = []
    for slopes in allSlopes:
        allTrees.append(calculatePath(lines, slopes, display))
    for slopes in allSlopes:
        print("For slope {} right and {} down, encountered {} trees".format(slopes[0], slopes[1], calculatePath(lines, slopes, False)))

calculateForAllSlopes(lines, False)
