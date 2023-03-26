user_input_a = input("정수입력>: ")

if user_input_a.isdigit():
    number = int(user_input_a)
    print(f"원의 지름은{number} 입니다.")
    print(f"원의 둘레는{number * 2 * 3.14} 입니다.")
    print(f"원의 넓이는{3.14 * number ** 2} 입니다.")
