def shoelace_formula(points):
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # Wrap around to the first point

        area += (x1 * y2) - (x2 * y1)

    return abs(area) // 2

with open('Day18/input.in', 'r') as file:
    moves = [tuple(move.split()) for move in file.read().splitlines()]

points = [(0, 0)]
curr_point = (0, 0)
perimeter = 0
for d, sv, r in moves:
    v = int(sv)
    perimeter += v
    if d == 'R':
        curr_point = (curr_point[0] + v, curr_point[1])
    if d == 'L':
        curr_point = (curr_point[0] - v, curr_point[1])
    if d == 'U':
        curr_point = (curr_point[0], curr_point[1] + v)
    if d == 'D':
        curr_point = (curr_point[0], curr_point[1] - v)
    
    points.append(curr_point)

print(shoelace_formula(points) + perimeter // 2 + 1)