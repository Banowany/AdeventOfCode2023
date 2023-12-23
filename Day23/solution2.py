
def dfs(grid: [str], source: (int, int), target: (int, int)):
    
    stack = [(source, 0, set())]
    
    result = 0
    while stack:
        curr, length, visited = stack.pop()    
        
        if curr == target:
            result = max(result, length)
        
        visited.add(curr)
        
        row, col = curr
        neighbours = []
        if row > 0 and grid[row - 1][col] != '#':
            neighbours.append((row - 1, col))
        if row < n-1 and grid[row + 1][col] != '#':
            neighbours.append((row + 1, col))
        if col > 0 and grid[row][col - 1] != '#':
            neighbours.append((row, col - 1))
        if col < n-1 and grid[row][col + 1] != '#':
            neighbours.append((row, col + 1))
        
        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append((neighbour, length + 1, visited.copy()))
        
    return result

with open('Day23/input                    .in', 'r') as file:
    grid = file.read().splitlines()

n = len(grid)

source = (0, grid[0].index('.'))
target = (n - 1, grid[n - 1].index('.'))

result = dfs(grid, source, target)
print(result)
   