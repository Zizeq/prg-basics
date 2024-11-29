# Creates a shopping list based on product names
# entered from the keyboard.

# shopping list file name
shopping_list = 'shopping_list.txt'

# Adds product name at the end of a shopping list
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')  # Write each product on a new line

# Takes next product name from the keyboard
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        # Stops entering product names
        print("Shopping list creation stopped.")
    else:
        add_product(shopping_list, product)
        print(f"Added '{product}' to the shopping list.")