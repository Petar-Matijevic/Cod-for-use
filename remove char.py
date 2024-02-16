import re

input_string = "this is a string with special characters like @ and *"
clean_string = re.sub(r'[^a-z0-9]', ' ', input_string)
print(clean_string)