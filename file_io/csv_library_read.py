import csv

students = []

# if the csv file does not have a header
# with open('students.csv') as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({'name': row[0], 'grade': row[1]})
#     for name, grade in reader:
#         students.append({'name': name, 'grade': grade})

# if the csv file has a header
with open('students_read.csv') as file:
    reader = csv.DictReader(file)
    # for row in reader:
    #     students.append({'name': row[0], 'grade': row[1]})
    for row in reader:
        # print(row)
        # students.append({'name': row['name'], 'grade': row['grade']})
        students.append(row)

for student in sorted(students, key=lambda student: student['name'], reverse=True):
    print(f"{student['name']} is in {student['grade']}")



