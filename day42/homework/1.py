# 1)დაასრულეთ ყველამ საკლასო სამუშაო

def max_multiple(divisor, bound):
    return (bound//divisor)*divisor


def sum_digits(number):
       return sum(int(digit) for digit in str(abs(number)))


def dont_give_me_five(start,end):
    return len([i for i in range(start, end + 1) if '5' not in str(i)])


def fizzbuzz(n):
     return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else 
        "Fizz" if i % 3 == 0 else 
        "Buzz" if i % 5 == 0 else 
        i 
        for i in range(1, n + 1)
    ]


def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    arr.sort()
    return sum(arr[1:-1])


def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    arr.sort()
    return sum(arr[1:-1])

