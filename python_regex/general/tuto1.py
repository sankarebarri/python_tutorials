import re

pattern = re.compile(r"\sTP")
result = pattern.findall("PT tutorialsTPpoint PT")
print(result)

result2 = pattern.findall("TP is TPTP and TP all tp")
print(result2)

a = ["june 15", "march 10", "july 4 hj"]
regex = re.compile(r"[a-z]+ \d+")
output = [regex.findall(k) for k in a]
# print(output)

# flatten the output
output = [elem for k in a for elem in regex.findall(k)]
# print(output)

text = "My cat, your dog and my cats are playing with dogs"
pattern = r"dogs?|cats?"
re_obj = re.compile(pattern)
# print(re_obj.findall(text))
