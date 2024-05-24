def count_even_odd(arr):

    even_count=0
    for num in arr:
        if(num%2==0):
            even_count+=1
    odd_count = len(arr) - even_count
    return even_count, odd_count

# Test the function
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_even_odd(array)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
