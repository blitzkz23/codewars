# Find the next square! [https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python]
import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt = math.isqrt(sq)
    if sqrt * sqrt == sq:
        return (sqrt + 1) ** 2
    else :
        return -1
