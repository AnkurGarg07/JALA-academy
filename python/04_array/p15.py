def difference_largest_smallest(arr):
    if not arr:
        return None
    return max(arr) - min(arr)
array = [10, 5, 8, 20, 3]
print("Difference between largest and smallest values:", difference_largest_smallest(array))
