from sympy import solve
from sympy.abc import x, y, z
print(solve([x + y - 2*z, y + 4*z], [x, y], dict=True))