power = lambda x:  x * x
under = lambda x: x < 3

list_input_a = {1, 2, 3, 4, 5}

output_a = map(power, list_input_a)
output_b = filter(under, list_input_a)

print(output_a)
print(list(output_a))

print(output_b)
print(list(output_b))

