# 2)შექმენით ფუნქცია manual_join() რომელიც გააკეთებს იგივე დავალებას რასაც აკეთებს მეთოდი .join() 
# (ანუ შექმენით join-ის კლონი).
def manual_join(iterable, separator=''):
    result = ''
    for i, element in enumerate(iterable):
        if i == len(iterable) - 1:
            result += element
        else:
            result += element + separator
print('result')