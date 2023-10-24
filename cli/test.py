import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--save")
parser.add_argument(
    "--file_name",
    nargs=1
)
parser.add_argument("--show", action="store_true")

args = parser.parse_args()

if args.file_name:
    print(args.file_name[0])
else:
    print("default")

if args.show:
    print("show")
else:
    print("no show")
