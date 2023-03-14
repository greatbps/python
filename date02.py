import datetime

now = datetime.datetime.now()

if now.hour >= 12:
    print(f"현재 시각은 {now.hour}로 오후입니다.")
else:
    print(f"현재 시각은 {now.hour}로 오전입니다.")