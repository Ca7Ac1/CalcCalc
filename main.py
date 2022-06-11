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
sound = False
func = ""
app = tk.Tk()
inputFrame = tk.Frame(app)
inp = tk.Entry(inputFrame, width=22, font=("Comic Sans", 22), justify="right")
inp.config(state="readonly")
funcFrame = tk.Frame(app)
fun = tk.Entry(funcFrame, width=22, font=("Comic Sans", 22))
fun.config(state="readonly")
helpFrame = tk.Frame(app)
def silly():
    global sound
    sound = not(sound)
def plus():
    global parsing_string
    parsing_string += " + "
    update_gui()
    if(sound):
        playsound(f"{path}/plus.wav")
def minus():
    global parsing_string
    parsing_string += " - "
    update_gui()
    if(sound):
        playsound(f"{path}/minus.wav")
def times():
    global parsing_string
    parsing_string += " * "
    update_gui()
    if(sound):
        playsound(f"{path}/times.wav")
def divide():
    global parsing_string
    parsing_string += " / "
    update_gui()
    if(sound):
        playsound(f"{path}/divided by.wav")
def zero():
    global parsing_string
    parsing_string += "0"
    update_gui()
    if(sound):
        playsound(f"{path}/0.wav")
def one():
    global parsing_string
    parsing_string += "1"
    update_gui()
    if(sound):
        playsound(f"{path}/1.wav")
def two():
    global parsing_string
    parsing_string += "2"
    update_gui()
    if(sound):
        playsound(f"{path}/2.wav")
def three():
    global parsing_string
    parsing_string += "3"
    update_gui()
    if(sound):
        playsound(f"{path}/3.wav")
def four():
    global parsing_string
    parsing_string += "4"
    update_gui()
    if(sound):
        playsound(f"{path}/4.wav")
def five():
    global parsing_string
    parsing_string += "5"
    update_gui()
    if(sound):
        playsound(f"{path}/5.wav")
def six():
    global parsing_string
    parsing_string += "6"
    update_gui()
    if(sound):
        playsound(f"{path}/6.wav")
def seven():
    global parsing_string
    parsing_string += "7"
    update_gui()
    if(sound):
        playsound(f"{path}/7.wav")
def eight():
    global parsing_string
    parsing_string += "8"
    update_gui()
    if(sound):
        playsound(f"{path}/8.wav")
def nine():
    global parsing_string
    parsing_string += "9"
    update_gui()
    if(sound):
        playsound(f"{path}/9.wav")
def equals():
    global func
    global parsing_string
    print(parsing_string)
    if(sound):
        playsound(f"{path}/is.wav")
    expr_string = parsing_string
    parsing_string = ""
    update_gui()
    expr = parse(expr_string.split())
    print(expr)
    if("x" in str(expr)):
        func = expr
        update_gui("Function set.")
        fun.config(state="normal")
        fun.delete(0, 'end')
        fun.insert(0, str(func))
        fun.config(state="readonly")
    else:
        try:
            update_gui(expr.solve(0))
            read_ans(expr.solve(0))
        except:
            update_gui("error")
    
def sin():
    global parsing_string
    parsing_string += " s "
    update_gui()
    if(sound):
        playsound(f"{path}/the sine of.wav")
def cos():
    global parsing_string
    parsing_string += " c "
    update_gui()
    if(sound):
        playsound(f"{path}/cosine.wav")
def tan():
    global parsing_string
    parsing_string += " t "
    update_gui()
    if(sound):
        playsound(f"{path}/the tangent of.wav")
def nl():
    global parsing_string
    parsing_string += " ln "
    update_gui()
    if(sound):
        playsound(f"{path}/natural log.wav")
def log():
    global parsing_string
    parsing_string += " log "
    update_gui()
    if(sound):
        playsound(f"{path}/the log base.wav")
def exp():
    global parsing_string
    parsing_string += " ^ "
    update_gui()
    if(sound):
        playsound(f"{path}/to the power of.wav")
def point():
    global parsing_string
    parsing_string += "."
    update_gui()
    if(sound):
        playsound(f"{path}/point.wav")
def lparen():
    global parsing_string
    parsing_string += " ( "
    update_gui()
    if(sound):
        playsound(f"{path}/paren.wav")
def rparen():
    global parsing_string
    parsing_string += " ) "
    update_gui()
    if(sound):
        playsound(f"{path}/paren.wav")
def atan():
    global parsing_string
    parsing_string += " at "
    update_gui()
    if(sound):
        playsound(f"{path}/the inverse tangent of.wav")
def e():
    global parsing_string
    parsing_string += str(CalcMath.e)
    update_gui()
    if(sound):
        playsound(f"{path}/e.wav")
def pi():
    global parsing_string
    parsing_string += str(CalcMath.PI)
    update_gui()
    if(sound):
        playsound(f"{path}/pi.wav")
def x():
    global parsing_string
    parsing_string += " x "
    update_gui()
    if(sound):
        playsound(f"{path}/x.wav")
def solve():
    global func
    global parsing_string
    expr_string = parsing_string
    parsing_string = ""
    ans = func.solve(int(expr_string))
    if(sound):
        playsound(f"{path}/solve.wav")
    update_gui(ans)
    read_ans(ans)
def deriv():
    global func
    global parsing_string
    expr_string = parsing_string
    parsing_string = ""
    ans = func.deriv_solve(int(expr_string))
    if(sound):
        playsound(f"{path}/derivative.wav")
    update_gui(ans)
    read_ans(ans)
