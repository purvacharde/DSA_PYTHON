##Write a Python program t.

s = input('Enter a string: ')

for i in s:
    if s.count(i) == 1:
        print(i)
        break
else:
    print("No non-repeating character found.")