def check_even_odd(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

number = 5
result = check_even_odd(number)
print(f"{number} is {result}.")
