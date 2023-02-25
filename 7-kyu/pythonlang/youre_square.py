# You're a Square ! [https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python]
import math

def is_square(n):    
    sqrt_result = 0
    if n < 0:
        return False
    
    sqrt_result = math.sqrt(n)
    return sqrt_result.is_integer()