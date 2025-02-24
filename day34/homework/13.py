#
#2)შექმენით manual_split ფუნქცია

#3)შექმენით manual_replace ფუნქცია

#4)შექმენით manual_join ფუნქცია

#5)კომენტარებით ახსენით რას აკეთებს split,join,replace ფუნქციები

def manual_split(str,symbol):
     result = []
     test = ""

     for i in str:

        if i != symbol:
            test += i
        else:
            result.append(test)
            test = ""

     return result
            

print(manual_split("hello this  group 45"," "))

def manual_replace(text, old, new):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:  # ეძებს ძველ სიტყვას
            result += new  # ცვლის ახალით
            i += len(old)  # უშვებს მოძებნილი სიტყვის სიგრძეს
        else:
            result += text[i]
            i += 1
    return result





def manual_join(brr,symbol):
        result = ""

        for i in brr:
            result += i + symbol

        return result[0:-1]


print(manual_join(["nuca","lika","luka","nika"],"&"))






#manual_split: თუ გაქვთ სტრიქონი, მაგალითად "apple,banana,grape", და სეპარატორად ",", ფუნქცია დაარეჩება: ["apple", "banana", "grape"].
#manual_replace: თუ გაქვთ სტრიქონი "hello world" და გსურთ "world"-ის შეცვლა "everyone"-ით, შედეგი იქნება "hello everyone".
#manual_join: თუ გაქვთ ლისტი ["apple", "banana", "grape"] და სეპარატორად ",", შედეგი იქნება "apple,banana,grape"




