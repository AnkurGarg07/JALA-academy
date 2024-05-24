try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ArithmeticError:
    print("Arithmetic error occurred.")
