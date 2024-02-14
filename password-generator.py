import secrets
import string

def generate_password(length):
    password = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password += secrets.choice(characters)
    return password

password_length = int(input("Enter password length: "))
generated_password = generate_password(password_length)
print("Your password is:", generated_password)
