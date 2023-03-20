counter = 0
def fibonacci(n):
    print(f"피보나치 {n}를 구합니다.")
    global counter
    counter += 1
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print("-----")
print("fibonacci(10)에 계산된 계사 횟수는{}번입니다.".format(counter))
""" print(f"fibonacci(1) : {fibonacci(1)}")
print(f"fibonacci(2) : {fibonacci(2)}")
print(f"fibonacci(3) : {fibonacci(3)}")
print(f"fibonacci(4) : {fibonacci(4)}")
print(f"fibonacci(5) : {fibonacci(5)}") 
print(f"fibonacci(35) : {fibonacci(35)}") """
