# 1)ცვლადში შეინახეთ ორიგინალი აქაუნთის სახელი, პაროლი და ემაილი, შემდეგ მომხმარებელს შეეკითხეთ მისი აქაუნთის სახელი,
#  პაროლი და ემაილი (input-ის მეშვეობით) ეს ყველაფერი შეინახეთ ახალ ცვლადებში და შეამოწმეთ უდრის თუ არა ინფუთით 
# შემოტანილი აქაუნთის მონაცემები, ორიგინალ აქაუნთის მონაცემებს


name = "nuca"
pasword = "malakmadzen23"
Email = "malakmadzeN@gmail.com"

name1 = input("please enter your name: ")
pasword1 = input("please enter your password: ")
Email1 = input("please enter your Email: ")

if name == name1 and pasword == pasword1 and Email == Email1:
    print("your loged in")
else:
    print("sorry Try again")