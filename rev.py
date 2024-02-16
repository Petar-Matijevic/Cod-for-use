def reverse_string_with_for_loop(input_string):
    reversed_string = ""
    for char in input_string:
        print(reversed_string)
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
original_string = "hello"
reversed_string = reverse_string_with_for_loop(original_string)
print("Reversed string:", reversed_string)