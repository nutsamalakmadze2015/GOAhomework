# 3)შექმენით ორი ცვლადი, პირველში შეინახეთ ემაილი, მეორეში შეინახეთ პაროლი, შემდეგ მომხმარებელს
#  შეეკითხეთ პაროლი და ემაილი სანამ არ დაემთხვევა სწორ პაროლ და ემაილს.
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