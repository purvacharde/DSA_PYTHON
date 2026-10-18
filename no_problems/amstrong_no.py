# n = int(input('Enter a no: '))
# temp = n
# res = 0
# length = len(str(n))

# while temp > 0:
#     last = temp % 10
#     res += last ** length
#     temp //= 10

# if res == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



n = int(input('Enter a no: '))
temp = n
res = 0
length = 0

while temp > 0:
    last = temp % 10
    length += 1
    temp //= 10

temp = n

while temp > 0:
    last = temp % 10
    res += last ** length
    temp //= 10

if res == n:
    print('Amstrong No')
else:
    print('Not an Amstrong no')

