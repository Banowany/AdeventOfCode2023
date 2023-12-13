def count_diffs_for_every_column_reflection(grid):
    diffs = []
    #reflection 0 mean reflection between 0 and 1
    n = len(grid[0])
    m = len(grid)
    for reflection in range(n-1):
        len_to_end = min(reflection + 1, n - reflection - 1)
        diff = 0
        for jump in range(len_to_end):
            for i in range(m):
                if grid[i][reflection-jump] != grid[i][reflection+jump+1]:
                    diff += 1
        diffs.append(diff)
    return diffs

def count_diffs_for_every_row_reflection(grid):
    diffs = []
    #reflection 0 mean reflection between 0 and 1
    n = len(grid[0])
    m = len(grid)
    for reflection in range(m-1):
        len_to_end = min(reflection + 1, m - reflection - 1)
        diff = 0
        for jump in range(len_to_end):
            for j in range(n):
                if grid[reflection-jump][j] != grid[reflection+jump+1][j]:
                    diff += 1
        diffs.append(diff)
    return diffs

with open('Day13/input.in', 'r') as file:
    lines = file.read().splitlines()

grids = []
tmp = []
for line in lines:
    if line == '':
        grids.append(tmp)
        tmp = []
    else:
        tmp.append(line)
grids.append(tmp)

result = 0
for grid in grids:
    diffs_column = (count_diffs_for_every_column_reflection(grid))
    diffs_row =(count_diffs_for_every_row_reflection(grid))
    for i, diff_column in enumerate(diffs_column):
        if diff_column == 1:
            result += i+1

    for i, diff_row in enumerate(diffs_row):
        if diff_row == 1:
            result += (i+1)*100

print(result)
