"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(numbers) // 2):
    j = i * 2 + 1
    #print(j)
    print(f"i = {i}, j = {j}, ")
    numbers[j] = numbers[j] ** 2
print(numbers)"""

for j in range(14, 1, -1):
    if j % 2 == 1:
        print(" "* int(j//2), "*" * int(14 - j), " " * int(j//2))
    
    