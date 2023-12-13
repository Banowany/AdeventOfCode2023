
import re


def count_possibilites(spring, control_numbers):
    if '?' in spring:
        location = spring.index('?')
        spring1 = spring.copy()
        spring1[location] = '#'
        spring2 = spring.copy()
        spring2[location] = '.'
        return count_possibilites(spring1, control_numbers) + count_possibilites(spring2, control_numbers)
    else:
        spring_str = ''.join(spring)
        finded_element = re.findall(r'#+', spring_str)
        len_of_element = [len(x) for x in finded_element]

        return 1 if len_of_element == control_numbers else 0
        

    

with open('Day12/input.in', 'r') as file:
    lines = file.read().splitlines()

spring_and_control_numbers = [(line.split()[0], list(map(int, line.split()[1].split(',')))) for line in lines]
result = 0
for row in spring_and_control_numbers:
    result += count_possibilites(list(row[0]), row[1])
print(result)

