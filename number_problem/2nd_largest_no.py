# Write a Python program to find the second-largest unique digit in an integer without using sort(), sorted(), or set().

n = int(input('Enter a number:'))

largest = -float('inf')
second = -float('inf')
while n > 0:
    last = n % 10
    if last > largest:
        second = largest
        largest = last
    elif largest != last and second < last:
        second = last
    n //= 10
print(second)