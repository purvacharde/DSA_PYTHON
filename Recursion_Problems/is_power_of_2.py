# write a program to check if a number is a power of 2 or not using recursion


def is_power_of_2(n, res=1):
    if res == n:
        return 'Power of 2'
    if res > n:
        return 'Not a power of 2'
    return is_power_of_2(n, res * 2)

print(is_power_of_2(16)) 