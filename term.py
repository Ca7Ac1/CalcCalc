from __future__ import annotations
from typing import List

import calcmath

### TERM ###
class Term():

  def solve(self, x: float) -> float:
    raise NotImplementedError

  def deriv_solve(self, x: float, error: float=1E-11) -> float:
    return (self.solve(x + error) - self.solve(x)) / error

  def deriv_term(self) -> Term:
    raise NotImplementedError

  def integral_solve(self, left: float, right: float, error: float=1E-3) -> float:
    x = left
    area = 0

    while x < right:
      area += (self.solve(x) + self.solve(x + error)) * error / 2
      x += error 

  def integral_term(self) -> Term:
    raise NotImplementedError

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

  def deriv_solve(self, x: float, error: float=1E-11) -> float:
    sol = 0
    
    for term in self.deriv_term().terms:
      sol += term.solve(x)

    return sol

  def deriv_term(self) -> Term:
    deriv = []

    for term in self.terms:
      deriv.append(term.deriv_term())

    return MultiTerm(deriv)

  def integral_solve(self, left: float, right: float, error: float=1E-3) -> float:
    sol = 0
    
    for term in self.integral_term().terms:
      sol += term.solve(left, right, error)

    return sol 

  def integral_term(self) -> Term:
    integral = []

    for term in self.terms:
      integral.append(term.integral_term())

    return MultiTerm(integral)

  def __str__(self):
    return f"[{' + '.join(str(i) for i in self.terms)}]"

### NUMTERM ###
class NumTerm(Term):
  def __init__(self, num: float):
    self.num = num

  def solve(self, x: float) -> float:
    return self.num

  def deriv_solve(self, x: float) -> float:
    return self.num

  def deriv_term(self) -> Term:
    return NumTerm(0)

  def integral_solve(self, left: float, right: float) -> float:
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

  def deriv_solve(self, x: float) -> float:
    return self.deriv_term().solve(x)

  def deriv_term(self) -> Term:
    if self.exponent == 1:
      return NumTerm(self.coefficient)
      
    return PolyTerm(self.coefficient * self.exponent, self.exponent - 1)

  def integral_solve(self, left: float, right: float) -> float:
    integral = self.integral_term()
    return integral.solve(right) - integral.solve(left)

  def integral_term(self) -> Term:
    return PolyTerm(self.coefficient / (self.exponent + 1), self.exponent + 1)

  def __str__(self):
    return f"({self.coefficient}x^({self.exponent}))"


### POWTERM ###
class PowTerm(PolyTerm):
  def __init__(self, coefficient: float, exponent: int):
    self.coefficient = coefficient
    self.exponent = exponent

  def solve(self, x: float):
    return self.coefficient * calcmath.CalcMath.pow(x, self.exponent)
  
  def deriv_term(self) -> Term:
    if self.exponent == 1:
      return NumTerm(self.coefficient)

    return PowTerm(self.coefficient * self.exponent, self.exponent - 1)
  
  def integral_term(self) -> Term:
    if self.exponent == -1:
      #TODO: add ln here
      return NumTerm(0)

    return PowTerm(self.coefficient / (self.exponent + 1), self.exponent + 1)


### EXPTERM ###
class ExpTerm(Term):
  def __init__(self, coefficient: float, base: float, exp: Term):
    self.coefficient = coefficient
    self.base = base
    self.exp = exp
    
  def solve(self, x: float) -> float:
    e = 0

    for term in self.exp:
      e += term.solve()
    
    return self.coefficient * calcmath.CalcMath.pow(self.base, e)

  def deriv_solve(self, x: float, error: float=1E-11) -> float:
    return self.deriv_term().solve(x)

  def deriv_term(self) -> Term:
    #TODO: Do this
    return 0

  def integral_solve(self, left: float, right: float, error: float=1E-3) -> float:
    x = left
    area = 0

    while x < right:
      area += (self.solve(x) + self.solve(x + error)) * error / 2
      x += error 

  def integral_term(self) -> Term:
    raise NotImplementedError

  def __repr__(self):
    return f"Term: ({self.__str__()})"


### LNTERM ###
class LnTerm(Term):
  def __init__(self, coefficient, term: Term):
    self.term = Term
  
  def solve(self, x: float) -> float:
    raise NotImplementedError

  def deriv_solve(self, x: float, error: float=1E-11) -> float:
    return (self.solve(x + error) - self.solve(x)) / error

  def deriv_term(self) -> Term:
    raise NotImplementedError

  def integral_solve(self, left: float, right: float, error: float=1E-3) -> float:
    x = left
    area = 0

    while x < right:
      area += (self.solve(x) + self.solve(x + error)) * error / 2
      x += error 

  def integral_term(self) -> Term:
    raise NotImplementedError

  def __repr__(self):
    return f"Term: ({self.__str__()})"
