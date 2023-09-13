import random

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-=+<>/"
    password = ''.join(random.choices(characters, k=length))
    return password

password_length = int(input("Enter password length (should be mare than 12): "))
generated_password = generate_password(password_length)
print("Random password:", generated_password)
