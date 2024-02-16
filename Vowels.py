    # Input string for a user
input_string = input("Show me what you are: ")

    # Counters
vowel_counter = 0
constant_counter = 0

    # For Loop logic of a program

for char in input_string:
    if char.lower() in "aeiou":
        vowel_counter +=1
        print(char)
    elif char.isalpha():
        constant_counter +=1

    # Print result of program
print("Vowel counter: ", vowel_counter)
print("Constant counter: ", constant_counter)