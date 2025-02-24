# 1)დაასრულეთ აუცილებლად საკლასო დავალება ვისაც არ დაგისრულებიათ:
#     1.1)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი და დააბრუნებს ამ სახელს, ოღონდ ლუწ ინდექსზე მდგომი ასოები უნდა იყოს გადიდებული, კენტ ინდექსზე მდგომი ელემენტები უნდა იყოს პატარა.
#     1.2)შექმენით ფუნქცია manual_join() რომელიც გააკეთებს იგივე დავალებას რასაც აკეთებს მეთოდი .join() (ანუ შექმენით join-ის კლონი).
#     1.3)შექმენით ორი ცვლადი, პირველში შეინახეთ ემაილი, მეორეში შეინახეთ პაროლი, შემდეგ მომხმარებელს შეეკითხეთ პაროლი და ემაილი სანამ არ დაემთხვევა სწორ პაროლ და ემაილს.

def name_change(name):
    result = ""

    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i].upper()
        else:
            result += name[i].lower()
    return result

print(name_change("nuca"))


def manual_join(iterable, separator=''):
    result = ''
    for i, element in enumerate(iterable):
        if i == len(iterable) - 1:
            result += element
        else:
            result += element + separator
    return result


def check_email_password():
    email = "example@email.com"
    password = "securepassword123"
print(check_email_password)   
while True:
        email = input("Please enter email: ")
        password = input("Please enter password: ")

        if  email == email and password ==password:
            print("Login was successful.")
            break
        else:
            print("email is incorect,Try again.")