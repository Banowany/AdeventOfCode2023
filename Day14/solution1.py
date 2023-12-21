def calculate_load(stable_and_rocks, rows_num):
    stable = stable_and_rocks[0]
    rounded_rocks =  stable_and_rocks[1]
    # -1 -> n, n-1, n-2, ...
    # 0 -> n-1, n-2, n-3, ...
    load = 0
    for single_load in range(rows_num - stable - rounded_rocks, rows_num - stable):
        load += single_load
    return load


with open('Day14/input.in', 'r') as file:
    lines = file.read().splitlines()

stables_and_rocks = []
for j in range(len(lines[0])):
    stableLocation = -1
    num_of_rounded_rocks = 0
    for i in range(len(lines)):
        if lines[i][j] == 'O':
            num_of_rounded_rocks += 1
        elif lines[i][j] == '#':
            if num_of_rounded_rocks > 0:
                stables_and_rocks.append((stableLocation, num_of_rounded_rocks))
            num_of_rounded_rocks = 0
            stableLocation = i
loads = [calculate_load(x, len(lines)-1) for x in stables_and_rocks]
print(sum(loads))