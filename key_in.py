dictionary = {"name":"7D 건조 망고", "type":"당절임", \
              "ingredient":["망고", "설탕", "치자"], "origin":"필리핀"}

value = dictionary.get("존재하지 않는 키")
print("값", value)
if value == None:
    print("부존재 키 접근")