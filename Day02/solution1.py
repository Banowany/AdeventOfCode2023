with open('Day02/input', 'r') as file:
    lines = file.read().splitlines()

game_results = [line.split(": ")[1] for line in lines] #index = gameID - 1

result = 0
max_red = 12
max_green = 13
max_blue = 14

for i, game_result in enumerate(game_results):
    isPossible = True
    for set in game_result.split("; "):
        for node in set.split(", "):
            quantity = int(node.split(" ")[0])
            color = node.split(" ")[1]
            if color == "red" and quantity > max_red:
                isPossible = False
                break
            elif color == "green" and quantity > max_green:
                isPossible = False
                break
            elif color == "blue" and quantity > max_blue:
                isPossible = False
                break
        if isPossible == False:
            break
    if isPossible:
        result += (i + 1)

print(result)
