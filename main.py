import random
import string

pwLength = int(input("Enter your password length: "))
def generate_password(length=pwLength, include_uppercase=True, include_digits=True, include_special_chars=True):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    length = min(length, len(all_chars))
    password = ''.join(random.sample(all_chars, length))

    return password

password = generate_password()
print("Generated password:", password)
input("Press Enter to close the window...")
