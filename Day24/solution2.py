import numpy
import re


class Hail:
    def __init__(self, position, velocity) -> None:
        self.p = position
        self.v = velocity
    
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

from sympy import symbols, Eq, solve

# Definiuj symbole
x_0, y_0, z_0, vx_0, vy_0, vz_0, k, l, m = symbols('a,b,c,d,e,f,g,h,i')
x_1, y_1, z_1 = hails[0].p 
vx_1, vy_1, vz_1 = hails[0].v
x_2, y_2, z_2 = hails[1].p
vx_2, vy_2, vz_2 = hails[1].v
x_3, y_3, z_3 = hails[2].p
vx_3, vy_3, vz_3 = hails[2].v

# Definiuj równania
eqs = [
    Eq(x_0+k*vx_0-x_1-k*vx_1, 0),
    Eq(y_0+k*vy_0-y_1-k*vy_1, 0),
    Eq(z_0+k*vz_0-z_1-k*vz_1, 0),
    Eq(x_0+l*vx_0-x_2-l*vx_2, 0),
    Eq(y_0+l*vy_0-y_2-l*vy_2, 0),
    Eq(z_0+l*vz_0-z_2-l*vz_2, 0),
    Eq(x_0+m*vx_0-x_3-m*vx_3, 0),
    Eq(y_0+m*vy_0-y_3-m*vy_3, 0),
    Eq(z_0+m*vz_0-z_3-m*vz_3, 0)
    ]

# Rozwiązuj układ równań
solution = solve(eqs, (x_0, y_0, z_0, vx_0, vy_0, vz_0, k, l, m))

# Wyświetl wyniki
print("Rozwiązanie:")
print(solution)

print(solution[0][0] + solution[0][1] + solution[0][2])
