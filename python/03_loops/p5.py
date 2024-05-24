def find_largest_number(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    return largest


num1 = 15
num2 = 25
num3 = 10
largest = find_largest_number(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")
