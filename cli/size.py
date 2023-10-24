import argparse

parser = argparse.ArgumentParser()
# a list of allowed arguments to the flag --size
parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M")

args = parser.parse_args()

if args.size == "S":
    print("Small")
elif args.size == "L":
    print("Large")
elif args.size == "XL":
    print("Xtra large")
else:
    print("Medium")
    # print(args)
