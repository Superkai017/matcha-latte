def extact_domain(email):
    if "@" not in email:
        raise ValueError("Invalid email address")
    return email.split("@", 1)[1]
print(extact_domain("user@example.com"))