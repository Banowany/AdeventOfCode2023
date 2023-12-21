from functools import cache


def tail(grid):
    n = len(grid)
    tailed_grid = [[''] * n for _ in range(n)]
    for j in range(n):
        stables_all_rocks = []
        stable = -1
        all = 1
        rocks = 0
        for i in range(n):
            all += 1
            if grid[i][j] == 'O':
                rocks += 1
            elif grid[i][j] == '#':
                stables_all_rocks.append((stable, all, rocks))
                stable = i
                all = 1
                rocks = 0
        stables_all_rocks.append((stable, all, rocks))
        for stable, all, rocks in stables_all_rocks:
            for i in range(max(stable, 0), stable + all):
                if i == stable:
                    tailed_grid[i][j] = '#'
                elif rocks > 0:
                    tailed_grid[i][j] = 'O'
                    rocks -= 1
                else:
                    tailed_grid[i][j] = '.'

    tailed_grid = [''.join(x) for x in tailed_grid]
    return tuple(tailed_grid)


def rotate_90_degrees(grid):
    n = len(grid)
    rotated_grid = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_grid[j][(n - 1) - i] = grid[i][j]

    rotated_grid = [''.join(x) for x in rotated_grid]

    return tuple(rotated_grid)

def cycle(grid):
    tailed_north = tail(grid)
    rotated_west = rotate_90_degrees(tailed_north)
    tailed_west = tail(rotated_west)
    rotated_south = rotate_90_degrees(tailed_west)
    tailed_south = tail(rotated_south)
    rotated_east = rotate_90_degrees(tailed_south)
    tailed_east = tail(rotated_east)
    return rotate_90_degrees(tailed_east) 

def count_total_load(grid):
    n = len(grid)
    result = 0
    for j in range(n):
        for i in range(n):
            if grid[i][j] == 'O':
                result += (n-i)

    return result

with open('Day14/input2.in', 'r') as file:
    lines = file.read().splitlines()

result = tuple(lines)
grid_to_cycle_cache = {}
cycle_to_grid_cache = {}
for i in range(1000000000): # 188 1000000000 I finded cycle in my solution where begin in 171 and length of it is 14
    if result in grid_to_cycle_cache:
        begin_of_cycle_of_cycle = grid_to_cycle_cache[result]
        len_of_cycle_of_cycle = i - begin_of_cycle_of_cycle
        aproprite_cycle_of_cycle = begin_of_cycle_of_cycle + (1000000000 - begin_of_cycle_of_cycle)%len_of_cycle_of_cycle
        print(count_total_load(cycle_to_grid_cache[aproprite_cycle_of_cycle]))
        break
    else:
        grid_to_cycle_cache[result] = i
        cycle_to_grid_cache[i] = result 
    result = cycle(result)