def find_starting_point(grid: [str]) -> (int, int):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return (i, j)
    return None
    

with open('Day21/example.in', 'r') as file:
    grid = file.read().splitlines()

starting_point = find_starting_point(grid)

#Krok 0
reached_garden_plots = set()
reached_garden_plots.add(starting_point)
reached_garden_plots_counter = {}


n = len(grid)
for i in range(100):
    new_garden_plots = set()
    new_garden_plots_counter = {}
    for point in reached_garden_plots:
        x, y = point
        # Check up
        if grid[(x-1)%n][y] != '#':
            new_garden_plots.add(((x-1)%n, y))
        # Check left
        if grid[x][(y-1)%n] != '#':
            new_garden_plots.add((x, (y-1)%n))
            if (x, (y-1)%n) in new_garden_plots_counter:
                new_garden_plots_counter[(x, (y-1)%n)] = new_garden_plots_counter[(x, (y-1)%n)] + quantity
            else:
                new_garden_plots_counter[(x, (y-1)%n)] = quantity
        # Check down
        if grid[(x+1)%n][y] != '#':
            new_garden_plots.add(((x+1)%n, y))
            if ((x+1)%n, y) in new_garden_plots_counter:
                new_garden_plots_counter[((x+1)%n, y)] = new_garden_plots_counter[((x+1)%n, y)] + quantity
            else:
                new_garden_plots_counter[((x+1)%n, y)] = quantity
        # Check right
        if grid[x][(y+1)%n] != '#':
            new_garden_plots.add((x, (y+1)%n))
            if (x, (y+1)%n) in new_garden_plots_counter:
                new_garden_plots_counter[(x, (y+1)%n)] = new_garden_plots_counter[(x, (y+1)%n)] + quantity
            else:
                new_garden_plots_counter[(x, (y+1)%n)] = quantity
    reached_garden_plots = new_garden_plots
    reached_garden_plots_counter = new_garden_plots_counter

print(len(reached_garden_plots))