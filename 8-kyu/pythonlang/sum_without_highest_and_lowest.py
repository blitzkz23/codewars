# Sum without highest and lowest number [https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python]
def sum_array(arr):
    if arr == None or arr == []:
        return 0
    if len(arr) == 1 or len(arr) == 2:
        return 0
    lowest, highest = arr[0], arr[0]
    sum = 0

    for num in arr:
        if num < lowest:
            lowest = num
        elif num > highest:
            highest = num
        sum += num
    
    return sum-lowest-highest
