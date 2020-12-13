#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()
busesRaw = lines[1].strip().split(',')

def readData(lines):
    waitTime = int(lines[0].strip())
    busesStr = lines[1].strip().split(',')
    buses = []
    for s in busesStr:
        if s != 'x':
            buses.append(int(s))
    return waitTime, buses

def getEarliestBus(waitTime, buses):
    found = False
    while found != True:
        for bus in buses:
            if waitTime % bus == 0:
                print("Found bus {} at time {}".format(bus, waitTime))
                return waitTime, bus
        waitTime += 1

waitTime, buses = readData(lines)

print("Wait: " + str(waitTime))
print("Buses: {}".format(buses))

departure, bus = getEarliestBus(waitTime, buses)

print("Part 1: " + str((departure - waitTime) * bus))

def part2(buses):
    i = 1
    time = int(buses[0])
    inc = int(buses[0])
    while i < len(buses):
        if buses[i] == 'x':
            print("Nothing to do for index: " + str(i))
            i += 1
        else:
            if (time + i) % int(buses[i]) == 0:
                print("got time {} up to {}".format(time, i))
                inc *= int(buses[i])
                i += 1
            else:
                time += inc
    print("Part 2: " + str(time))

part2(busesRaw)
