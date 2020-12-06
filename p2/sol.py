file1 = open('data.txt', 'r') 
lines = file1.readlines() 
good = 0

def do_line(line):
    global good
    data = line.split(' ')
    
    minVal, maxVal = data[0].split('-')
    charReq = data[1][0]
    password = data[2]
    count = password.count(charReq)
    
    if(count >= int(minVal) and count <= int(maxVal)):
        good += 1
        print(' passed: {}, has {} {}\'s and needs {}-{}'.format(password, count, charReq, minVal, maxVal))
    else:
        print('    failed: {}, has {} {}\'s but needs {}-{}'.format(password, count, charReq, minVal, maxVal))

for line in lines:
    do_line(line)

print(str(good) + ' passwords')
