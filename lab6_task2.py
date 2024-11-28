class Subject:
    def __init__(self, name:str, estimation:int):
        self.name = name
        self.estimation = estimation

class Student:
    def __init__(self, fio:str, group:str, subjects:Subject=[5]):
        self.fio = fio
        self.group = group
        self.subjects = subjects


print("!------------------ [ Student manager ] ------------------!")
students = []

for i in range(5):
    students.append(Student(input("FIO: "),input("Group: "), [Subject(input("Subject name: "), int(input("Subject estimation: "))),Subject(input("Subject name: "), int(input("Subject estimation: "))),Subject(input("Subject name: "), int(input("Subject estimation: "))),Subject(input("Subject name: "), int(input("Subject estimation: "))),Subject(input("Subject name: "), int(input("Subject estimation: ")))]))

resultStudents = []
for student in students:
    averageStore = 0
    for subject in student.subjects:
        averageStore += subject.estimation
    averageStore /= 5
    if averageStore > 4.0:
        resultStudents.append(student)

if resultStudents.count == 0:
    print("No students with an average score of more than 4 were found")
    exit
print("!------------------ [ RESULT ] ------------------!")
for student in resultStudents:
    print(f"FIO: {student.fio} Group: {student.group}")