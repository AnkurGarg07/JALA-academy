# 1. Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    101: "Ankur",
    103: "Kumkum",
    102: "Laghvi",
    104: "Paras",
    105: "Megha"
}
print("Initial dictionary:", students)

# 1.1 Adding the values in dictionary
students[106] = "Anshika"
print("After adding a value:", students)

# 1.2 Updating the values in dictionary
students[102] = "Laghvi Nagar"
print("After updating a value:", students)

# 1.3 Accessing the value in dictionary
print("Accessing value with key 103:", students[103])

# 1.4 Create a nested loop dictionary
nested_students = {
    101: {"name": "Ankur", "age": 20, "grades": {"math": 90, "science": 85}},
    102: {"name": "Kumkum", "age": 21, "grades": {"math": 75, "science": 80}},
    103: {"name": "Laghvi", "age": 22, "grades": {"math": 85, "science": 90}},
    104: {"name": "Paras", "age": 20, "grades": {"math": 95, "science": 95}},
    105: {"name": "Megha", "age": 21, "grades": {"math": 70, "science": 75}}
}
print("Nested dictionary:", nested_students)

# 1.5 Access the values of nested loop dictionary
print("Accessing nested value for student 101, math grade:", nested_students[101]["grades"]["math"])

# 1.6 Print the keys present in a particular dictionary
print("Keys in students dictionary:", students.keys())

# 1.7 Delete a value from a dictionary
del students[104]
print("After deleting a value with key 104:", students)
