#4)codewars, Regex count lowercase letters
def lowercase_count(strng):
        return sum(1 for char in strng if char.islower())