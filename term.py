from __future__ import annotations
from typing import List

import calcmath

### TERM ###


class Term():

    def solve(self, x: float) -> float:
        raise NotImplementedError

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        return (self.solve(x + error) - self.solve(x)) / error

    def deriv_term(self) -> Term:
        raise NotImplementedError

    def integral_solve(self, left: float, right: float, error: float = 1E-3) -> float:
        x = left
        area = 0

        while x < right:
            area += (self.solve(x) + self.solve(x + error)) * error / 2
            x += error

        return area

    def integral_term(self) -> Term:
        raise NotImplementedError

    def graph(self, left: float, right: float):
        x = []
        y = []
        i = left
        while(i <= right):
            x.append(i)
            y.append(self.solve(i))
            i += 0.001
        return [x, y]

    def newtonsmethod(self, start, error=1E-8):
        x = start
        while(calcmath.CalcMath.abs_val(self.solve(x))):
            x = x - (self.solve(x) / self.deriv_solve(x))
            print(x)
        return x

    # def __iter__(self):
    #   self.iter = True
    #   return self

    # def __next___(self):
    #   if self.iter:
    #     self.iter = False
    #     return self

    #   raise StopIteration

    def __repr__(self):
        return f"Term: ({self.__str__()})"


### MULTITERM ###
class MultiTerm(Term):
    def __init__(self, terms: List[Term]):
        self.terms = terms

    def solve(self, x: float) -> float:
        sol = 0

        for term in self.terms:
            sol += term.solve(x)

        return sol

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        sol = 0

        for term in self.terms:
            sol += term.deriv_solve(x, error)

        return sol

    def deriv_term(self) -> Term:
        deriv = []

        for term in self.terms:
            deriv.append(term.deriv_term())

        return MultiTerm(deriv)

    def integral_solve(self, left: float, right: float, error: float = 1E-3) -> float:
        sol = 0

        for term in self.terms:
            sol += term.integral_solve(left, right, error)

        return sol

    def integral_term(self) -> Term:
        integral = []

        for term in self.terms:
            integral.append(term.integral_term())

        return MultiTerm(integral)

    def __str__(self):
        return f"[{' + '.join(str(i) for i in self.terms)}]"


### PRODUCTTERM ###
class ProductTerm(Term):
    def __init__(self, l: Term, r: Term):
        self.l = l
        self.r = r

    def solve(self, x: float) -> float:
        return self.l.solve(x) * self.r.solve(x)

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        return self.l.deriv_solve(x, error) * self.r.solve(x) + self.r.deriv_solve(x, error) * self.l.solve(x)

    def deriv_term(self) -> Term:
        return MultiTerm([ProductTerm(self.l.deriv_term(), self.r), ProductTerm(self.r.deriv_term(), self.l)])

    def __str__(self):
        return f"({str(self.l)} * {str(self.r)})"


### DIVTERM ###
class DivTerm(Term):
    def __init__(self, n: Term, d: Term):
        self.n = n
        self.d = d

    def solve(self, x: float) -> float:
        return self.n.solve(x) / self.d.solve(x)

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        return (self.d.solve(x) * self.n.deriv_solve(x, error) - self.n.solve(x) * self.d.deriv_solve(x, error)) / (calcmath.CalcMath.ipow(self.d.solve(x), 2))

    def deriv_term(self) -> Term:
        return DivTerm(MultiTerm([ProductTerm(self.d, self.n.deriv_term()), ProductTerm(-self.n, self.d.deriv_term())]), ProductTerm(self.d, self.d))

    def __str__(self):
        return f"({str(self.n)} / {str(self.d)})"

### NUMTERM ###


class NumTerm(Term):
    def __init__(self, num: float):
        self.num = num

    def solve(self, x: float) -> float:
        return self.num

    def deriv_solve(self, x: float, error: float = 1E-1) -> float:
        return 0

    def deriv_term(self) -> Term:
        return NumTerm(0)

    def integral_solve(self, left: float, right: float, error: float = 1E-1) -> float:
        integral = self.integral_term()
        return integral.solve(right) - integral.solve(left)

    def integral_term(self) -> Term:
        return PolyTerm(self.num, 1)

    def __str__(self):
        return f"{self.num}"

    def __float__(self):
        return self.num

    def __int__(self):
        return int(self.__float__())


