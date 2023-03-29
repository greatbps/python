students = [{"name": "John","수학": 90, "영어":90, "국어": 60}, 
           {"name": "Vin","수학": 90, "영어":80, "국어": 70},
           {"name": "Alex","수학": 100, "영어":100, "국어": 100},
           {"name": "Tes","수학": 90, "영어":90, "국어": 60}]

print("이름", "총점", "평균", sep="\t")

for student in students:
    #print(student["name"], student["수학"] + student["영어"] + student["국어"])
    score_sum = student["수학"] + student["영어"] + student["국어"]
    avg_score = score_sum / 3
    print(student["name"], score_sum, avg_score, sep="\t")

