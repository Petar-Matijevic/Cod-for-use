# Step 1: Create a Hash Map data structure
char_map ={}

# Step 2: Loop through the string and populate the Hash Map
impute_string = 'Loop through the string and populate the Hash Map'
for char in impute_string:
    if char in char_map:
        char_map[char] +=1
    else:
        char_map[char] = 1

# Step 3: Traverse the Hash Map and print the characters with more than 1 count

matching_char=[char for char, count in char_map.items() if count==1]
print(matching_char)
