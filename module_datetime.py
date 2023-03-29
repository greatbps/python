import datetime as dt

now = dt.datetime.now()
print(now)

print(f"{now.year}년 {now.month}월 {now.day}일 입니다.")

print(now.strftime("%Y.%m.%d %H:%M:%S"))
