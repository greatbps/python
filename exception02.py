list_a = [1, 2, 3, 4, 5]

num = input("정수입력> ")

try:
    num = int(num)
    print(list_a[num])
except ValueError as v:
    print(type(v))
except IndexError as i:
    print(type(i))
 