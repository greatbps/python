dictionary = {"name":"7D 건조 망고", "type":"당절임", \
              "ingredient":["망고", "설탕", "치자"], "origin":"필리핀"}
print("name", dictionary["name"])
print("type", dictionary["type"])
print("ingredient", dictionary["ingredient"][1])
print("origin", dictionary["origin"])


dictionary["name"] = "준행고"

dictionary["price"] = "5000"
print(dictionary)

