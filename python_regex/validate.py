# email = input("What's your email: ").strip()

# username, domain = email.split('@')

# # if username and domain.endswith(".edu"):
# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

# best method using re
import re

re_email = input("What's your email: ").strip()

# if re.search(r"^.+@.+\.edu$", re_email):
# if re.search(r"^[^@]+@[^@]+\.edu$", re_email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", re_email):
# if re.search(r"^\w+@\w\.(edu|gov|com|info)$"): # \w represents [a-zA-Z0-9_]
if re.search(r"^(\w\s)+@\w\.(edu|gov|com|info)$"): # \w represents [a-zA-Z0-9_]
    print("Email Valid")
else:
    print("Email Invalid")

# def test_email(re_email):
#     if re_email == 'sankarebarri@yahoo.com':
#         print('Email Valid')
#     elif re_email == '@yahoo.com':
#         print('No character before @')
#     elif re_email == 'sankarebarri@yahoo.com':



