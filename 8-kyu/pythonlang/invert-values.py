# Invert Values [https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python]
def invert(lst):
    newArr = []
    for num in lst:
        num *= -1
        newArr.append(num)
    return newArr

# People's one liner solution
def invert2(lst):
   return [i*-1 for i in lst]

def invert3(lst):
    return list(map(lambda x: -x, lst));