with open('Day08/input.in', 'r') as file:
    lines = file.read().splitlines()

steps = lines[0]
lines = lines[2:]
connections = {}
starting = []
for line in lines:
    parent = line[0:3]
    if parent[2] == 'A':
        starting.append(parent)
    left = line[7:10]
    right = line[12:15]
    connections[parent] = (left, right)

how_many_jump = 0
currents = starting
while True:
    for step in steps:
        how_many_z = 0
        how_many_jump += 1
        for i, current in enumerate(currents):
            if step == 'L':
                currents[i] = connections[current][0]
            else:
                currents[i] = connections[current][1]
            if currents[i][2] == 'Z':
                how_many_z += 1
            if how_many_z == len(currents):
                print(how_many_jump)
                break
        print(currents)
        if how_many_z == len(currents):
            break
    if how_many_z == len(currents):
            break