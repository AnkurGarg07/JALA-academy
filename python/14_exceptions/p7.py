try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    # Code that always executes
    print("This block always executes.")
