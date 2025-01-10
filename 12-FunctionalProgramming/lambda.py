'''
def mean(x,y):
    func = (int(x) + int(y))/2
    return func

n1 = input("First number: ")
n2 = input("Second number: ")


result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')
''''''
n1 = int(input("First number: "))
n2 = int(input("Second number: "))

mean = lambda x,y: (x+y)/2

result = mean(n1,n2)
print(f"The arithmetic mean of the numbers {n1} and {n2} is {result}")
''''''
def ms_to_kmh(ms):
    ms = int(ms*3.6)
    return ms
mile = int(input("Miles: "))
result = ms_to_kmh(mile)
print (f"{mile} m/s = {result} km/h")
''''''
mile = int(input("Miles: "))
conv = 3.6
ms_to_kmh = lambda x,y: x*y 

result = int(ms_to_kmh(mile,conv))
print (f"{mile} m/s = {result} km/h")
''''''
def avg_speed(distance,hours,minutes):
    minutes = minutes / 60
    return distance/(hours + minutes)

distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))
result = round(avg_speed(distance,hours,minutes),1)
print (f"Average speed: {result} km/h ")
'''''''
avg_speed = lambda x,y: x/y 

distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))
time = hours + minutes / 60
result = round(avg_speed(distance,time),1)
print (f"Average speed: {result} km/h ")
''''''
number = int(input("Enter your number: "))
is_even = lambda x: x%2
result = is_even(number)

if result == 0:
    print ("Even")
else:
    print ("Odd")
''''''
name = "John"
surname = "Doe"
initials = lambda name,surname: name[0] + surname[0]
print (f"{initials(name,surname)}") 
''''''
def min_pts(limit):
   def check(pts):
      if pts >= limit:
         return True
      return False
   return check

print("=== MIN 50 PTS TO PASS ===")
assess_test = min_pts(50)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")

print("=== MIN 60 PTS TO PASS ===")
assess_test = min_pts(60)
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")
''''''
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
sort = lambda names: sorted(names, key=len)
print (f"{sort(names)}")
''''''
payments = [
    15.90,
    38.47,
    4.07,
    132.70,
    9.15]
pln = lambda data: round((data * 4.5),2)

print (f"{list(map(pln,payments))}")
''''''
sentence = 'I completely agree with you'
result = list(map(lambda sentence:len(sentence) , sentence.split()))
print(f"No. of letters in words: {result}")
''''''
products = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
value = lambda data: (data[0] * data[1])
result = list(map(value, products))
result = sum(result)
print (f"Total value: {result}")
''''''
employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees))
for i in emp_J:
    print(i)
''''''
record = [48,47,54,50,42,68,39,46]
allowed = 50
high = list(filter(lambda e:e > allowed, record))
print("Speed too high:", *high)
'''
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
ari = list(filter(lambda e:e > 2, grades))
for i in ari:
    i = i + i
    

