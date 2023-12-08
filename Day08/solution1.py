with open('Day08/input.in', 'r') as file:
    lines = file.read().splitlines()

steps = lines[0]
lines = lines[2:]
connections = {}
for line in lines:
    parent = line[0:3]
    left = line[7:10]
    right = line[12:15]
    connections[parent] = (left, right)

current = 'AAA'
how_many_jump = 0
while True:
    for step in steps:
        how_many_jump += 1
        if step == 'L':
            current = connections[current][0]
        else:
            current = connections[current][1]
        if current == 'ZZZ':
            print(how_many_jump)
            break
    if current == 'ZZZ':
        break