# Highest and Lowest [https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python]
def high_and_low(numbers):
    arr = numbers.split()
    num_arr = [int(i) for i in arr]
    lowest, highest = num_arr[0], num_arr[0]
    for num in num_arr:
        if num < lowest:
            lowest = num
        elif num > highest:
            highest = num
    return f"{highest} {lowest}"
        