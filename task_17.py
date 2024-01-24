# 17. Write a Python program to find and replace a specific word in a text document.


def find_replace_word(file_path,old_word,new_word):
    with open(file_path, "r") as file:
        content = file.read()

    new_content = content.replace(old_word,new_word)


    with open(file_path, "w") as file:
        file.write(new_content)



file_path = "task_17.txt"
old_word = "apple"
new_word = "mango"

print(f'The word "{old_word}" has been replaced with "{new_word}" in {file_path}.')

find_replace_word(file_path,old_word,new_word)
