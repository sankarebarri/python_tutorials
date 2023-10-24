import argparse

parser = argparse.ArgumentParser()
# telling that -v and -s can't be used at once
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-s", "--silent", action="store_true")

args = parser.parse_args()
print(args)
