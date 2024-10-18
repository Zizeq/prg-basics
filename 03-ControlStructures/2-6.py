number = int(input("Input your number: "))

if number < 0:
    print(f'{number} is negative')
elif number > 0:
    print(f'{number} is positive')
else:
    print(f'{number} is 0')