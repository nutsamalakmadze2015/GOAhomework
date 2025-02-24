#7) codewars  Find the capitals

def capitals(word):
     return [i for i, char in enumerate(word) if char.isupper()]