# 9. Create a program that generates a random password with a mix of letters, numbers, and special characters.


import random
import string




def generate_password(length = 8):
    caracters = string.ascii_letters + string.digits +string.punctuation

    password = ''.join(random.choice(caracters) for _ in range(length) )
    return password


rando_pasword = generate_password()

print(f"{rando_pasword} is random generated password")