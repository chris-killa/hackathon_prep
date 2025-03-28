from Peyman import get_username
from chioma import remove_special_characters
from Chris import add_at_symbol_to_username
from martin import add_domain_to_username, display_email_address


def main():
    username = get_username()
    clean_username = remove_special_characters(username)
    add_at_symbol = add_at_symbol_to_username(clean_username)
    add_domain = add_domain_to_username(add_at_symbol)
    display_email_address(add_domain)


if __name__ == "__main__":
    main()