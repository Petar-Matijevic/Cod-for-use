def count_digits(input_string):
    digit_count = sum(character.isdigit() for character in input_string)
    return digit_count

# Testing function
input_string ="abc 123 def 456"
print(count_digits(input_string))
