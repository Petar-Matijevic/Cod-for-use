string1 = input("String 1: ")
string2 = input("String 2: ")

if len(string2) != len(string1):
    print("The strings are not anagram")
else:
    char_array1 = sorted(list(string1))
    char_array2 = sorted(list(string2))
if char_array1 == char_array2:
    print("The two strings are anagrams")
else:
    print("The two strings are not anagrams")
