raw_input = input("Inch 단위의 숫자를 입력해 주세요!: ")
inch = int(raw_input)
cm = inch * 2.54

#print(inch, "inch는 cm 단위로", cm, "cm입니다.")
print("{} inch는 cm 단위로 {} cm입니다.".format(inch, cm) )