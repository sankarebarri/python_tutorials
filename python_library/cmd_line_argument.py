import sys

# try:
#     print('Hello, my name is', sys.argv[1])
# except IndexError:
#     print('Too few arguments')

## with no sys.exit()
# if len(sys.argv) < 2:
#     print('Too few arguments')
# elif  len(sys.argv) > 2:
#     print('Too many arguments')
# else:
#     print('Hello, my name is', sys.argv[1])

# # with sys.exit()
# if len(sys.argv) > 2:
#     sys.exit('Too many arguments')
# elif len(sys.argv) < 2:
#     sys.exit('Too few arguments')

# print('Hello, my name is', sys.argv[1])

# printing multiple argv
if len(sys.argv) < 2:
    sys.exit('Too few arguments')
for arg in sys.argv[1:]:
    print('Hello, my name is', arg)