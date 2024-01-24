# 20. Write a Python function to check if a given string is a pangram (contains all letters of the alphabet)


def is_pangram(g_string):
    unique_alpha = set(c.lower() for c in g_string if c.isalpha()) #list comprehension on set

    return set('abcdefghijklmnopqrstuvwxyz') == unique_alpha

input_string = "The quick brown fox jumps over the lazy dog"

result = is_pangram(input_string)

if result:
    print(f"{input_string} is pangram")
else:    
    print(f"{input_string} is not pangram")
