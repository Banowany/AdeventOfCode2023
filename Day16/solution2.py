from collections import deque


def get_energized_tiles(grid, begin_beam, cache):
    queue = deque()
    queue.append(begin_beam)
    energized = set()
    visited = set()

    n = len(grid[0])
    m = len(grid)

    while queue:
        locationx, locationy, movex, movey = queue.popleft()
        if locationx < 0 or locationy < 0 or locationx >= n or locationy >= m:
            continue

        if (locationx, locationy, movex, movey) in visited:
            continue

        if (locationx, locationy, movex, movey) in cache:
            cached_energized = cache[(locationx, locationy, movex, movey)][0]
            cached_visited = cache[(locationx, locationy, movex, movey)][1]
            energized.union(cached_energized)
            visited.union(cached_visited)
            continue

        visited.add((locationx, locationy, movex, movey))
        energized.add((locationx, locationy))
        sign = grid[locationy][locationx]
        if sign == '.':
            queue.append((locationx + movex, locationy + movey, movex, movey))
        elif sign == '\\':
            movex, movey = movey, movex
            queue.append((locationx + movex, locationy + movey, movex, movey))
        elif sign == '/':
            movex, movey = -movey, -movex
            queue.append((locationx + movex, locationy + movey, movex, movey))
        elif sign == '|':
            if movex == 0:
                queue.append((locationx + movex, locationy + movey, movex, movey))
            else:
                queue.append((locationx, locationy + 1, 0, 1))
                queue.append((locationx, locationy - 1, 0, -1))
        else:
            if movey == 0:
                queue.append((locationx + movex, locationy + movey, movex, movey))
            else:
                queue.append((locationx + 1, locationy, 1, 0))
                queue.append((locationx - 1, locationy, -1, 0))
    return (energized, visited)


with open('Day16/input.in', 'r') as file:
    grid = file.read().splitlines()

cache = {}
n = len(grid[0])
m = len(grid)

maxv = 0
for x in range(n):
    beam = (x, 0, 0, 1)
    result = get_energized_tiles(grid, beam, cache)
    cache[beam] = result
    maxv = max(maxv, len(result[0]))

for x in range(n):
    beam = (x, m-1, 0, -1)
    result = get_energized_tiles(grid, beam, cache)
    cache[beam] = result
    maxv = max(maxv, len(result[0]))
    
for y in range(n):
    beam = (0, y, 1, 0)
    result = get_energized_tiles(grid, beam, cache)
    cache[beam] = result
    maxv = max(maxv, len(result[0]))

for y in range(n):
    beam = (n - 1, y, -1, 0)
    result = get_energized_tiles(grid, beam, cache)
    cache[beam] = result
    maxv = max(maxv, len(result[0]))


print(maxv)
