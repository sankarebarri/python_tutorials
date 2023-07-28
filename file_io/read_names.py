### Reading from files

# simple read
with open('better_name.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    # print(f'hello {line}', end="")
    print(f'hello {line.rstrip()}') # same as above

## shorter code
with open('better_name.txt', 'r') as file:
    for line in sorted(file):
        print(f'hell {line}', end='')

### sorting before reading
names = []
with open('better_name.txt') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f'hello, {name}')