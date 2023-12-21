def find_starting_point(grid: [str]) -> (int, int):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return (i, j)
    return None
    

with open('Day21/input.in', 'r') as file:
    grid = file.read().splitlines()

starting_point = find_starting_point(grid)

#Krok 0
reached_garden_plots = set()
reached_garden_plots.add(starting_point)


n = len(grid)
for i in range(65):
    new_garden_plots = set()
    for point in reached_garden_plots:
        x, y = point
        # Check up
        if grid[(x-1)%n][y%n] != '#':
            new_garden_plots.add((x-1, y))
        # Check left
        if grid[x%n][(y-1)%n] != '#':
            new_garden_plots.add((x, y-1))
        # Check down
        if grid[(x+1)%n][y%n] != '#':
            new_garden_plots.add((x+1, y))
        # Check right
        if grid[x%n][(y+1)%n] != '#':
            new_garden_plots.add((x, y+1))
    reached_garden_plots = new_garden_plots

print(len(reached_garden_plots))

for i in range(131):
    new_garden_plots = set()
    for point in reached_garden_plots:
        x, y = point
        # Check up
        if grid[(x-1)%n][y%n] != '#':
            new_garden_plots.add((x-1, y))
        # Check left
        if grid[x%n][(y-1)%n] != '#':
            new_garden_plots.add((x, y-1))
        # Check down
        if grid[(x+1)%n][y%n] != '#':
            new_garden_plots.add((x+1, y))
        # Check right
        if grid[x%n][(y+1)%n] != '#':
            new_garden_plots.add((x, y+1))
    reached_garden_plots = new_garden_plots

print(len(reached_garden_plots))

for i in range(131):
    new_garden_plots = set()
    for point in reached_garden_plots:
        x, y = point
        # Check up
        if grid[(x-1)%n][y%n] != '#':
            new_garden_plots.add((x-1, y))
        # Check left
        if grid[x%n][(y-1)%n] != '#':
            new_garden_plots.add((x, y-1))
        # Check down
        if grid[(x+1)%n][y%n] != '#':
            new_garden_plots.add((x+1, y))
        # Check right
        if grid[x%n][(y+1)%n] != '#':
            new_garden_plots.add((x, y+1))
    reached_garden_plots = new_garden_plots

print(len(reached_garden_plots))

for i in range(131):
    new_garden_plots = set()
    for point in reached_garden_plots:
        x, y = point
        # Check up
        if grid[(x-1)%n][y%n] != '#':
            new_garden_plots.add((x-1, y))
        # Check left
        if grid[x%n][(y-1)%n] != '#':
            new_garden_plots.add((x, y-1))
        # Check down
        if grid[(x+1)%n][y%n] != '#':
            new_garden_plots.add((x+1, y))
        # Check right
        if grid[x%n][(y+1)%n] != '#':
            new_garden_plots.add((x, y+1))
    reached_garden_plots = new_garden_plots

print(len(reached_garden_plots))