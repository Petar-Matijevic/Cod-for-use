def isValid(s):
    stack =[]
    mapping = {')':'(','}':'{',']':'['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False

        else:
            return False


    return not stack

input_string = "{[()]}"

if isValid(input_string):
    print(f"Valid {input_string}")
else:
    print(f"Not Valid {input_string}")