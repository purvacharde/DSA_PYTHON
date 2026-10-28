# Rotate list by K positions.

a = [1, 2, 3, 4, 5]
k = 3

r = k % len(a)
m = a[-r:] + a[:-r]
print(m)