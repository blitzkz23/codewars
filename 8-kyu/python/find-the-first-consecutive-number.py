# Find the first non-consecutive number [https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python]
def first_non_consecutive(arr):
    for num in range(len(arr)-1):
        if arr[num+1] - arr[num] != 1:
            return arr[num+1]
        
