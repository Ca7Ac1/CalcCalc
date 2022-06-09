from calcmath import CalcMath
from term import *
import math
import matplotlib.pyplot as plt

# hello


# exp = ExpTerm(1, CalcMath.e, PolyTerm(1, 1))
# print(exp.solve(1.1))
# print(exp.solve(1.2))
# print(exp.deriv_solve(1.1, 1E-19))
# print(exp.deriv_term())

# print(CalcMath.pow(2.1, 2.1, 1E-7))

# poly = ProductTerm(PolyTerm(7, 2), MultiTerm([PolyTerm(9, 2), NumTerm(-5)]))
# print(f"Solved at 2: {poly.solve(2)}")
# print(f"Derivative: {poly.deriv_term()}")
# print(f"Integral solved between -1 and 1: {poly.integral_solve(-1, 1)}")
# print("\n")
# print(poly.newtonsmethod(.2))

# expr = ProductTerm(PolyTerm(1, 1), SinTerm(1, DivTerm(NumTerm(1), PolyTerm(1, 1))))
expr = SinTerm(1, PolyTerm(1, 1))
fig, ax = plt.subplots()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
data = expr.graph(-20, 20)
x = data[0]
ax.set_xlim(xmin=-20, xmax=20)
y = data[1]
ax.set_ylim(ymin=-1.2, ymax=1.2)
ax.plot(x, y, linewidth=2)
plt.show()


