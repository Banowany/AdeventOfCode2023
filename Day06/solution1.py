import math

def count_how_many_solutions(time, distance):
    delta = time**2 - 4*distance
    if delta > 0:
        x1 = (time + math.sqrt(delta)) / 2
        x2 = (time - math.sqrt(delta)) / 2
        
        x1 = int(x1)
        while x1 * x1 - time * x1 + distance >= 0:
            x1 -= 1

        x2 = int(x2)
        while x2 * x2 - time * x2 + distance >= 0:
            x2 += 1
        
        return x1 - x2 + 1

time_and_distance = [(44, 202), (82, 1076), (69, 1138), (81, 1458)]
results = [count_how_many_solutions(record[0], record[1]) for record in time_and_distance]
solution = 1
for result in results:
    solution *= result
print(solution)