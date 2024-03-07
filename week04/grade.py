import sys

percentage = float(input("Enter a percentage number (0-100): "))
absoluteValue = abs(percentage)

while True:
    if absoluteValue < 0 or absoluteValue > 100:
        print("Please insert a valid number between 0 and 100")
        sys.exit()
    elif absoluteValue < 40: # we know it is greater than 0 
        print ("Fail") 
        sys.exit()
    elif absoluteValue < 50: # between 40 and 49 
        print ("Pass") 
        sys.exit() 
    elif absoluteValue < 60: # between 50 and 59 
        print ("Merit 1") 
        sys.exit() 
    elif absoluteValue < 70: # between 60 and 69 
        print ("Merit 2") 
        sys.exit() 
    else: # the only option left is between 70 and 100 
        print ("Distinction") 
        sys.exit()

