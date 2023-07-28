# with open('students.csv') as file:
#     for line in file:
#         # row = line.rstrip().split(',')
#         # print(f"{row[0]} class is {row[1]}")
#         name, grade = line.rstrip().split(',')
#         print(f"{name} class is {grade}")

# sorting
# with open('students.csv') as file:
#     for line in sorted(file, reverse=True):
#         name, grade = line.rstrip().split(',')
#         print(f'{name} in {grade}')

students = []
with open('students.csv') as file:
    for line in file:
        # student = {}
        name, grade = line.rstrip().split(',')
        # student['name'] = name
        # student['grade'] = grade
        student = {'name': name, 'grade': grade}
        students.append(student)

# print(students)
# for info in students:
#     # print(info)
#     print(f"{info['name']} is in {info['grade']}")

# sorting with the key word
def get_name(student):
    return student['name']

def get_grade(student):
    return student['grade']

for info in sorted(students, key=get_grade, reverse=True):
    print(f"{info['name']} is in {info['grade']}")
# students = {}

