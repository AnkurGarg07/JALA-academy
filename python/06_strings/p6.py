import re

string = "Hello, World!"
pattern = r"Hello"
match = re.match(pattern, string)
if match:
    print("String matches pattern")
else:
    print("String does not match pattern")
