file1 = open('data.txt', 'r') 
lines = file1.readlines() 
 
values = []

# Strips the newline character 
for line in lines: 
    values.append(int(line))
    
values.sort()

valuesReversed = values.copy()
valuesReversed.reverse()

for val in values:
    for valB in values:
        for valR in valuesReversed:
            sum = val + valB + valR
            if sum == 2020:
                print("got 2020 with " + str(val) + ", " + str(valB) + " and " + str(valR))
                print("their product is " + str(val*valR*valB))
            if sum < 2020:
                break
