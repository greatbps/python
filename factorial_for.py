def factorial(n):
    output = 1
    for i in range(1, n+1):
            output *= i 
    return output
print(factorial(1))
print(factorial(3))
print(factorial(5))