# Using startswith()
string = "Hello, World!"
print(string.startswith("Hello")) 

# Using endswith()
print(string.endswith("World!"))  


string1 = "Hello"
string2 = "World"

# Comparing strings
if string1 < string2:
    print(f"{string1} is less than {string2}")
elif string1 > string2:
    print(f"{string1} is greater than {string2}")
else:
    print(f"{string1} is equal to {string2}")
