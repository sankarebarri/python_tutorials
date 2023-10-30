import tempfile

# named_file = tempfile.NamedTemporaryFile(
#     dir="./",
#     prefix="temp_start_",
#     suffix="_temp_end"
# )

# print('Named file:', named_file)
# print('Named file name:', named_file.name)

# # Closing the file
# named_file.close()

# Create a temporary directory
# with tempfile.TemporaryDirectory(
#         dir='TempDir',
#         prefix='hey-',
#         suffix='-there'
# ) as tempdir:
#     print("Temp Dir:", tempdir)

# SpooledTemporaryFile: stores data in the memory until the
# maximum size is reached or fileno() is called
sp_file = tempfile.SpooledTemporaryFile(
    max_size=5
)
print(sp_file)

sp_file.write(b"my temp file")
print(sp_file.__sizeof__())

# printing if data is written to the disk
print(sp_file._rolled)  # return False if it's in the memory
print(sp_file._file)
