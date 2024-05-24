def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

array = [1, 2, 3, 5]
index = 3
value = 4
print("Original array:", array)
print("Array after inserting", value, "at index", index, ":", insert_element(array, index, value))
