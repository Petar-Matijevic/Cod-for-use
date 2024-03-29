def is_prime(number):
    if number <=1:
        return False
    elif number == 2:
        return True
    elif number % 2==0:
        return False

    # Check for factors up to the square root of the number

    for i in range(3,int(number**0.5)+1,2):
        if number % i == 0:
            return False

    return  True

num_to_check = 177

if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")