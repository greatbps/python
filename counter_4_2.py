numbers = [1, 1, 1, 2, 3, 5, 6, 3, 2, 7, 8, 3, 5, 5, 2, 1, 9]

counter = { }

for number in numbers:
    counter[number] = 0 
for number in numbers:
    counter[number] += 1 
print(counter)
