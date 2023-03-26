try:
    file = open("info.txt", "w")

    file.close()
except:
    print("오류")
#finally:
print(file.closed)