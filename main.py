from calcmath import CalcMath
from term import *
import math
import matplotlib.pyplot as plt

poly = MultiTerm([PolyTerm(9, 2), NumTerm(-5)])
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

print(poly.newtonsmethod(2))
