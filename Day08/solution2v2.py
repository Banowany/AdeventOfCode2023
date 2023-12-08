from math import gcd

def nww(a, b):
    return a*b // gcd(a, b)

def count_steps(connections, start):
    current = start
    how_many_jump = 0
    while True:
        for step in steps:
            how_many_jump += 1
            if step == 'L':
                current = connections[current][0]
            else:
                current = connections[current][1]
            if current[2] == 'Z':
                break
        if current[2] == 'Z':
            break
    return how_many_jump

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

jumps_for_everyone = [count_steps(connections, start) for start in starting]
common_jump = 1
for jump in jumps_for_everyone:
    common_jump = nww(common_jump, jump)
print(common_jump)