from typing import List, Set


def get_columns_without_galaxy(image:List[str]) -> Set[int]:
    columns_without_galaxy = set()
    for j in range(len(image[0])):
        is_empty = True
        for i in range(len(image)):
            if image[i][j] == '#':
                is_empty = False
        if is_empty:
            columns_without_galaxy.add(j)
    return columns_without_galaxy

def get_rows_without_galaxy(image:List[str]) -> Set[int]:
    rows_without_galaxy = set()
    for i in range(len(image)):
        is_empty = True
        for j in range(len(image[0])):
            if image[i][j] == '#':
                is_empty = False
        if is_empty:
            rows_without_galaxy.add(i)
    return rows_without_galaxy

def find_galaxies(image:List[str]) -> list:
    galaxies = []
    for i, row in enumerate(image):
        for j, space in enumerate(row):
            if space == '#':
                galaxies.append((i, j))
    return galaxies



with open('Day11/input.in', 'r') as file:
    lines = file.read().splitlines()

columns_without_galaxy = get_columns_without_galaxy(lines)
rows_without_galaxy = get_rows_without_galaxy(lines)
galaxies = find_galaxies(lines)
results = []

for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        diff_x = abs(galaxy1[0] - galaxy2[0])
        diff_y = abs(galaxy1[1] - galaxy2[1])
        
        begin_x = min(galaxy1[0], galaxy2[0])
        end_x = max(galaxy1[0], galaxy2[0])

        for x in range(begin_x + 1, end_x):
            if x in rows_without_galaxy:
                diff_x += 999999

        begin_y = min(galaxy1[1], galaxy2[1])
        end_y = max(galaxy1[1], galaxy2[1])

        for y in range(begin_y + 1, end_y):
            if y in columns_without_galaxy:
                diff_y += 999999
        
        results.append(diff_x + diff_y)
print(results)
print(sum(results))