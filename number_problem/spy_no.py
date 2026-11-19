#  Que SPY NO

n = int(input('Enter a number: '))   
# 123 is a spy no because 1*2*3 = 6 and 1+2+3 = 6
res = 1
s = 0

while n > 0:
   last = n % 10
   res *= last
   s += last
   n //= 10

if res == s:
   print('Spy No')
else:
   print('Not a spy no')