def graph():
    global func
    global parsing_string
    expr_string = parsing_string
    parsing_string = ""
    if(sound):
        playsound(f"{path}/graphing.wav")
    update_gui()
    inputs = expr_string.split()
    fig, ax = plt.subplots()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    data = func.graph(int(inputs[0]), int(inputs[1]))
    print(data)
    x = data[0]
    # ax.set_xlim(xmin=-10, xmax=10)
    y = data[1]
    # ax.set_ylim(ymin=-10, ymax=10)
    ax.plot(x, y, linewidth=2)
    plt.show()
def integ():
    global func
    global parsing_string
    expr_string = parsing_string
    parsing_string = ""
    if(sound):
        playsound(f"{path}/the integral of.wav")
    inputs = expr_string.split()
    print(inputs)
    ans = func.integral_solve(int(inputs[0]), int(inputs[1]))
    update_gui(ans)
    read_ans(ans)
def roots():
    global func
    global parsing_string
    expr_string = parsing_string
    parsing_string = ""
    if(sound):
        playsound(f"{path}/roots.wav")
    ans = func.newtonsmethod(int(expr_string))
    update_gui(ans)
    read_ans(ans)
def space():
    global parsing_string
    parsing_string += " "
    update_gui()
    if(sound):
        playsound(f"{path}/space.wav")
def negate():
    global parsing_string
    parsing_string += "-"
    update_gui()
    if(sound):
        playsound(f"{path}/negative.wav")
def update_gui(toRender=None):
    global inp
    global parsing_string
    if(toRender == None):
        toRender = parsing_string
    inp.config(state="normal")
    inp.delete(0, 'end')
    inp.insert(0, toRender)
    inp.config(state="readonly")
def read_ans(ans):
    if(sound):
        for i in str(ans):
            if(i == "."):
                playsound(f"{path}/point.wav")
            elif(i == "-"):
                playsound(f"{path}/negative.wav")
            else:
                playsound(f"{path}/{i}.wav")
def help_out():
    print("Most of the calculator is self explanatory, but the function stuff is a little bit annoying to use.\nWhen you input something containing x and hit =, your input is saved in the function bar (at the bottom). You can then do five operations with this function: solve at a value, find the derivative at a value, find the integral over a range, graph it over a range, or find the roots (starting at a value). To use any of these, simply type the required number of arguments (1 or 2) separated by a space into the calculator, and then press whichever button corresponds to the operation you want to perform.\nSolve, derivative, and roots take 1 argument, and integral and graph take 2.\n Example: \n If I put x^2 into the calculator already, I can then type 2 and then hit the solve button. The calculator will return 4. If I put 2 4 and hit graph, the function will be graphed from x=2 to x=4. If I put 8 and hit roots, the function will try and find the root closest to 8.")

buttonFrame = tk.Frame(app)
buttons = [
    tk.Button(buttonFrame, text="+", command=plus, width=7, height=2), 
    tk.Button(buttonFrame, text="7", command=seven, width=7),
    tk.Button(buttonFrame, text="8", command=eight, width=7),
    tk.Button(buttonFrame, text="9", command=nine, width=7),
    tk.Button(buttonFrame, text="pi", command=pi, width=7),
    tk.Button(buttonFrame, text="e", command=e, width=7),
    tk.Button(buttonFrame, text="-", command=minus, height=2),
    tk.Button(buttonFrame, text="4", command=four),
    tk.Button(buttonFrame, text="5", command=five),
    tk.Button(buttonFrame, text="6", command=six),
    tk.Button(buttonFrame, text="ln", command=nl),
    tk.Button(buttonFrame, text="log", command=log),
    tk.Button(buttonFrame, text="*", command=times, height=2),
    tk.Button(buttonFrame, text="1", command=one),
    tk.Button(buttonFrame, text="2", command=two),
    tk.Button(buttonFrame, text="3", command=three),
    tk.Button(buttonFrame, text="space", command=space),
    tk.Button(buttonFrame, text="^", command=exp, width=7),
    tk.Button(buttonFrame, text="÷", command=divide, height=2),
    tk.Button(buttonFrame, text="negate", command=negate),
    tk.Button(buttonFrame, text="0", command=zero),
    tk.Button(buttonFrame, text=".", command=point),
    tk.Button(buttonFrame, text="(", command=lparen),
    tk.Button(buttonFrame, text=")", command=rparen),
    tk.Button(buttonFrame, text="=", command=equals, height=2),
    tk.Button(buttonFrame, text="x", command=x),
    tk.Button(buttonFrame, text="sin", command=sin),
    tk.Button(buttonFrame, text="cos", command=cos),
    tk.Button(buttonFrame, text="tan", command=tan),
    tk.Button(buttonFrame, text="arctan", command=atan),
    tk.Button(buttonFrame, text="???", command=silly, height=2), 
    tk.Button(buttonFrame, text="solve", command=solve),
    tk.Button(buttonFrame, text="derivative", command=deriv),
    tk.Button(buttonFrame, text="integral", command=integ),
    tk.Button(buttonFrame, text="graph", command=graph),
    tk.Button(buttonFrame, text="roots", command=roots),
    tk.Button(helpFrame, text="help (outputs in console)", command=help_out, width=50, height=2)
]

inputFrame.pack()
buttonFrame.pack()
funcFrame.pack()
helpFrame.pack()
inp.grid()
fun.grid()
row = 0
col = 0
for i in buttons:
    i.grid(row=row, column=col, sticky="nsew")
    col += 1
    if(col == 6):
        row += 1
        col = 0
# app.master.title('CalcCalc')
app.mainloop()



