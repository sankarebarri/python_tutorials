import tempfile

# temp_file = tempfile.TemporaryFile(
#     dir="./"
# )

# try:
#     # writing to the temporary file
#     temp_file.write(b"This is my tempfile")
#     # position to start reading the file
#     temp_file.seek(0)  # reading starts from the beginning
#     # reading the file
#     data = temp_file.read()
#     print(data)
# finally:
#     temp_file.close()

# Using context manager
with tempfile.TemporaryFile(mode="w+t", dir="./") as file:
    file.write("My temporary file")
    file.seek(0)
    print(file.read())
    file.close()
