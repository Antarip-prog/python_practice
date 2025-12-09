print('Hello','you!',sep=', ')

num1 = input('Give first number:')
num2 = input('Give second number:')

print(type(num1))

print(int(num1) + int(num2))

str1 = input('Give first name:')
str2 = input('Give second name:')

print('Hello',str1 , str2, sep=(' '))
print('Hello {}{}'.format(str1,str2))