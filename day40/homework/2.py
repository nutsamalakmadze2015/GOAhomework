# 2)ასევე შეასრულეთ შემდეგი Codewars ები:
# https://www.codewars.com/kata/53af2b8861023f1d88000832
def are_you_playing_banjo(name):
    if name[0] == "R":
        return name + " plays banjo" 
    elif name[0] == "r" :
        return name +" plays banjo" 
    else:
        return name + " does not play banjo"
# https://www.codewars.com/kata/57eae65a4321032ce000002d
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result
# https://www.codewars.com/kata/5772da22b89313a4d50012f7
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 	'Hello guest'
# https://www.codewars.com/kata/58649884a1659ed6cb000072
def update_light(current):
    if current =="green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"