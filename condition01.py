number = input("정수를 입려하세요!: ")
if number.isdigit:
    last_charater = number[-1]
else:
    print("정수를 입력하세요.")

last_number = int(last_charater)

if last_number % 2 == 0:
    print(f"입력하신 숫자는 {number} 이고 짝수입니다.")
else :
    print(f"입력하신 숫자는 {number} 이고 홀수입니다.")