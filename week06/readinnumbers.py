def readNum(message = "enter first number: "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
                print("That was not a number!")
    return num

num1 = readNum()
num2 = readNum("enter second number: ")

answer = num1*num2
print(f"Answer is {answer}")
        
