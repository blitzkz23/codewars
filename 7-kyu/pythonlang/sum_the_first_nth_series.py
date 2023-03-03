# Sum of the first nth term of Series [https://www.codewars.com/kata/555eded1ad94b00403000071/train/python]
def series_sum(n):
    numerator = 1
    denumerator = 4
    sum = 0
    if n == 0:
        return '0.00'
    if n == 1:
        return '1.00'

    for i in range (0, n-1):
        if i == 0:
            sum += numerator/(denumerator)
        else:
            denumerator = denumerator + 3 
            sum += numerator/(denumerator)
    return f'{1+sum:.2f}'

# People one liner
def series_sum2(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
