def check_equality(num1, num2):
    is_equal = (num1 == num2)
    is_not_equal = (num1 != num2)
    
    return is_equal, is_not_equal

num1 = 5
num2 = 3
is_equal, is_not_equal = check_equality(num1, num2)
print(f"Are {num1} and {num2} equal? {is_equal}")
print(f"Are {num1} and {num2} not equal? {is_not_equal}")
num1 = 4
num2 = 4
is_equal, is_not_equal = check_equality(num1, num2)
print(f"Are {num1} and {num2} equal? {is_equal}")
print(f"Are {num1} and {num2} not equal? {is_not_equal}")
