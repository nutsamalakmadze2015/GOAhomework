#codewars, Jaden Casing Strings
def to_jaden_case(string):
    words = string.split()
    capitalized_words = []
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)
    jaden_cased_string = " ".join(capitalized_words)
    
    return jaden_cased_string
    