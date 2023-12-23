
def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen, t_path))
    return paths

def longest_path(graph, source, target):
    paths = DFS(graph, source)
    target_paths = [path for path in paths if path[-1] == target]
    return max(len(path) for path in target_paths)

with open('Day23/input.in', 'r') as file:
    grid = file.read().splitlines()

n = len(grid)

source = (0, grid[0].index('.'))
target = (n - 1, grid[n - 1].index('.'))

graph = {}
for row in range(n):
    for col in range(n):
        if grid[row][col] == '>':
            graph[(row, col)] = [(row, col + 1)]
        elif grid[row][col] == '<':
            graph[(row, col)] = [(row, col - 1)]
        elif grid[row][col] == 'v':
            graph[(row, col)] = [(row + 1, col)]
        elif grid[row][col] == '^':
            graph[(row, col)] = [(row - 1, col)]
        elif grid[row][col] == '.':
            graph[(row, col)] = []
            if col + 1 < n and grid[row][col+1] != '#':
                graph[(row, col)].append((row, col+1))
            if col - 1 >= 0 and grid[row][col-1] != '#':
                graph[(row, col)].append((row, col-1))
            if row + 1 < n and grid[row+1][col] != '#':
                graph[(row, col)].append((row+1, col))
            if row - 1 >= 0 and grid[row-1][col] != '#':
                graph[(row, col)].append((row-1, col))

result = longest_path(graph, source, target)
print(result-1)
