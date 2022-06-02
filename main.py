from calcmath import CalcMath
from term import *
import math
import matplotlib.pyplot as plt

exp = ExpTerm(1, CalcMath.e, PolyTerm(1, 1))
print(exp.solve(1.1))
print(exp.solve(1.2))
print(exp.deriv_solve(1.1, 1E-19))
print(exp.deriv_term())

# print(CalcMath.pow(2.1, 2.1, 1E-7))

# poly = ProductTerm(PolyTerm(7, 2), MultiTerm([PolyTerm(9, 2), NumTerm(-5)]))
# print(f"Solved at 2: {poly.solve(2)}")
# print(f"Derivative: {poly.deriv_term()}")
# print(f"Integral solved between -1 and 1: {poly.integral_solve(-1, 1)}")
# print("\n")
# print(poly.newtonsmethod(.2))

# fig, ax = plt.subplots()
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('center')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# data = poly.graph()
# x = data[0]
# ax.set_xlim(xmin=-10, xmax=10)
# y = data[1]
# ax.set_ylim(ymin=-10, ymax=10)
# ax.plot(x, y, linewidth=2)
# plt.show()


# a = ProductTerm([NumTerm(5), PolyTerm(5)])
