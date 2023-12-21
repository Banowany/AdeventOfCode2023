def count_hash(word):
    result = 0
    for sign in word:
        result += ord(sign)
        result *= 17
        result %= 256
    return result

with open('Day15/input.in', 'r') as file:
    words = file.read().split(',')

hashed_words = [count_hash(word) for word in words]
print(sum(hashed_words))