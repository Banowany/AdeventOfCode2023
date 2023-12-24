import numpy
import re


class Hail:
    def __init__(self, position, velocity) -> None:
        self.p = position
        self.v = velocity
    def position_in_which_time(self, position) -> float:
        return (position[0] - self.p[0]) / self.v[0]
        
def find_intersection(hail1, hail2):
    # p1, p2 - punkty na prostych
    # v1, v2 - wektory kierunkowe prostych

    det = hail1.v[0] * hail2.v[1] - hail1.v[1] * hail2.v[0]
    if det == 0:
        # Proste są równoległe, brak punktu przecięcia
        return None

    # Obliczanie parametrów t1 i t2
    t1 = ((hail2.p[0] - hail1.p[0]) * hail2.v[1] - (hail2.p[1] - hail1.p[1]) * hail2.v[0]) / det
    t2 = ((hail2.p[0] - hail1.p[0]) * hail1.v[1] - (hail2.p[1] - hail1.p[1]) * hail1.v[0]) / det

    # Obliczanie współrzędnych punktu przecięcia
    intersection_point = (hail1.p[0] + t1 * hail1.v[0], hail1.p[1] + t1 * hail1.v[1])

    return intersection_point

def to_hail(hail_string: str):
    # Extract numbers using regular expressions
    numbers = re.findall(r'-?\d+', hail_string)

    # Convert numbers into tuples
    point = tuple(map(int, numbers[:3]))
    velocity = tuple(map(int, numbers[3:]))

    return Hail(point, velocity)
    

with open('Day24/input.in', 'r') as file:
    hails_as_string = file.read().splitlines()

hails = [to_hail(x) for x in hails_as_string]

begin = 200000000000000
end = 400000000000000

result = 0
for i, hail1 in enumerate(hails):
    for hail2 in hails[i+1:]:
       intersection = find_intersection(hail1, hail2)
       if intersection is None:
           continue
       if hail1.position_in_which_time(intersection) < 0 or hail2.position_in_which_time(intersection) < 0:
           continue
       if intersection[0] >= begin and intersection[0] <=end:
           if intersection[1] >= begin and intersection[1] <=end:
               result += 1

print(result)