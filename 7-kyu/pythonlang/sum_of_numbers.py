def get_sum(a,b):
    if a == b:
        return a
    else:
        sum = 0
        if a < b:
            for x in range(a, b+1):
                sum += x
        else:
            for x in range(b, a+1):
                sum += x
            
        return sum
    
get_sum(789, 45)