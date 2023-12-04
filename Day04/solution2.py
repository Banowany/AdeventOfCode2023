with open('Day04/input.in', 'r') as file:
    lines = file.read().splitlines()

def list_of_string_numbers_to_list_of_number(string_of_list_number):
    return [int(num) for num in string_of_list_number.split()]

winning_and_recived_as_string = [x.split(': ')[1] for x in lines]
winning_and_recived_as_pair_of_string = [(x.split(' | ')[0], x.split(' | ')[1]) for x in winning_and_recived_as_string]
winning_and_recived = [(list_of_string_numbers_to_list_of_number(x[0]), list_of_string_numbers_to_list_of_number(x[1])) for x in winning_and_recived_as_pair_of_string]

result = [1 for _ in range(len(winning_and_recived))]
for (i, (winning, received)) in enumerate(winning_and_recived):
    match_quantity = 0
    for x in winning:
        for y in received:
            if x == y:
                match_quantity += 1
    for j in range(match_quantity):
        if i + j + 1 >= len(winning_and_recived):
            continue
        result[i + j + 1] += result[i]

print(sum(result))