# Odd or Even? []https://www.codewars.com/kata/5949481f86420f59480000e7/train/python]
def odd_or_even(arr):
    return 'even' if sum(num for num in arr) % 2 == 0 else 'odd' 