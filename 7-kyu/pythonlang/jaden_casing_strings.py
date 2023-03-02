# Jaden Casing Strings[https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python]
def to_jaden_case(string):
    splitted_string = string.split()
    arr = []
    for word in splitted_string:
        word = word.capitalize()
        arr.append(word)
    return ' '.join(map(str, arr))

# People one liner
def to_jaden_case2(string):
    return ' '.join(word.capitalize() for word in string.split())