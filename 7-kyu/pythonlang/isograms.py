# Isograms [https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python]
def is_isogram(string):
    arr = []
    for char in string:
        char = char.lower()
        if char not in arr:
            arr.append(char)
        else:
            return False
    return True

# People one liner
def is_isogram(string):
    return len(string) == len(set(string.lower()))