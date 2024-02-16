def are_rotations(str1,str2):
    if len(str1) != len(str2):
        return False
    temp=str1+str2
    if str2 in temp:
        return  True
    return False

# Test the function
string1 = "hello"
string2 = "lohel"
print(are_rotations(string1, string2))