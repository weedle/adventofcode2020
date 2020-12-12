#!/usr/bin/python3
import re
import math

# Load file
datafile = open('data.txt', 'r')
lines = datafile.readlines()

class Pos:
    x = 0
    y = 0
    angle = 90

    def turn(self, deg):
        self.angle += deg
        self.angle = self.angle % 360

    def forward(self, units):
        self.x += units * math.sin(math.pi * self.angle / 180)
        self.y += units * math.cos(math.pi * self.angle / 180)

    def toString(self):
        return "({}, {}), facing {}".format(self.x, self.y, self.angle)

class Waypoint:
    x = 10
    y = 1

    def toString(self):
        return "({}, {})".format(self.x, self.y)

class Ship:
    pos = Pos()
    wp = Waypoint()

    def turn(self, deg):
        s = math.sin(math.pi * deg / 180)
        c = math.cos(math.pi * deg / 180)

        print(s)
        print(c)

        # rotate
        # had to change the sign of the sins FOR SOME REASON
        # TODO: probably figure out why I had to did that
        newX = self.wp.x * c + self.wp.y * s
        newY = -self.wp.x * s + self.wp.y * c

        self.wp.x = newX
        self.wp.y = newY

    def forward(self, units):
        self.pos.x += units * self.wp.x
        self.pos.y += units * self.wp.y

    def toString(self):
        return "Ship: {}, Waypoint: {}".format(self.pos.toString(), self.wp.toString())


# let's say N and E are + in their respective axes
ship = Ship()

for line in lines:
    line = line.strip()
    order = line[0]
    val = int(line[1:])
    #print("ORDER: " + order)
    #print("VAL: " + str(val))
    if order == "L":
        ship.turn(-val)
    elif order == "R":
        ship.turn(val)
    elif order == "N":
        ship.wp.y += val
    elif order == "S":
        ship.wp.y -= val
    elif order == "E":
        ship.wp.x += val
    elif order == "W":
        ship.wp.x -= val
    elif order == "F":
        ship.forward(val)
    else:
        print("Failed to interpret: " + line)
    print("After order {}, ship is {}".format(line, ship.toString()))

print("Manhatten distance is now:" + str(abs(ship.pos.x) + abs(ship.pos.y)))
