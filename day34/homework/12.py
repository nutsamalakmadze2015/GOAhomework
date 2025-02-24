#12) codewars, Sum without highest and lowest number

def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    arr.sort()
    return sum(arr[1:-1]) 