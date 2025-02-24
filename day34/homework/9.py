#9) codewars, Summing a number's digits

def sum_digits(number):
     return sum(int(digit) for digit in str(abs(number)))