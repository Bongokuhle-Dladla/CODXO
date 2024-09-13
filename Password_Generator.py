import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(length))