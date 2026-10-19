# Write a Python program to find the largest and smallest digit in a given integer.

n = 583261

large = -float('inf')
small = float('inf')

while n > 0:
    last = n % 10
    if last > large:
        large = last
        
    if small > last:
        small = last
    n //= 10
print(f'The large no is {large} \nThe small no is {small}')