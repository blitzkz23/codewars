# A Needle in the Haystack [https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python]
def find_needle(haystack):
    for index, value in enumerate(haystack):
        if (value == "needle"):
            return "found the needle at position {}".format(index)
        
# People one liner solution
def find_needle2(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))