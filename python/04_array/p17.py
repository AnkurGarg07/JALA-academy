def remove_duplicates_return_new(arr):
    return list(dict.fromkeys(arr))
array = [1, 2, 2, 3, 4, 4, 5]
print("Original array:", array)
print("New array after removing duplicates:", remove_duplicates_return_new(array))
