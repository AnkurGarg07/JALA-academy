def find_smaller_larger(num1, num2):
    smaller = min(num1, num2)
    larger = max(num1, num2)
    return smaller, larger


num1 = 5
num2 = 3
smaller, larger = find_smaller_larger(num1, num2)
print(f"Among {num1} and {num2}, the smaller number is {smaller} and the larger number is {larger}")
