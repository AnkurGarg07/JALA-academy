def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1


array = [10, 20, 30, 40, 50]
value = 30
index = find_index(array, value)
if index != -1:
    print(f"Index of {value}:", index)
else:
    print(f"{value} not found in the array.")
