from collections import deque

def is_north_possible(loop, starting_location):
    if starting_location[0] - 1 < 0:
        return False
    start_sign = loop[starting_location[0]][starting_location[1]]
    north_sign = loop[starting_location[0] - 1][starting_location[1]]
    if start_sign == 'S' or start_sign == '|' or start_sign == 'L' or start_sign == 'J':
        return north_sign == '|' or north_sign == '7' or north_sign == 'F'
    else:
        return False
    
def is_south_possible(loop, starting_location):
    if starting_location[0] + 1 >= len(loop):
        return False
    start_sign = loop[starting_location[0]][starting_location[1]]
    south_sign = loop[starting_location[0] + 1][starting_location[1]]
    if start_sign == 'S' or start_sign == '|' or start_sign == '7' or start_sign == 'F':
        return south_sign == '|' or south_sign == 'L' or south_sign == 'J'
    else:
        return False

def is_west_possible(loop, starting_location):
    if starting_location[1] - 1 < 0:
        return False
    start_sign = loop[starting_location[0]][starting_location[1]]
    west_sign = loop[starting_location[0]][starting_location[1] - 1]
    if start_sign == 'S' or start_sign == '-' or start_sign == 'J' or start_sign == '7':
        return west_sign == '-' or west_sign == 'L' or west_sign == 'F'
    else:
        return False

def is_east_possible(loop, starting_location):
    if starting_location[1] + 1 >= len(loop[0]):
        return False
    start_sign = loop[starting_location[0]][starting_location[1]]
    east_sign = loop[starting_location[0]][starting_location[1] + 1]
    if start_sign == 'S' or start_sign == '-' or start_sign == 'L' or start_sign == 'F':
        return east_sign == '-' or east_sign == 'J' or east_sign == '7'
    else:
        return False

def bfs(loop, starting_location):
    queue = deque()
    visited = set()
    max_distance = 0
    queue.append((starting_location, 0))
    while queue:
        current_location, distance = queue.popleft()
        if current_location in visited:
            continue
        max_distance = max(max_distance, distance)
        visited.add(current_location)
        
        if is_north_possible(loop, current_location):
            queue.append(((current_location[0] - 1, current_location[1]), distance + 1))
        if is_south_possible(loop, current_location):
            queue.append(((current_location[0] + 1, current_location[1]), distance + 1))
        if is_west_possible(loop, current_location):
            queue.append(((current_location[0], current_location[1] - 1), distance + 1))
        if is_east_possible(loop, current_location):
            queue.append(((current_location[0], current_location[1] + 1), distance + 1))
    
    return max_distance

with open('Day10/input.in', 'r') as file:
    lines = file.read().splitlines()

for i, line in enumerate(lines):
    if 'S' in line:
        location_of_S = (i, line.index('S'))
        break

max_distance = bfs(lines, location_of_S)
print(max_distance)