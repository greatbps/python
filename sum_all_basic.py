def sum_all(*values):
    #output = 0
    for value in values:
        value += value
    return value
print(sum_all(1, 3, 4, 6))
