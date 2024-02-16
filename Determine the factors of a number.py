def find_factors(number):
    factors = []

    for i in range(1,int(number**0.5)+1):
        if number % i == 0:
            factors.append(i)
            if i !=number // i:
                factors.append(number//i)

    return factors

number_to_factorize = 12
result_factors = find_factors(number_to_factorize)

print(f"The factors of {number_to_factorize} are: {result_factors}")