def remove_special_characters(username):
    """Takes username as an argument, removes all special characters,
    and returns the updated username.
    Example: if the username is user&123_ @
             the function should return user123
    """
    clean_name = []
    for char in username:
        if char.isalnum():
            clean_name.append(char)
    return "".join(clean_name)

if __name__ == "__main__":
    print(remove_special_characters("user&123_ @"))