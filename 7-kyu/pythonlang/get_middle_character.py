# Get the middle character [https://www.codewars.com/kata/56747fd5cb988479af000028/train/python]
import math

def get_middle(s):
    if len(s) % 2 == 1:
        mid = math.floor(len(s)/2)
        return s[mid]
    else:
        mid = round(len(s)/2)
        return s[mid-1:mid+1]
