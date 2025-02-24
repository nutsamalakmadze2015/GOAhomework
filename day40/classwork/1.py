# 1)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი და დააბრუნებს ამ სახელს, ოღონდ ლუწ ინდექსზე მდგომი ასოები უნდა იყოს 
# გადიდებული, კენტ ინდექსზე მდგომი ელემენტები უნდა იყოს დაპატარავებული.
def name_change(name):
    result = ""

    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i].upper()
        else:
            result += name[i].lower()
    return result

print(name_change("nuca"))



