import heapq


def dijkstra(grid):
    visited = set()
    pq = [(0, 0, 0, (0, 0, 0, 0))]

    rows_num = len(grid)
    columns_num = len(grid[0])
    while pq:
        d, r, c, (dc, uc, lc, rc) = heapq.heappop(pq)

        if r == rows_num - 1 and c == columns_num - 1:
            print(d)
            break

        if r < 0 or r >= rows_num:
            continue
        if c < 0 or c >= columns_num:
            continue
        if (r, c, (dc, uc, lc, rc)) in visited:
            continue
        
        visited.add((r, c, (dc, uc, lc, rc)))

        if dc < 3 and r < rows_num - 1 and uc == 0:
            heapq.heappush(pq, (d + grid[r+1][c], r+1, c, (dc+1, 0, 0, 0)))
        if uc < 3 and r > 0 and dc == 0:
            heapq.heappush(pq, (d + grid[r-1][c], r-1, c, (0, uc+1, 0, 0)))
        if lc < 3 and c > 0 and rc == 0:
            heapq.heappush(pq, (d + grid[r][c-1], r, c-1, (0, 0, lc+1, 0)))
        if rc < 3 and c < columns_num - 1 and lc == 0:
            heapq.heappush(pq, (d + grid[r][c+1], r, c+1, (0, 0, 0, rc+1)))

with open('Day17/input.in', 'r') as file:
    grid = file.read().splitlines()

grid = [[int(char) for char in line] for line in grid]
dijkstra(grid)