from functools import cache
import re

@cache
def dynimic_count(spring, control_numbers, curr_pos, num_of_processed_groups, len_of_processing_group):
    result = 0
    if curr_pos == len(spring):
        if num_of_processed_groups == len(control_numbers) and len_of_processing_group == 0:
            result = 1
        elif num_of_processed_groups == len(control_numbers) - 1 and control_numbers[num_of_processed_groups] == len_of_processing_group:
            result = 1
        else:
            result = 0
    elif spring[curr_pos] == '#':
        if num_of_processed_groups == len(control_numbers):
            result = 0
        elif len_of_processing_group == control_numbers[num_of_processed_groups]:
            result = 0
        else:
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups, len_of_processing_group + 1)
    elif spring[curr_pos] == '.':
        #1.Zwiekszyc ilosc grup gdy dlugosc odpowiednia
        #2.Gdy dlugosc sie nie zgadza zwroc zero
        #3.Gdy dlugosc zero pusc dalej
        if len_of_processing_group == 0:
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups, 0)
        elif len_of_processing_group == control_numbers[num_of_processed_groups]:
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups + 1, 0)
        # elif len_of_processing_group != 0:
        else:
            result = 0
            
    else:
        #1.gdy zero i ilosc grup odpowiednia to kropka
        #2.gdy dlugosc zero  i grup brakuje to oba wersje
        #3.gdy dlugosc niezerowa ale mniejsza od docelowej to hasztag
        #4.gdy dlugosc rowna zwroc kropke
        if len_of_processing_group == 0 and num_of_processed_groups == len(control_numbers):
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups, 0)
        elif len_of_processing_group == 0 and num_of_processed_groups < len(control_numbers):
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups, 0) + dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups, 1)
        elif len_of_processing_group < control_numbers[num_of_processed_groups]:
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups, len_of_processing_group + 1)
        else:
            result = dynimic_count(spring, control_numbers, curr_pos + 1, num_of_processed_groups + 1, 0)
    return result


def count_possibilites(spring, control_numbers):
    return dynimic_count(spring, control_numbers, 0, 0, 0)
        

    

with open('Day12/input.in', 'r') as file:
    lines = file.read().splitlines()

spring_and_control_numbers = [(line.split()[0], list(map(int, line.split()[1].split(',')))) for line in lines]
result = 0
for row in spring_and_control_numbers:
    new_spring = '?'.join([row[0]] * 5)
    new_control = row[1]*5
    tmp = count_possibilites(new_spring, tuple(new_control))
    print(tmp)
    result += tmp
print(result)

