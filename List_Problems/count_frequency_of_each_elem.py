##Write a Python program to count how many times each element appears in a list, without using count() or importing any module.

a = [1, 2, 2, 3, 1, 2, 4, 3]
b = []
for i in a:
    if i not in b:
        count = 0
        for j in a:
            if i == j:
                count += 1
        b.append(i)
        print(i, ':', count)