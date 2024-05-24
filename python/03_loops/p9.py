def is_prime(num):
    if(num==1 | num==0):
        return False
    flag=True
    for i in range(2,num-1):
        if(num%i==0):
            flag=False
            break
    return flag

number=0
if(is_prime(number)):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
