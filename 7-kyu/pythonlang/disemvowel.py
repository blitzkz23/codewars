# Disemvowel [https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python]
def disemvowel(string_):
    vowels = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
    new_str = ''
    for word in string_:
        if word not in vowels:
            new_str = new_str + word
    return new_str