# Square(n) Sum [https://www.codewars.com/kata/515e271a311df0350d00000f/train/python]
def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num**2
    return sum

# People one-liner
def square_sum2(numbers):
    return sum(x ** 2 for x in numbers)