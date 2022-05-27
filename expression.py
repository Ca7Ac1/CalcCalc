from term import Term
  
class Expression:

  def __init__(self):
    self.terms = []
    
  def solve(self, x: float):
    sol = 0

    for i in self.terms:
      sol += i.solve()

    return sol
      
  def add(self, term: Term):
    self.terms.append(term)
    
  def clear(self):
    self.terms.clear()

