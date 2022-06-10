from calcmath import CalcMath
from term import *
import math
import matplotlib.pyplot as plt
import tkinter as tk
from pathlib import Path
from playsound import playsound
from expression import *

path = Path(__file__).parent / 'voices/'
parsing_string = ""
sound = True


def silly():
    sound = not(sound)


def plus():
    global parsing_string
    parsing_string += "+ "
    playsound(f"{path}/plus.wav")


def minus():
    global parsing_string
    parsing_string += "- "
    playsound(f"{path}/minus.wav")


def times():
    global parsing_string
    parsing_string += "* "
    playsound(f"{path}/times.wav")


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        buttons = [tk.Button(self, text='Quit', command=self.quit), tk.Button(
            self, text="+", command=plus), tk.Button(self, text="-", command=minus), tk.Button(self, text="x", command=times)]
        for i in buttons:
            i.grid()

        # self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        # self.quitButton.grid()
        # self.plusButton = tk.Button(self, text="+", command=plus)
        # self.plusButton.grid()


# app = Application()
# app.master.title('Sample application')
# app.mainloop()

expr = parse(input().split())
print(expr.solve(5.7))
print(expr.deriv_term())
print(expr.deriv_solve(5.7))
fig, ax = plt.subplots()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
data = expr.graph(-5, 5)
x = data[0]
ax.set_xlim(xmin=-10, xmax=10)
y = data[1]
ax.set_ylim(ymin=-2, ymax=2)
ax.plot(x, y, linewidth=2)
plt.show()
