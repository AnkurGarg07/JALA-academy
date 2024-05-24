def print_odd_even(numbers):
    odd_numbers = []
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_even(numbers)
