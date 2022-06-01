from calcmath import CalcMath
from term import *
import math

a = MultiTerm([NumTerm(5), PolyTerm(5, 5), PolyTerm(6, 6)])
print(a.integral_term())
print(a.integral_solve(1, 2))
print(a.deriv_term())
print(a.deriv_solve(1)
print(a)