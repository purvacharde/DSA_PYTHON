##	Reverse number and check palindrome.

n = int(input('Enter a no: '))

temp = n
rev = 0

while temp > 0:
    last = temp % 10
    rev = rev*10 + last
    temp //= 10

if n == rev:
    print('Palindrome')
else:
    print('Not a Palindrome')