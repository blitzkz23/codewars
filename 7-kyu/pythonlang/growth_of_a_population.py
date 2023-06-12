# Growth of a Population [https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python]
import math

def nb_year(p0, percent, aug, p):
    n_year = 0
    while p0 <= p:
        p0 =  math.floor(p0 + p0 * (percent/100) + aug)
        n_year+=1
        if p0 >= p:
            return n_year
    

print(nb_year(1000, 2.0, 50, 1214))
