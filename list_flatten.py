def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
            #output += item
        else:
            output.append(item)
            #output.extend(str(item))
    return output

example = [[1,2], 3, [4, 5,[6, [7, 8]]], 9]
print(f"원본: {example}")
print(f"변환 : {flatten(example)}")