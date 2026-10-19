##	Sum of digits of a number.

n = int(input('Enter a no: '))

sum = 0

while n > 0:
    last = n % 10
    sum += last
    n //= 10
print(sum)