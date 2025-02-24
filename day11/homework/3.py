#3)შემოატანინეთ მომხარებელს პაროლი და დაბეჭდეთ ეგ პაროლი თუ შემოტანილი
#  პაროლი უდრის თქვენთვის სასურველ პაროლს მაშინ უნდა გამოიტანოს True თუ არადა False

password1 = "catind"
password = input("please enter your password: ")
print(password)
if password1 == password:
    print("True")
elif password1 != password:
    print("False")