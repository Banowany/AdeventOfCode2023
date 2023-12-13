from collections import deque
import re

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

def bfs(loop, starting_location, visited):
    queue = deque()
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

north_connection = is_north_possible(lines, location_of_S)
south_connection = is_south_possible(lines, location_of_S)
west_connection = is_west_possible(lines, location_of_S)
east_connection = is_east_possible(lines, location_of_S)


line = lines[location_of_S[0]]
if north_connection and south_connection:
    line = line[:location_of_S[1]] +  '|' + line[location_of_S[1] + 1:]
elif east_connection and west_connection:
    line = line[:location_of_S[1]] +  '-' + line[location_of_S[1] + 1:]
elif east_connection and north_connection:
    line = line[:location_of_S[1]] +  'L' + line[location_of_S[1] + 1:]
elif north_connection and west_connection:
    line = line[:location_of_S[1]] +  'J' + line[location_of_S[1] + 1:]
elif south_connection and west_connection:
    line = line[:location_of_S[1]] +  '7' + line[location_of_S[1] + 1:]
else:
    line = line[:location_of_S[1]] +  'F' + line[location_of_S[1] + 1:]

# print(line)
lines[location_of_S[0]] = line

visited = set()
max_distance = bfs(lines, location_of_S, visited)

not_loop_locations = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if not (i, j) in visited:
            not_loop_locations.append((i, j))
    
def replace(match):
    matched_text = match.group(0)
    replacement = '-' * len(matched_text)
    return replacement

for i in range(len(lines)):
    lines[i] = re.sub(r'L-*J', replace, lines[i])
    lines[i] = re.sub(r'F-*7', replace, lines[i])

how_many_dot_inside = 0
for dot_location in not_loop_locations:
    i = dot_location[0]
    # print(lines[i])
    crosses_left_vertical = 0
    for j in range(dot_location[1]):
        if (i, j) in visited and (lines[i][j] == '|' or lines[i][j] == 'J' or lines[i][j] == '7'):
            crosses_left_vertical += 1
        # if (i, j) in visited and (lines[i][j] == 'F' or lines[i][j] == 'L'):
        #     crosses_left -= 1
    # crosses_right = 0
    # for j in range(dot_location[1] + 1, len(lines[i])):
    #     if (i, j) in visited and (lines[i][j] == '|' or lines[i][j] == 'F' or lines[i][j] == 'L'):
    #         crosses_right += 1
        
    if crosses_left_vertical % 2 == 1: #and crosses_right % 2 == 1:
        print(dot_location)
        how_many_dot_inside += 1
print(how_many_dot_inside)