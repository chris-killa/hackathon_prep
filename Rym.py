def convert_to_email(username):
    sanitized_username = "".join(c for c in username if c.isalnum())
    return sanitized_username + "@email.com"

username = get_username()
print("Generated Email:", convert_to_email(username))