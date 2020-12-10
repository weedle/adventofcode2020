#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()
preambleLength = 25

def doPreamble(nums):
    sums = []
    for i in range(0,len(nums)):
        subSums = []
        for j in range(i+1,len(nums)):
            subSums.append(nums[i] + nums[j])
        sums.append(subSums)
    return sums

def verifyNum(num, sums):
    pool = []
    for subarray in sums:
        for val in subarray:
            pool.append(val)
    result = num in pool
    return result


def part1(lines):
    nums = []
    for line in lines:
        nums.append(int(line.strip()))

    history = nums[0:preambleLength]
    sums = doPreamble(history)

    result = verifyNum(nums[preambleLength], sums)
    print("Verifying {}: {}".format(nums[preambleLength], result))

    if result == False:
        print("FOUND FAILURE FOR NUM: {}".format(nums[preambleLength]))
        return nums[preambleLength]

    for i in range(preambleLength+1,len(nums)):
        #print("Processing num: " + str(nums[i]))

        #print("  First: update history")
        history.pop(0)
        history.append(nums[i-1])
        #print("  History is now: {}".format(history))

        sums = doPreamble(history)
        #print("  Recalculate sums: {}".format(sums))

        result = verifyNum(nums[i], sums)
        print("    Verifying {}: {}".format(nums[i], result))
        if result == False:
            print("FOUND FAILURE FOR NUM: {}".format(nums[i]))
            return nums[i]

def part2(target):
    nums = []
    for line in lines:
        nums.append(int(line.strip()))

    for i in range(0,len(nums)):
        if nums[i] >= target:
            return
        sum = nums[i]
        for j in range(i+1,len(nums)):
            sum += nums[j]
            if sum == target:
                print("SUCCESS: {} -> {}".format(nums[i], nums[j]))
                minVal = nums[i]
                maxVal = nums[i]
                for k in range(i,j):
                    if minVal > nums[k]:
                        minVal = nums[k]
                    if maxVal < nums[k]:
                        maxVal = nums[k]
                print("MIN IS {}, MAX IS {}, SUM IS {}".format(minVal, maxVal, minVal + maxVal))
                return
            if sum > target:
                print("Sum from {}:{} to {}:{} failed".format(i, nums[i], j, nums[j]))
                break;
        #print("{}: {}".format(str(i), str(nums[i])))

part2(22477624)
