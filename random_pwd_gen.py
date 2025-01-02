import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generates a strong password with the given options.

    Parameters:
        length (int): Length of the password (default: 12).
        use_uppercase (bool): Include uppercase letters (default: True).
        use_digits (bool): Include numbers (default: True).
        use_special_chars (bool): Include special characters (default: True).

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 for adequate strength.")

    # Create a pool of characters
    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Ensure the password meets all criteria
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/"))
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return ''.join(password)


# Example usage
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")