from __future__ import annotations

import calcmath

class Term():

  def solve(self, x: float) -> float:
    raise NotImplementedError

  def deriv_solve(self, x: float) -> float:
    raise NotImplementedError

  def deriv_term(self) -> Term:
    raise NotImplementedError

  def integral(self, x: float) -> float:
    raise NotImplementedError

  def integral_term(self) -> Term:
    raise NotImplementedError


class NumTerm():
  def __init__(self, num: float):
    self.num = num

  def solve(self, x: float) -> float:
    return self.num

  def deriv_solve(self, x: float) -> float:
    return self.num

  def deriv_term(self) -> Term:
    return 0

  def integral(self, x: float) -> float:
    return integral_term().solve(x)

  def integral_term(self) -> Term:
    return PolyTerm(self.num, 1)

  
class PolyTerm():

  def __init__(self, coefficient: float, exponent: float):
    self.coefficient = coefficient
    self.exponent = exponent

    if self.exponent == 0:
      raise Exception("polyterm cannot have 0 exponent")

  def solve(self, x: float) -> float:
    return self.coefficient * calcmath.CalcMath.pow(x, self.exponent)

  def deriv_solve(self, x: float) -> float:
    return self.deriv_term().solve(x)

  def deriv_term(self) -> Term:
    if self.exponent == 1:
      return NumTerm(self.coefficient)
      
    return PolyTerm(self.coefficient * self.exponent, self.exponent - 1)

  def integral(self, x: float) -> float:
    return self.integral_term().solve(x)

  def integral_term(self) -> Term:
    return PolyTerm(self.coefficient / (self.exponent + 1), self.exponent + 1)
  
    