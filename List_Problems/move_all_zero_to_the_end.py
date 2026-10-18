# a = [0, 1, 0, 3, 12]
# a = [0, 0, 1, 2]
# a = [0, 0, 0, 1]
a = [0, 1, 0, 2, 0, 3, 4, 0]

for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)

print(a)