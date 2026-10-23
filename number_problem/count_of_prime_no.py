#Write a Python program to count how many prime digits are present in an integer.


n = int(input('Enter a number:'))

count = 0

while n > 0:
    last = n % 10

    if last > 1:
        for i in range(2, last):
            if last % i == 0:
                break
        else:
            count += 1
    n //= 10
print('The count of prime no is', count)