#1) ჩაწერე განსხვავებული მონაცემთა ტიპების (int, float, string, boolean) ცვლადები.
#დაწერე კოდი, რომელიც ამოწმებს, არის თუ არა მოცემული ცვლადი string ტიპის.
#დაწერე კოდი, რომელიც ამოწმებს, არის თუ არა მოცემული ცვლადი integer ტიპის.
#დაწერე კოდი, რომელიც შეამოწმებს, არის თუ არა მოცემული ცვლადი boolean ტიპის.
#მომხმარებელს შემოატანინეთ სახელი გვარი ასაკი სიმაღლე საყვარელი ფერი და გამოიტანეთ ეს ყველაფერი ერთ დიდ წინადადებაში

age = 9
name = "nia"
num = 5.7
f = False

print(type(age))

print(type(name))

print(type(num))

print(type(f))



name = input("please enter your name : ")
surname = input("please enter your surname: ")
age = input("please enter your age: ")
fav_color = input("please enter your fav_color: ")

print(name + surname + age + fav_color) 