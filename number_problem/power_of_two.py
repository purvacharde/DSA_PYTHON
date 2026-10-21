##Write a Python program to check whether a number is a power of 2 using a bitwise operator.

a = int(input('Enter a no: '))

if a > 0 and (a & (a-1))== 0:
    print('Power of 2')
else:
    print('Not a power of 2')
