import random
import string

def generate_password(length):
    # Define all possible characters
    letters = string.ascii_letters      # a-z A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # special characters

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate random password
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password


# ---- User Input ----
try:
    length = int(input("Enter desired password length: "))

    if length <= 0:
        print("❌ Length must be greater than 0")
    else:
        password = generate_password(length)
        print("🔐 Generated Password:", password)

except ValueError:
    print("❌ Please enter a valid number")