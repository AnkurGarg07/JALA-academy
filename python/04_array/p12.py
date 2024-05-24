def remove_duplicates(arr):
    return list(set(arr))
array = [1, 2, 2, 3, 4, 4, 5]
print("Original array:", array)
print("Array after removing duplicates:", remove_duplicates(array))
