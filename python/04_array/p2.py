def average_of_array(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)

array = [1, 2, 3, 4, 5]
print("Average of array:", average_of_array(array))
