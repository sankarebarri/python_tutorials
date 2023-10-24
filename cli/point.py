import argparse

parser = argparse.ArgumentParser()

# nargs means it requires 2 arguments
parser.add_argument(
    "--coordinates",
    nargs=2,
    metavar=("X", "Y"),
    help="take the cartesian coordinates %(metavar)s"
)
args = parser.parse_args()
print(args)

# it requires 0 or more arguments
# parser.add_argument("numbers", nargs="*", type=float)
# args = parser.parse_args()
# print(sum(args.numbers))

# it requires at least 1 arguments
# parser.add_argument("files", nargs="+")
# args = parser.parse_args()
# print(args)

# you can combine both + and * in the same code
# parser.add_argument("--veggies", nargs="+")
# parser.add_argument("--fruits", nargs="*")
# args = parser.parse_args()


# print(args)
