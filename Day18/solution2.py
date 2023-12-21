def shoelace_formula(points):
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # Wrap around to the first point

        area += (x1 * y2) - (x2 * y1)

    return abs(area) // 2

def get_distance_direction(code):
    code = code[1:-1]
    dis = int(code[1:-1], 16)  # Convert hex to decimal
    dir = code[-1]

    if dir == '0':
        dir = 'R'
    elif dir == '1':
        dir = 'D'
    elif dir == '2':
        dir = 'L'
    else:
        dir = 'U'

    return (dir, dis)

with open('Day18/input.in', 'r') as file:
    moves = [tuple(move.split()) for move in file.read().splitlines()]

points = [(0, 0)]
curr_point = (0, 0)
perimeter = 0
for _, _, r in moves:
    d, v = get_distance_direction(r)
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