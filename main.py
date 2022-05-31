from calcmath import CalcMath
from term import *
import math

a = MultiTerm([NumTerm(5), PolyTerm(5, 5), PolyTerm(6, 6)])
print(a.deriv_solve(1))