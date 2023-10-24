import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--dividend", type=int)
parser.add_argument("--divisor", type=int)

args = parser.parse_args()
if args.divisor == 0:
    print("")
    sys.exit("can't divide by zero")
print(args.dividend / args.divisor)
