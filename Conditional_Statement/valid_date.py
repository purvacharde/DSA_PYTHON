#Write a Python program to check whether a given date is valid.

day = int(input('Enter a day : '))
month = int(input('Enter a month : '))
year = int(input('Enter a year : '))


if month == 2:
    if 1 <= day <= 29:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print('Valid date')
        else:
            print('Not valid')
    else:
        print('Not valid')
elif month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day <= 30:
        print('Valid date')
    else:
        print('Not valid')
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if 1<= day <= 31:
        print('valid date')
    else:
        print('Not valid')

else:
    print('Invalid month')