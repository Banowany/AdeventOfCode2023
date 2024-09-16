def dfs(graph, source: (int, int), target: (int, int)):
    
    stack = [(source, 0, set())]
    
    result = 0
    while stack:
        curr, length, visited = stack.pop()    
        
        if curr == target:
            result = max(result, length)
            continue
        else:
            visited.add(curr)
        
        for neighbour in graph[curr]:
            if neighbour[0] not in visited:
                stack.append((neighbour[0], length + neighbour[1], visited.copy()))
        
    return result

def find_intersections(grid, source, target):
    stack = [source]
    visited = set()
    
    result = []
    while stack:
        curr= stack.pop()    
        
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
        
        count = 0
        for neighbour in neighbours:
            if neighbour not in visited:
                count += 1
                stack.append(neighbour)
        
        if count > 1:
            result.append(curr)
        
    return result

def build_intersection_graph(grid, source, target, intersections):
    intersections = set(intersections)
    
    graph = {}
    graph[source] = []
    graph[target] = []
    for intersection in intersections:
        graph[intersection] = []
        
    for intersection in intersections:
        stack = [(intersection, 0)]
        visited = set()
        
        while stack:
            curr, length = stack.pop()
            if curr == intersection:
                pass
            elif curr == source:
                graph[source].append((intersection, length))
                graph[intersection].append((source, length))
                continue
            elif curr == target:
                graph[target].append((intersection, length))
                graph[intersection].append((target, length))
                continue
            elif curr in intersections:
                graph[intersection].append((curr, length))
                continue
            
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
                    stack.append((neighbour, length + 1))
                         
    return graph
    

with open('Day23/input.in', 'r') as file:
    grid = file.read().splitlines()

n = len(grid)

source = (0, grid[0].index('.'))
target = (n - 1, grid[n - 1].index('.'))

intersections = find_intersections(grid, source, target)
graph = build_intersection_graph(grid, source, target, intersections)
print(graph)
result = dfs(graph, source, target)
print(result)
# result = dfs(grid, source, target)
# print(result)
   