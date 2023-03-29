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
def get_score_sum(student):
    return student["math"] + student["korean"] + student["english"]

def avg_score(student):
    return get_score_sum(student) / 3

def student_to_string(student):
    print("{}\t {}\t {}".format(student["name"], get_score_sum(student), round(avg_score(student),2)))

print("이름", "총점", "평균", sep = "\t")

for student in students:
    print(student_to_string(student))