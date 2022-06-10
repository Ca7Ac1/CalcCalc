from term import *
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
      - base log value 
  - Ex : 1 + ( x + 9 ) ^ 3 - e ^ 5x

'''


def isnumeric(val: str):
    try:
        float(val)
        return True
    except:
        return False


functions = ['s', 'c', 't', 'as', 'ac', 'at', 'ln', 'base']

flip = ['^']

pemdas = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '(': -100,
    ')': 100
}

for i in functions:
    pemdas[i] = 4


def parse(expression: str):
    output = Queue()
    operator = []

    for i, token in enumerate(expression):
        if isnumeric(token):
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
            operator.append(pemdas[token])
        elif token in pemdas:
            while len(operator) != 0 and (pemdas[token] < pemdas[operator[-1]] or (pemdas[token] == pemdas[operator[-1]] and not (token in flip))):
                output.put(operator.pop())
            operator.append(token)
        else:
            print('invalid')
            exit(-1)

    while len(operator) > 0:
        output.put(operator.pop())

    print(list(output.queue))


parse('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'.split())
