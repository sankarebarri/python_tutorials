import csv

for _ in range(2):
    name = input("What's your name? ")
    home = input("What's your home? ")

    # # using .writer()
    # with open('students_write.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     writer.writerow([name, home])

    # using .DictReader()
    with open('students_write.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'home'])
        writer.writerow({"name": name, "home": home})