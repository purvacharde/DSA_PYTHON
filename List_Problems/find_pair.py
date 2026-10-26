#16.Find pairs in list whose sum = target value.

a = [2, 5, 8, 10, 6, 1, 5, 2, -1]

t = 9

for i in range(len(a)):
   for j in range(i+1, len(a)):
       if a[i] + a[j] == t:
           print((a[i], a[j]))
    