#Author: Gustavo

'''print(1,2,3, end="\t", sep="")
rint("hi")

def fun1(*args):
    print(type(args))
    print(args)
    for val in args:
    print(val)

fun1("a","b","c")

def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(args)
    for val in kwargs:
        print(val)

fun2(name="Joe", age=21, gender="M")'''

def ave(*values):
    numbers_of_values = len(values)
    sum = 0
    for value in values:
        sum += value
    average = sum / numbers_of_values
    return average, sum
        
av1, sum_of_numbers = (ave(1,2,3,4,5,6))
print(f"{av1} and sum is {sum_of_numbers}")
