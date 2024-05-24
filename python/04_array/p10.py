def find_duplicates(arr):
    duplicates = []
    seen = []
    for value in arr:
        if value in seen and value not in duplicates:
            duplicates.append(value)
        seen.append(value)
    return duplicates
array = [1, 2, 3, 2, 4, 5, 3]
print("Original array:", array)
print("Duplicate values:", find_duplicates(array))
