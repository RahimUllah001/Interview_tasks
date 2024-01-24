# 15. Implement a program that counts the number of vowels in a given string.

def count_vowels(word):
    count = 0
    for i in word.lower():
        if i in "aeiou":
            count = count + 1
    print(count)            




given_string = input("enter yr string: ")

count_vowels(given_string)