### POLYTERM ###
class PolyTerm(Term):

    def __init__(self, coefficient: float, exponent: int):
        self.coefficient = coefficient
        self.exponent = exponent

        if self.exponent <= 0:
            raise Exception("polyterm cannot have non natural number input")

    def solve(self, x: float) -> float:
        return self.coefficient * calcmath.CalcMath.ipow(x, self.exponent)

    def deriv_solve(self, x: float, error: float = 1E-1) -> float:
        return self.deriv_term().solve(x)

    def deriv_term(self) -> Term:
        if self.exponent == 1:
            return NumTerm(self.coefficient)

        return PolyTerm(self.coefficient * self.exponent, self.exponent - 1)

    def integral_solve(self, left: float, right: float, error: float = 1E-1) -> float:
        integral = self.integral_term()
        return integral.solve(right) - integral.solve(left)

    def integral_term(self) -> Term:
        return PolyTerm(self.coefficient / (self.exponent + 1), self.exponent + 1)

    def __str__(self):
        return f"({self.coefficient}x^{self.exponent})"


### POWTERM ###
class PowTerm(Term):
    def __init__(self, coefficient: float, base: Term, exponent: float):
        self.coefficient = coefficient
        self.base = base
        self.exponent = exponent

    def solve(self, x: float):
        return self.coefficient * calcmath.CalcMath.pow(self.base.solve(x), self.exponent, 1E-3)

    def deriv_term(self) -> Term:
        if self.exponent == 1:
            return ProductTerm(NumTerm(self.coefficient), self.base)

        return ProductTerm(self.base.deriv_term(), PowTerm(self.coefficient * self.exponent, self.base, self.exponent - 1))

    def integral_solve(self, left: float, right: float, error: float = 1E-3):
        return super().integral_solve(left, right, error)

    def __str__(self):
        return f"({self.coefficient} * {str(self.base)}^{self.exponent})"


### EXPTERM ###
class ExpTerm(Term):
    def __init__(self, coefficient: float, base: float, exp: Term):
        self.coefficient = coefficient
        self.base = base
        self.exp = exp

    def solve(self, x: float) -> float:
        return self.coefficient * calcmath.CalcMath.pow(self.base, self.exp.solve(x))

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        return self.deriv_term().solve(x)

    def deriv_term(self) -> Term:
        return ProductTerm(self.exp.deriv_term(), DivTerm(ExpTerm(self.coefficient, self.base, self.exp), NumTerm(calcmath.CalcMath.natural_log(self.base))))

    def __str__(self):
        return f"{self.coefficient} * {self.base} ^ {self.exp}"


### LOGTERM ###
class LogTerm(Term):
    def __init__(self, coefficient: float, base: float, value: Term):
        self.coefficient = coefficient
        self.base = base
        self.value = value

    def solve(self, x: float) -> float:
        return self.coefficient * calcmath.CalcMath.log(self.value.solve(x), self.base)

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        return self.deriv_term().solve()

    def deriv_term(self) -> Term:
        return DivTerm(self.value.deriv_term(), ProductTerm(LogTerm(1, CalcMath.calcmath.e, base), value))

    def __str__(self):
        return f"({self.coefficient} * log base {self.base} of {str(self.value)})"


### SINTERM ###
class SinTerm(Term):
    def __init__(self, coefficient: float, value: Term):
        self.coefficient = coefficient
        self.value = value

    def solve(self, x: float) -> float:
        return self.coefficient * calcmath.CalcMath.sin(self.value.solve(x))

    def deriv_solve(self, x: float, error: float =1E-11) -> float:
        return self.deriv_term().solve(x)

    def deriv_term(self) -> Term:
        return ProductTerm(self.value.deriv_term(), CosTerm(self.coefficient, self.value))

    def __str__(self):
        return f"{self.coefficient} * sin({self.value})"



### COSTERM ###
class CosTerm(Term):
    def __init__(self, coefficient: float, value: Term):
        self.coefficient = coefficient
        self.value = value

    def solve(self, x: float) -> float:
        return self.coefficient * calcmath.CalcMath.cos(self.value.solve(x))

    def deriv_solve(self, x: float, error: float = 1E-11) -> float:
        return self.deriv_term().solve(x)

    def deriv_term(self) -> Term:
        return ProductTerm(self.value.deriv_term(), SinTerm(self.coefficient, self.value))

    def __str__(self):
        return f"{self.coefficient} * cos({self.value})"
