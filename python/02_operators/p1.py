def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check if the divisor is not zero to avoid division by zero error
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

# Test the function
print(arithmetic_operation(5, 3, '+'))  # Addition
print(arithmetic_operation(5, 3, '-'))  # Subtraction
print(arithmetic_operation(5, 3, '*'))  # Multiplication
print(arithmetic_operation(5, 3, '/'))  # Division
print(arithmetic_operation(5, 0, '/'))  # Division by zero error
print(arithmetic_operation(5, 3, '%'))  # Invalid operator
