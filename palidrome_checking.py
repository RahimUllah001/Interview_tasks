'''my approach
str = "racecar"
j = 0
for i in range(len(str)):
    j = j-1
    if str[i] == str[j]:
        print(" same")
    else:
        print("n ot same")

'''

# Efficient method
def is_palindrome(s):
    return s == s[::-1]


word = input("enter your word to check: ").lower()

if is_palindrome(word):
    print(f"{word } is palindrome")
else:
    print(f"{word } is not palindrome")    
