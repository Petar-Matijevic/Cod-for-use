def reverse_number(number):
    reversed_str=str(number)[::-1]

    reversed_num = int(reversed_str)

    return reversed_num

original_number = 12345
reversed_result = reverse_number(original_number)

print(f"The original number: {original_number}")
print(f"The reversed number: {reversed_result}")