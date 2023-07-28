# with open('better_name.txt', 'r') as file:
#     lines = file.readlines()

# for line in lines:
#     # print(f'hello {line}', end="")
#     print(f'hello {line.rstrip()}') # same as above

### shorter code
with open('better_name.txt', 'r') as file:
    for line in file:
        print(f'hell {line}', end='')