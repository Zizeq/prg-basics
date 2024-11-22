"""
arr = [2, 3, 7, 5, 4] #4

print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(len(arr)-1)
sum = arr[0] + arr[-1]
print(sum)
print(arr[len(arr)//2])
for i in range(len(arr)):
    if i != len(arr) - 1:
        print(arr[i], end=" ")
    else:
        print(arr[i]) 
        
arr = [1,2,3,4,5] #5
print(arr)
arr[0] -= 1
print(arr)
arr[-1] += 4
print(arr)
arr[len(arr)//2] = arr[len(arr)//2] * 2
print(arr)

def weekday(n): #6
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

print (weekday(1))
print (weekday(4))
print (weekday(7))  

shopping_list = [ #7
   "milk", "bread", "eggs", "butter", "cheese",
   "tomatoes", "potatoes", "carrots", "onions", "garlic"
]
for item in shopping_list:
   print(item)


computer_games = [ #8
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
computer_sorted = sorted(computer_games)

index = 0

while index < len(computer_sorted):
    print(f"{index + 1}. {computer_sorted[index]}")
    index += 1


polish_license_plates = [ #9
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]
counter = 1
for car_number in polish_license_plates:
   if car_number.startswith("KR") or car_number.startswith("KK") :
      print(counter, car_number)
      counter += 1



test_results = [ #10
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

question_number = len(test_results)

correct_answers = 0
incorrect_answers = 0
for answer in test_results:
   if answer == True:
      correct_answers += 1

# calculates the number of incorrect answers
   if answer == False:
      incorrect_answers += 1

# calculates the percentage of correct answers
percent = (correct_answers / question_number)

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f"Percentage of correct answers: {round(percent*100, 1)}%")


temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Number of measurements
measurements = len(temperatures)

# Calculates the total of all temperatures
temp_total = 0
for temp in temperatures:
    temp_total += temp  # Summing up the temperatures

# Calculates average temperature
avg_temp = temp_total / measurements 

# Calculates min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# Calculates the number of days with negative temperatures
negative_temp = 0
i = 0
while i < measurements:
    if temperatures[i] < 0:
        negative_temp += 1
    i += 1

# Prints out the monthly weather report
print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', measurements)
print('Average temperature in the month:', avg_temp)
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)
"""
categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expenses = max(expenses)
max_index = expenses.index(max_expenses)

most_expensive = categories[max_index]

print(most_expensive)


