# Find the odd int [https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python]

def find_it(seq):
    num_dict = {}
    for num in seq:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    for key, value in num_dict.items():
        if value % 2 == 1:
            return key

# People one-liner
def find_it2(seq):
    return [x for x in seq if seq.count(x) % 2][0]