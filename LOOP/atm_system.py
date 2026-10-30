# ATM system (loop until user exits).

bal = 10000
while True:
    print('1. Check Balance')
    print('2. Deposite')
    print('3. Withdraw')
    print('4. Exit')
    print()

    a = int(input('Enter your choice: '))

    if a == 1:
        print('Balance :',bal)

    elif a == 2:
        amount = int(input('Enter an amount: '))
        bal += amount
        print('Balance :',bal)

    elif a == 3:
        amount = int(input('Enter an amount: '))
        if amount <= bal:
            bal -= amount
            print('Balance:', bal)
        else:
            print('Insufficient bal')

    elif a == 4:
        break

else:
    print('Invalid Choice')