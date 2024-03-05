x=int(input('Enter the first number: '))
y=int(input('Enter the number that you want divide by: '))
result=int(x//y)
remainder=x%y

print('{} divided by {} is {} with remainder {}'.format(x,y,result,remainder))