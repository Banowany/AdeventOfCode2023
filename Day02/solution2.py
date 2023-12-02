with open('Day02/input', 'r') as file:
    lines = file.read().splitlines()

game_results = [line.split(": ")[1] for line in lines] #index = gameID - 1

result = 0

for i, game_result in enumerate(game_results):
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in game_result.split("; "):
        for node in set.split(", "):
            quantity = int(node.split(" ")[0])
            color = node.split(" ")[1]
            if color == "red" and quantity > max_red:
                max_red = quantity
            elif color == "green" and quantity > max_green:
                max_green = quantity
            elif color == "blue" and quantity > max_blue:
                max_blue = quantity
    result += (max_red * max_green * max_blue)

print(result)
