def print_n_times(*values,n=3):
    for i in range(n):
        print("i는 {}".format(i))
        for value in values:
            print(value)
        print()

print_n_times("즐거운", "파이썬", "개발", n=5)
