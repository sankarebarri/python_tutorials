email = input("What's your email: ").strip()

username, domain = email.split('@')

# if username and domain.endswith(".edu"):
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
