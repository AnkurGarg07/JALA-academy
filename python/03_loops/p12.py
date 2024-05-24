def print_gender(gender):
    if gender.upper() == 'M':
        return "Male"
    elif gender.upper() == 'F':
        return "Female"
    else:
        return "Invalid input"

gender = 'M'
result = print_gender(gender)
print(f"Gender is {result}.")
