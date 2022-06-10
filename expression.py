from term import *
from calcmath import *
from queue import Queue

'''
Formatting for our parsing:

  - Read left to right
  - Follows PEMDAS
  - Allows for parenthesis
  - Every token will be space seperated
  - Allows for default operations
  - Only allows for one variable which will be represented by x
  - Other operations:
    - s : sin()
    - c : cos()
    - t : tan()
    - as : arcsin()
    - ac : arccos()
    - at : arctan()
    - ^ : exponent
    - ln : natural log
    - log : log
      - value log base 
  - Ex : 1 + ( x + 9 ) ^ 3 - e ^ ( 5 * x )

'''


def isnumeric(val: str):
    try:
        float(val)
        return True
    except:
        return False


functions = ['s', 'c', 't', 'as', 'ac', 'at', 'ln']

flip = ['^']

pemdas = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    'log': 3,
    '(': -100,
    ')': 100
}

for i in functions:
    pemdas[i] = 4


def parse(expression: str):
    output = Queue()
    operator = []

    for i, token in enumerate(expression):
        if token == 'x':
            output.put('x')
        elif isnumeric(token):
            output.put(NumTerm(float(token)))
        elif token == '(':
            operator.append(token)
        elif token == ')':
            try:
                while operator[-1] != '(':
                    output.put(operator.pop())
                operator.pop()

                if len(operator) != 0 and operator[-1] in functions:
                    output.put(operator.pop())
            except:
                print('invalid')
                exit(-1)
        elif token in functions:
            operator.append(token)
        elif token in pemdas:
            while len(operator) != 0 and (pemdas[token] < pemdas[operator[-1]] or (pemdas[token] == pemdas[operator[-1]] and not (token in flip))):
                output.put(operator.pop())
            operator.append(token)
        else:
            print('invalid')
            exit(-1)

    while len(operator) > 0:
        output.put(operator.pop())

    output_term = None
    terms = []

    output = list(output.queue)
    print(output)

    while len(output) > 0:
        t = output.pop(0)

        if t == 'x':
            output_term = PolyTerm(1, 1)
            terms.append(output_term)
        elif t in pemdas:
            if t == '+':
                output_term = MultiTerm([terms.pop(), terms.pop()])
                terms.append(output_term)
            elif t == '-':
                output_term = MultiTerm([ProductTerm(
                    terms.pop(), NumTerm(-1)), terms.pop()])
                terms.append(output_term)
            elif t == '*':
                output_term = ProductTerm(terms.pop(), terms.pop())
                terms.append(output_term)
            elif t == '/':
                output_term = DivTerm(terms.pop(), terms.pop())
                terms.append(output_term)
            elif t == 's':
                output_term = SinTerm(1, terms.pop())
                terms.append(output_term)
            elif t == 'c':
                output_term = CosTerm(1, terms.pop())
                terms.append(output_term)
            elif t == 't':
                output_term = TanTerm(1, terms.pop())
                terms.append(output_term)
            elif t == 'ln':
                output_term = LogTerm(1, CalcMath.e, terms.pop())
                terms.append(output_term)
            elif t == 'log':
                output_term = LogTerm(1, terms.pop(), terms.pop())
                terms.append(output_term)
            elif t == '^':
                power = terms.pop()

                if isinstance(power, NumTerm):
                    power = power.num

                    output_term = PowTerm(1, terms.pop(), power)
                    terms.append(output_term)
                else:
                    print('cant do this yet')
            else:
                print("BAD: ", end=' ')
                print(t)
        else:
            terms.append(t)
        
    print(output_term)
    return output_term
