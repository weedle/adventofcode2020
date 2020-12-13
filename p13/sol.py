#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()
waitTime = int(lines[0].strip())
buses = lines[1].strip().split(',')

def getEarliestBus(waitTime, buses):
    buses = [int(x) for x in buses if x != 'x']
    while True:
        for bus in buses:
            if waitTime % bus == 0:
                print("Found bus {} at time {}".format(bus, waitTime))
                return waitTime, bus
        waitTime += 1

print("Wait: " + str(waitTime))
print("Buses: {}".format(buses))

departure, bus = getEarliestBus(waitTime, buses)

print("Part 1: " + str((departure - waitTime) * bus))

def part2(buses):
    i = 1
    time = int(buses[0])
    inc = int(buses[0])
    while i < len(buses):
        while buses[i] == 'x':
            i += 1
        if (time + i) % int(buses[i]) == 0:
            print("  got time {} up to {}".format(time, i))
            inc *= int(buses[i])
            i += 1
        else:
            time += inc
    return time

print("Part 2: " + str(part2(buses)))
