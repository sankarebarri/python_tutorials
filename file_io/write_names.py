### write names to the file

# for _ in range(3):
#     name = input("What's your name? ")
#     file = open('name.txt', 'a')
#     file.write(f"{name}\n")
#     file.close()


for _ in range(3):
    name = input('What is your name? ')
    with open('better_name.txt', 'a') as file:
        file.write(f'{name}\n')