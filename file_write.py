import random
한글 = '가나다라마바사아자차카타파하'
with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(한글) + random.choice(한글)
        weight = random.randrange(40, 100)
        height = random.randrange(130,180)
        file.write(f"{name}, {weight}, {height}\n")

