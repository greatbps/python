number = input("정수입력> ")

try:
    number = int(number)
    print(f"원의 반지름은 {number} 입니다.")
    print(f"원의 둘레는 {number * 2 * 3.14} 입니다.")
except Exception as e:
    print(f"오류의 내용은{e}입니다.")