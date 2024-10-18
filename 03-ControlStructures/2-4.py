number1 = int (input('First number: '))
number2 = int (input('Second number: '))
operator = input ("Input the operator (+|-|*|/): ")

if operator == "+":
    print (number1 + number2)
elif operator == "-":
    print (number1 - number2)
elif operator == "*":
    print (number1 * number2)
else:
    print (number1 / number2)