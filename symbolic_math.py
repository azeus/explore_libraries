from sympy import *

M = Matrix([[1, 2, 3], [3, 2, 1]])
N = Matrix([0, 1, 1])
print(M*N)


x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(diff(cos(x), x))
print(diff(exp(x**2), x))

print(integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))