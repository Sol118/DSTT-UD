from sympy import solve, Symbol
x = Symbol('x')
ptb2 = x**2 + 9*x +8 
print(solve(ptb2, dict = True))

ptb2 = x**2 + 1*x + 10
nghiemx = solve(ptb2, dict = True) 
print(nghiemx)
