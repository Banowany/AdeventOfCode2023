import re

def extract_numbers_with_location(text, line_id):
    pattern = r'\d+'
    results = [(m.start(), m.end() - 1, int(m.group()), line_id) for m in re.finditer(pattern, text)]
    return results

with open('Day03/input', 'r') as file:
    lines = file.read().splitlines()

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

numbers_with_location = []
for i, line in enumerate(lines):
    numbers_with_location.extend(extract_numbers_with_location(line, i))

final_sum = 0
for number_with_location in numbers_with_location:
    is_part_number = False
    for y in range(number_with_location[3] - 1, number_with_location[3] + 2):
        for x in range(number_with_location[0] - 1, number_with_location[1] + 2):
            if y < 0 or y > max_y:
                continue
            elif x < 0 or x > max_x:
                continue
            elif y == number_with_location[3] and number_with_location[0] <= x and x <= number_with_location[1]:
                continue

            if lines[y][x] != '.':
                is_part_number = True
    if is_part_number:
        final_sum += number_with_location[2]

print(final_sum)

