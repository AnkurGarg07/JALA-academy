def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

array = [10, 20, 30, 40, 50]
value = 30
print("Original array:", array)
print("Array after removing", value, ":", remove_element(array, value))
