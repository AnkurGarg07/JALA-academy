def is_armstrong_number(num):
    num_str=str(num)
    num_length=len(num_str)
    sum=0
    for digit in num_str:
        sum=sum+ (int(digit)**num_length)

    return sum==num

number = 1634
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

