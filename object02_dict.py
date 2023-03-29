def create_student(name, math, korean, english):
    return {"name": name,
            "math" : math,
            "korean" : korean,
            "english" : english}

students = [create_student("이준한", 100, 100, 100),
            create_student("노경배", 80, 60, 90),
            create_student("이숙정", 70, 80, 90),
            create_student("박수정", 90, 100, 90),
            create_student("김영민", 90, 90, 100) 
            ]

for student in students:
    #print(student["name"], student["수학"] + student["영어"] + student["국어"])
    score_sum = student["math"] + student["korean"] + student["english"]
    avg_score = score_sum / 3
    print(student["name"], score_sum, avg_score, sep="\t")