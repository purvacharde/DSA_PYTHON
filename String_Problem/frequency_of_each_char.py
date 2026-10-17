a = 'this is a python'
b = []

for i in a:
    if i not in b:
        count = 0
        for j in a:
            if i == j:
                count += 1
        b.append(i)
        print(i, ':', count)