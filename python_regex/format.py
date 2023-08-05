name = input("What's your name: ").strip()

# if "," in name:
#     last, first = name.split(", ?")
#     name = f"{first} {last}"
# print(f"hello, {name}")
import re

# matches = re.search(r'^(.+), (.+)$', name)
# matches = re.search(r"^(.+), ?(.+)$", name)
# matches = re.search(r"^(.+), *(.+)$", name)
matches = re.search(r"^(.+), *(.+)$", name)
# if matches := re.search(r"^(.+), *(.+)$", name): ### walrus expression in python 3.8+ 
if matches:
    # last, first = matches.groups()

    # last = matches.group(1)
    # first = matches.group(1)

    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
    # print(matches.groups())
print(f"hello, {name}")