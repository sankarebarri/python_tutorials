import tempfile

tempfile = tempfile.TemporaryFile(
    dir="./"
)

print(f"Temporary object: {tempfile}")
print(f"Tempfile name: {tempfile.name}")
tempfile.close()
