basic_salary = 5000
total_salary = 0
is_bonus = input ("Have you received a bonus? (Y/N): ")
bonus = int(input("Percentage of your bonus: "))

if is_bonus == "Y":
    total_salary = basic_salary + basic_salary * (bonus * 0.01)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')