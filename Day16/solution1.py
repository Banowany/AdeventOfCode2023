from collections import deque


with open('Day16/input.in', 'r') as file:
    grid = file.read().splitlines()

queue = deque()
queue.append((0, 0, 1, 0))
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

print(len(energized))