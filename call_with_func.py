def power(item):
    return item * item

def under_item(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
output_b = filter(under_item, list_input_a)
print(output_a)
#print(power(30))
print(list(output_a))

print(list(output_b))

