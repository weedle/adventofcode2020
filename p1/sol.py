#!/usr/bin/python3
# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()

# Parse data and prepare storage variables
values = []

for line in lines:
    values.append(int(line))

values.sort()

# Build solution
#   Part 1
def part1(values):
    valuesReversed = values.copy()
    valuesReversed.reverse()
    for val in values:
        for valR in valuesReversed:
            sum1 = val + valR
            if sum1 == 2020:
                print("  Found solution: {} and {}, product is {}".format(str(val), str(valR), str(val*valR)))
                return
            if sum1 < 2020:
                break

def part2(values):
    valuesReversed = values.copy()
    valuesReversed.reverse()
    for val in values:
        for valB in values:
            for valR in valuesReversed:
                sum2 = val + valB + valR
                if sum2 == 2020:
                    print("  Found solution: {}, {}, and {}, product is {}".format(str(val), str(valB), str(valR), str(val*valB*valR)))
                    return
                if sum2 < 2020:
                    break

# Call req functions
print("Calculating solution for part 1:")
part1(values)
print("Calculating solution for part 2:")
part2(values)
