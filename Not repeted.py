def first_non_repeating_char(input_string):
    char_count={}

    for char in input_string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1

    for char in input_string:
        if char_count[char] == 1:
            return char

    return None
input_string = "abacccdasddbe"
print(first_non_repeating_char(input_string))
