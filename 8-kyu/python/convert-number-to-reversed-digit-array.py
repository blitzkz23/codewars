# Convert number to reversed array of digits [https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python]
def digitize(n):
    newArr = []
    if n == 0:
        newArr.append(n)
    else:
        newArr = [*map(int,str(n))]
        newArr.reverse()
    return newArr

# People's one liner solution
def digitize(n):
    return map(int, str(n)[::-1])