price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for key,value in price_list.items():
   print(f"{key} : {value}")
before = 0
for key, value in price_list.items():
    before = before + value
before = round(before, 2)
print(before)
after = 0
for key, value in price_list.items():
    value = value * 0.9
    value = round(value, 2)
    print(f"{key} : {value}")
    after = after + value
after = round(after, 2)
print(after)