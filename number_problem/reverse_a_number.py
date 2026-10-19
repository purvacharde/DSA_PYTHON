##	Reverse a number.

n = int(input('Enter a no: '))

rev = 0

while n > 0:
    last = n % 10
    rev = rev*10 + last
    n //= 10
print(rev)
    