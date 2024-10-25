def sum_digits(number):
    import math
    number = abs(number)
    string = str(number)
    total = 0
    for char in string:
        num = int(char)
        total += num

    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')