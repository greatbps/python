class Student:
    def __init__(self, name, age):
        print("객체가 생성되었습니다.")
        self.name = name
        self.age = age
    def print_info(self):
        print(self.name, self.age)

student = Student("이준행", 20)
student.print_info()
