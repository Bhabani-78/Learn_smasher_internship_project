import itertools

def check_brute_force(password):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;':,.<>?`~"
    for length in range(1, len(password) + 1):
        for attempt in itertools.product(chars, repeat=length):
            if ''.join(attempt) == password:
                return True
    return False

def check_dictionary_attack(password):
    with open('common_passwords.txt', 'r') as file:
        common_passwords = [line.strip() for line in file]
    if password in common_passwords:
        return True
    return False

def check_password_strength(password):
    strength = []
    if len(password) < 8:
        strength.append("Password length should be at least 8 characters.")
    if not any(char.isdigit() for char in password):
        strength.append("Password should contain at least one digit.")
    if not any(char.isalpha() for char in password):
        strength.append("Password should contain at least one letter.")
    if not any(char.isupper() for char in password):
        strength.append("Password should contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        strength.append("Password should contain at least one lowercase letter.")
    if not any(char.isalnum() for char in password):
        strength.append("Password should contain at least one special character.")
    if check_brute_force(password):
        strength.append("Password is vulnerable to brute force attack.")
    if check_dictionary_attack(password):
        strength.append("Password is vulnerable to dictionary attack.")
    return strength

password = input("Enter a password to check its strength: ")
strengths = check_password_strength(password)
if strengths:
    print("Password is weak. Please consider the following:")
    for s in strengths:
        print("- " + s)