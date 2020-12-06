file1 = open('data.txt', 'r') 
lines = file1.readlines() 
trees = 0
x = 0
slopeX = 1
slopeY = 2

def do_line(line):
    global trees
    print('{} {}'.forrmat(len(line), line))

print(len(lines))
for y in range(0, len(lines), slopeY):
    trimmed = lines[y].strip()
    line = list(trimmed)
    if line[x] == '#':
        line[x] = 'X'
        trees += 1
    else:
        line[x] = 'O'
    x += slopeX
    x = x % len(line)
    print(''.join(line))

print("Encountered " + str(trees) + " trees")
