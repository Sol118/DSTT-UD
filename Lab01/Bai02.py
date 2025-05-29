#2.1
from sympy import Symbol
x = Symbol('x')
f = x+x + x + 2
print(f)

a = Symbol('Noi')
b = Symbol('Chim')
print(3*b + 7*a)

a= Symbol('Noi')
b= Symbol('Chim')
print(a.name)
print(b.name)

x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)

p = x*(x+2*x)
print(p)

p = (x+2)*(y+3) 
print(p)

p = (x+2)*(y+3) + (x+2)*(x-3) 
print(p)

p = x*(-x+2*x-x)
print(p)

p = (x+2)+(x+3)
print(p.expand())

print("\n")

#2.2.1
from sympy import factor
bieuthuc = x**3 - y**3
print(factor(bieuthuc))

from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))

print("\n")

#2.2.3
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y 
print(bieuthuc)
    
giatri = bieuthuc.subs({x: 3, y: 2})
print(giatri)

print(x)
print(y)