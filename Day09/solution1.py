def predict(step) -> int:
    if all(el == 0 for el in step):
        return 0
    next_step = [step[i+1]-step[i] for i in range(len(step)-1)]
    predicted = predict(next_step)
    return step[len(step)-1]+predicted

def line_to_int_array(line: str):
    string_numbers = line.split()
    numbers = [int(num) for num in string_numbers]
    return numbers


with open('Day09/input.in', 'r') as file:
    lines = file.read().splitlines()

history = [line_to_int_array(x) for x in lines]
results = [predict(x) for x in history]
print(sum(results))