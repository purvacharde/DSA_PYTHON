a = [10, 5, 20, 8, 15]

if type(a) == list:
    largest = a[0]
    second = None

    for i in a:
        if i > largest:
            second = largest
            largest = i
        elif second != None and i < largest:
            second = i
        elif second == None and i < largest:
            second = i
    print(second)
