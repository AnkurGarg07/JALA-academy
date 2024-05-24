def compare_numbers(num1, num2):
    result = ""

    if num1 < num2:
        result = f"{num1} is less than {num2}"
    elif num1 <= num2:
        result = f"{num1} is less than or equal to {num2}"
    elif num1 > num2:
        result = f"{num1} is greater than {num2}"
    elif num1 >= num2:
        result = f"{num1} is greater than or equal to {num2}"
    else:
        result = f"{num1} is equal to {num2}"

    return result

# Test the function
print(compare_numbers(3, 3))   
print(compare_numbers(3, 5))   
print(compare_numbers(5, 3))  
print(compare_numbers(5, 5))  
