# Printer Error [https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python]
def printer_error(s):
    # not error code are 'a' to 'm'
    error = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    denominator = len(s)
    numerator = 0
    
    for char in s:
        if char in error:
            numerator+=1
        
    return f'{numerator}/{denominator}'

# People one liner
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))