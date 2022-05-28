from typing import Union
import math

class CalcMath:
  PI = 3.14159265358979323846264338
  e = 2.718281828459045235360287471
  
  def abs_val(val: Union[int, float]) -> Union[int, float]:
    return val if val >= 0 else -val
  
  def sign(val: Union[int, float]) -> int:
    return 1 if val >= 0 else -1
  
  def sqrt(val: float, error: float=1E-11) -> float:
    x = val / 2
  
    while (CalcMath.abs_val(x * x - val) >= error):
      x = (x + (val / x)) / 2
  
    return x
  
  def factorial(n: int) -> int:
    sol = 1
    for i in range(1, n + 1):
      sol *= i
      
    return sol
  '''
  def taylor(val: Union[float, int], coefficient: float, term: int, center: float=0) -> float:
    return coefficient * CalcMath.ipow(val - center, term) / CalcMath.factorial(term)
  '''
    
  def sin(x: float, error: float=1E-11) -> float:
      x = x % (2 * math.pi)
      n = 0
      result = 0
      # while the next term is greater than our error
      while CalcMath.abs_val(((-1) ** n * (x) ** (2*n + 1)) / (CalcMath.factorial(2*n + 1))) > error:
          result += ((-1) ** n * (x) ** (2*n + 1)) / (CalcMath.factorial(2*n + 1)) # add to result
          n += 1
      return result
  
  def cos(x: float, error: float=1E-11) -> float:
    return CalcMath.sin(x + CalcMath.PI / 2, error)
  
  def tan(x: float, error: float=1E-11) -> float:
    val = CalcMath.cos(x, error)
    if val == 0:
      return float('inf')
      
    return CalcMath.sin(x, error) / val
  
  def sec(x: float) -> float:
    val = CalcMath.cos(x)
    if val == 0:
      return float('inf')
    return 1.0 / CalcMath.cos(x)
  
  def csc(x: float) -> float:
    val = CalcMath.sin(x)
    if val == 0:
      return float('inf')
    return 1.0 / CalcMath.sin(x)
  def arctan(x: float, error: float=2E-7) -> float:
    x = x % (2 * CalcMath.PI)
    n = 0
    result = 0
    # while the next term is greater than our error
    while CalcMath.abs_val(((-1) ** n * (x) ** (2 * n + 1)) / (2 * n + 1)) > error:
        # print(n)
        result += ((-1) ** n * (x) ** (2 * n + 1)) / (2 * n + 1) # add to result
        n += 1
    return result
  # this is super dumb lol
  def arccos(x: float, error: float=1E-5):
    if(x > 1 or x < -1):
      raise Exception("Domain error: The domain is [-1, 1]")
    step = 0.001
    i = 0
    while(i <= 2 * CalcMath.PI):
      if(CalcMath.cos(i) >= x - error and CalcMath.cos(i) <= x + error):
        return i
      if(i + step >= 2 * CalcMath.PI):
        i = 0
        step /= 10
      i += step
  def natural_log(x: float):
    if(x <= 0):
      raise Exception("Domain Error: The domain is (0, inf)")
    
    # use Euler's method
    y0 = 0
    step = (x - 1) / CalcMath.ipow(10, len(str(x)) - 2)
    x0 = 1
    while(x0 <= x):
      derivative = 1 / x0
      y0 = y0 + step * derivative
      x0 += step
    return y0

  def ipow(base: Union[int, float], power: int) -> int:
    if power < 0:
      raise Exception("ipow not used for negatives")

    if power == 0:
      return 1
      
    if power % 2 == 0:
      return CalcMath.ipow(base * base, power / 2)

    return base * CalcMath.ipow(base, power - 1)
      
  # def pow(base: Union[float, int], power: Union[float, int]) -> Union[float, int]:
      