from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**2 - x*y + y**2
print(bieuthuc)

bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print(bieuthuc_moi)

from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)

from sympy import Symbol
from sympy import sin, cos 
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)
