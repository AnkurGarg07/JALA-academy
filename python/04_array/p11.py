def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
print("Common values between arrays:", find_common_values(array1, array2))
