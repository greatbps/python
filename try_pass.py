list_input_a = [1, 234, 456, "cat", 32456]

list_no = []

for item in list_input_a:
    try:
        a = int(item)
        list_no.append(a)
    except:
        pass
print(list_no)