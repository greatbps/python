#import datetime

#now = datetime.datetime.now()

month = int(input(">>>>>"))

if 3 <= month <= 5:
    print("봄입니다.")
elif month <=8:
    print("여름입니다.")
elif month <=11:
    print("가을입니다.")
else:
    print("겨울입니다.")