import random
import sys

numberToGuess = 30 
number=random.randint(1,30)
print('Here is a random number from 1 to 30: {}'.format(number))
#guess = int(input("Please guess the number:")) 
while number != numberToGuess: 
    if number < numberToGuess: 
        print("too low") 
        number=random.randint(1,30)
    print('Try again: {}'.format(number)) 
    sys.exit
else: # I know it cant be equal or too low, so it 
    print("too high")
    sys.exit 
    number=random.randint(1,30)
    print('Try again: {}'.format(number)) 
print("Well done! Yes the number was ", numberToGuess)
sys.exit 