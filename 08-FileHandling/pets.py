total = 0

with open('pets.txt', 'r') as file:
   for line in file:
        words = line.split()
        total += len(words)

print(f" Total amount of words in the file: {total}")
