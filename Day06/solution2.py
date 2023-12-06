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

print(count_how_many_solutions(44826981, 202107611381458))