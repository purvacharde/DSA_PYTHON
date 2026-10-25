# W A Function to check the no is strong or not

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def is_strong(n):
    temp = n
    res = 0

    while n:
        last = n % 10
        res += fact(last)
        n //= 10

    if res == temp:
        return 'Strong No'
    else:
        return 'Not a strong no'
print(is_strong(145))
