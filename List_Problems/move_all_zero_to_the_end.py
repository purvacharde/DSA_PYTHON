a = [0, 1, 0, 3, 12]

for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)

print(a)