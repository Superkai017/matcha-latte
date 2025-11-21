def is_valid_password(password):
    
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    else:
        return True
print(is_valid_password("Password123"))