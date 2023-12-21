import re


def count_hash(word):
    result = 0
    for sign in word:
        result += ord(sign)
        result *= 17
        result %= 256
    return result

def map_words(word):
    match = re.match(r'(\w+)(=\d+|-)', word)
    if match:
        signs = match.group(1)
        operator = match.group(2)[0]
        if operator == '=':
            number = int(match.group(2)[1:])
        else:
            number = -1
        return (signs, operator, number)
    else:
        return None

with open('Day15/input.in', 'r') as file:
    words = file.read().split(',')

labels_operations_focals = [map_words(word) for word in words]
boxes = [{} for _ in range(256)]
for i, (label, operation, focal) in enumerate(labels_operations_focals):
    hashv = count_hash(label)
    if operation == '=':
        if label in boxes[hashv]:
            tmp = boxes[hashv][label]
            boxes[hashv][label] = (focal, tmp[1])
        else:
            boxes[hashv][label] = (focal, i)
    else:
        try:
            boxes[hashv].pop(label)
        except KeyError:
            pass

result = 0
for i, box in enumerate(boxes):
    values = list(box.values())
    values.sort(key = lambda x : x[1])
    for j, value in enumerate(values):
        tmp = (i+1) * (j+1) * value[0]
        print((i+1, j+1, value[0]))
        result += tmp

print(result)