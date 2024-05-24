def find_second_largest(arr):
    unique_numbers = list(set(arr))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]
array = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print("Second largest number in the array:", find_second_largest(array))
