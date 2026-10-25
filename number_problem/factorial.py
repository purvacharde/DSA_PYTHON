# Factorial

n = int(input('Enter a no: '))
fact = 1
for i in range(2, n+1):
    fact *= i
print(fact)