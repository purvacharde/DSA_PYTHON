a = [12, 5, 8, 5, 2, 10, 2]

if type(a) == list and len(a) > 1:
    second = float('inf')
    smallest = a[0]
    for i in a:
        if i < smallest:
            second = smallest
            smallest = i
        elif smallest < i and second > i:
            second = i
    print(second)
else:
    print('Not a list')