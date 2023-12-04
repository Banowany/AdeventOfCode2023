with open('Day04/input.in', 'r') as file:
    lines = file.read().splitlines()

def list_of_string_numbers_to_list_of_number(string_of_list_number):
    return [int(num) for num in string_of_list_number.split()]

winning_and_recived_as_string = [x.split(': ')[1] for x in lines]
winning_and_recived_as_pair_of_string = [(x.split(' | ')[0], x.split(' | ')[1]) for x in winning_and_recived_as_string]
winning_and_recived = [(list_of_string_numbers_to_list_of_number(x[0]), list_of_string_numbers_to_list_of_number(x[1])) for x in winning_and_recived_as_pair_of_string]

result = 0
for winning, received in winning_and_recived:
    match_quantity = 0
    for x in winning:
        for y in received:
            if x == y:
                match_quantity += 1
    tmp = 0
    for _ in range(match_quantity):
        if tmp == 0:
            tmp = 1
        else:
            tmp *= 2
    result += tmp

print(result)