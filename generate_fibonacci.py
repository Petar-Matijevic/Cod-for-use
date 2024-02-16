def fibonacci(n):
    fibonacci_sequence = [0, 1]

    for i in range(2,n):
        next_number = fibonacci_sequence[i-1]+ fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

        # Compute the first five Fibonacci numbers
first_five_fibonacci = fibonacci(5)

        # Print the result
print("The first five Fibonacci numbers:", first_five_fibonacci)