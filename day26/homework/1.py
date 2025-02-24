#```დავალება:```

#0)ჩანაწერს გადახედეთ თავიდან.

#1)შექმენით ცარიელი სია, შემდეგ For Loop-ის მეშვეობით ამ სიაში ჩაამატეთ ყველა კენტი რიცხვი 0დან 100მდე, ბოლოს დაბეჭდეთ ეს სია.

#2)მომხმარებელს შემოატანინეთ მისი საყვარელი 5 საჭმელი (For Loop-ის მეშვეობით), შემდეგ შემოატანინეთ რიცხვი და ამ რიცხვის ინდექზე მდგომი ელემენტი ჯერ დაუბეჭდეთ, ბოლო ამოაგდეთ და ამოგდების შემდეგ დაბეჭდეთ სია.

#3)შექმენით სია, მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ შეეკითხეთ როგორ უნდა რო შეცვალოს ეს სახელი / თუ გადმოგცემთ "upper" სიაში დაამატეთ მომხმარებლის სახელი გადიდებულად, თუ გადმოგცემთ "lower" სიაში დაამატეთ დაპატარავებულად, თუ გადმოგცათ "capitalize" სიაში დაამატეთ ისე, რომ სახელის პირველი ასო გადიდებული იყოს...

#4)მომხმარებელს შემოატანინეთ მისი სახელი, თუ ეს სახელი იქნება სიგრძეში 6 სიმბოლოზე მეტი ან ტოლი, მაშინ დაუბეჭდეთ "Hello", თუ იქნება სიგრძეში 5 სიმბოლო, დაუბეჭდეთ "Ola", სხვა შემთხვევაში დაუბეჭდეთ "Bonju".

#5)შექმენით ორი ცარიელი სია (odd = [] / even = []), შემდეგ For Loop-ის მეშვეობით შექმენით რიცხვების თანმიმდევრობა 0დან 100მდე და გაფილტრეთ ეს რიცხვები (ლუწი რიცხვები ჩაამატეთ even სიაში, ხოლო კენტი რიცხვები ჩაამატეთ odd სიაში) ბოლოს დაბეჭდეთ ორივე სია.

#6)შექმენით სია 5 ელემენტით, მომხმარებელს შემოატანინეთ მისი საყვარელი საჭმელი და ასევე შემოატანინეთ რიცხვი, შემდეგ მომხმარებლის საყვარელი საჭმელი ჩასვით სიაში იმ ინდექსზე რომელი რიცხვიც შემოიტანა, ბოლოს დაბეჭდეთ სია. 

numbers=[]

for i in range (0,101):
    if i %  2 == 0 :
        numbers.append(i)
print(numbers)

food =input("pleas enter your food: ")
food1 =input("pleas enter your food: ")
food2 =input("pleas enter your food: ")
food3 =input("pleas enter your food: ")
food4 =input("pleas enter your food: ")
food5 =input("pleas enter your food: ")

name = input("pleas enter your name: ")
if name (".upper"):
    print(name.upper())
elif name (".lower"):
    print(name.lower())
else:
    print(name.capitalize())


odd = []
even = []


for i in range(101):
    if i % 2 == 0:
        even.append(i)  
    else:
        odd.append(i)   


print("even numbers:", even)
print("odd numbers:", odd)


food_list = []


for i in range(5):
    food = input("pleas enter your favorit food ")
    index = int(input("The number where you want to add it: "))




    

    food_list.insert(index, food)


print("ფინალური სია:", food_list)