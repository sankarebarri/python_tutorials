# read out from the students.csv
students = []
with open('students.csv') as file:
    for line in file:
        name, *grade = line.rstrip().split(',')
        student = {'name': name, 'grade': grade}
        students.append(student)

for student in sorted(students, key=lambda student: student['name'], reverse=True):
    print(f"{student['name']} is in {student['grade']}")
        