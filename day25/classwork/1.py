#append ფუნქცია სიაში ამატებს გადაცემულ ინდექზე გადაცემულ ელემენტ
#insert ფუნქცია სიის კონკრეტულ ინდექზე ამატებს რაიმე ახალ ელემენტს
#pop ფუნქცია ამოაგდებს რაიმე გადმოცემულ ინდექს 
#len ფუნქცია ითვლის ადამიანისავით ად გამოიყვენს რამდენი სიმბოლოა სიტყვაში

names=["vano","luka","nini","anano","ilia"]
names.insert(4,"nika")

print(names)

name=["vano","luka","nini","anano","ilia"]
name.pop(0)
name.pop(4)
print(name)

num=["1","2","3","4","5","6","7","8","9","10"]
num = input("pleas enter your number: ")
num.pop(3)

name = input("pleas enter your name: ")

if name == 5: 
    print("hello")

else:
    print("bye")