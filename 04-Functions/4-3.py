def triangle_area(a,b,c):
    import math
    area = (0.5 * (a+b+c))
    result = math.sqrt(area*(area - a)*(area - b)*(area - c))
    return result
a = int(input("First Number: "))
b = int(input("First Number: "))
c = int(input("First Number: "))
value = triangle_area(a, b, c)

print(f'The area of ​​a triangle with sides {a},{b},{c} is {value}')
